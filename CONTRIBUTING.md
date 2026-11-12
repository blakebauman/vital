# Contributing to Vital

Vital is a Claude Code / Cowork plugin: a team of agents and a set of skills for an AI agency that takes finished tech products to market. This guide covers how the repo is laid out, the rules every change must follow, and how to build and validate locally.

## Repository layout

The repo is a marketplace with one plugin. Everything users install lives in `plugins/vital/`; nothing else ships.

```
.claude-plugin/marketplace.json                # marketplace — source: ./plugins/vital
plugins/vital/.claude-plugin/plugin.json       # plugin manifest (name, displayName, version, description)
plugins/vital/agents/*.md                      # one subagent per file (YAML frontmatter + system prompt)
plugins/vital/skills/<name>/SKILL.md           # one skill per directory (YAML frontmatter + instructions)
plugins/vital/skills/<name>/references/        # optional deeper reference material for a skill
plugins/vital/skills/<name>/evals/evals.json   # the skill's eval cases
plugins/vital/hooks/                           # hooks.json + the scripts it runs
plugins/vital/README.md                        # user-facing docs; the directory listing page
plugins/vital/CONNECTORS.md                    # recommended connectors
scripts/validate.py                            # repo validator — never shipped
docs/                                          # install + eval guides
```

Paths in the rules below are relative to `plugins/vital/`.

The repo root **is** the plugin, so it can be installed directly from the GitHub URL.

## The rules (enforced by `scripts/validate.py` and CI)

These come from Claude Code's plugin spec and from install failures we have already hit. A change that breaks any of them will fail CI.

**Agents** (`agents/*.md`)

- `name` must be **3–50 characters**, kebab-case, and **unique** across all agents. (A 2-char name like `pr` fails — that is why the PR agent is `pr-comms`.)
- `color` must be one of: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`. **`magenta` is not valid.** Colors may repeat across agents.
- `model` should be `inherit` (default) or a valid alias (`sonnet`, `opus`, `haiku`, `fable`) or a full model ID.
- `description` is required and should say **when to delegate** to the agent, with trigger phrases. Keep `<example>` blocks in the body, not the frontmatter, so the YAML stays valid.
- Restrict `tools` only when the agent should be limited (e.g. the `engineering` advisor is read-only + web).
- List the skills the agent owns under `skills:` (a YAML list). They are preloaded into the agent's context when it starts, so a specialist begins with its playbook instead of rediscovering it. Preload only skills the agent owns — every preload costs context on every delegation. The validator checks each name exists.

**Hooks** (`hooks/hooks.json`)

- Hooks run on the user's machine, so keep them local, read-only, fast, and silent when they don't apply. No network calls — the same rule as no bundled MCP servers.
- Put hook scripts in `hooks/` and reference them as `${CLAUDE_PLUGIN_ROOT}/hooks/<file>`. Inside the script, use no environment variables (not even `$CLAUDE_PROJECT_DIR`) and no command substitution — Anthropic's directory holds those for manual review. Hooks run from the project directory, so relative paths like `.vital/` work.

**Skills** (`skills/<name>/SKILL.md`)

- Every skill directory must contain a `SKILL.md` with valid YAML frontmatter.
- `name` must match the directory name. `description` is required and should be third-person with trigger phrases in quotes. Both agent and skill descriptions are capped at 1024 chars.
- Add `allowed-tools` (e.g. `WebSearch, WebFetch, Read, Write`) for skills that do web research or produce files, so those turns don't stop for permission prompts. Only real tool names pass validation.
- Keep `SKILL.md` lean; move long reference material to `references/`.
- Follow the [Agent Skills spec](https://agentskills.io/specification): `name` lowercase kebab-case, max 64 chars, matching the directory; optional `compatibility` (max 500 chars) when a skill depends on Vital's agents or a host feature.
- **Entry points are skills, not commands.** `/vital:launch`, `/vital:status`, and `/vital:readiness` are `skills/launch`, `skills/status`, and `skills/readiness` with `disable-model-invocation: true`, so they run only when the user types them. Each names the agent it runs through *and* an inline fallback for hosts without Vital's agents. Do not add a `commands/` directory — it is the legacy format.
- Every skill needs `evals/evals.json` with ids 1–3 (happy path) and 4 (adversarial); the validator enforces it. Fixture files go under `evals/files/` (a `.vital/` fixture there is un-ignored in `.gitignore`).
- **Reference paths must be `${CLAUDE_PLUGIN_ROOT}`-prefixed.** Write `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/references/<file>.md`, never a bare `references/<file>.md` — the harness expands the variable at load time, but a bare relative path is resolved against the user's working directory and silently fails once the plugin is installed. The validator enforces the prefix and checks the target exists.
- **Degrade gracefully across hosts.** `pptx`, `xlsx`, `dataviz`, and `my-writing-style` are not present in every host. Reference them only with a stated fallback ("...via the `xlsx` skill when available, a markdown table otherwise"), and add any new external dependency to `EXTERNAL_SKILLS` in `scripts/validate.py`.
- **Every skill reads the workspace before generating** and writes its deliverable back, per `skills/vital-playbook/references/workspace.md`.

**Evals** (`skills/<name>/evals/evals.json`)

- Ids 1-3 are happy-path cases; **id 4 is adversarial** — a prompt where the correct behaviour is to push back, refuse, or state an uncomfortable truth. At least one of its assertions must fail if the model simply complies.
- Assertions test judgment anchored to that prompt's specifics, never the presence of a section. A skill scoring 1.00 with_skill has no headroom and needs harder assertions. Full guidance: `docs/evaluating-skills.md`.

**MCP servers**

- Vital ships **none**, deliberately. Installing a go-to-market plugin should not add network endpoints to a user's session. Document connectors in `CONNECTORS.md` for the user to opt into instead.

**Manifest** (`.claude-plugin/plugin.json`)

- Valid JSON; `name` kebab-case; **`description` ≤ 500 characters**.

**Design**

- Design work uses the **impeccable** design-quality layer (see `skills/design-brief/references/impeccable.md`). Reference **impeccable only** — never `stardust`. The validator fails on any `stardust` string.

**Capital discipline**

- The `capital` agent and its skills (`incorporation`, `fundraising`, `bootstrapping`, `pitch-deck`) are **advisory only**. Every one must keep its boundary: Vital provides information/frameworks/benchmarks/drafts, **not legal, tax, financial, or investment advice**, and routes binding decisions to a qualified attorney/CPA. Do not remove these disclaimers.

## Add an agent

1. Create `agents/<name>.md` with frontmatter (`name`, `description`, `model: inherit`, a valid `color`, `skills` it owns, optional `tools`) and a system-prompt body.
2. Add it to the team table in `skills/vital-playbook/SKILL.md`, the roster in `agents/vital-lead.md`, and the README.
3. Run the validator.

## Add a skill

1. Create `skills/<name>/SKILL.md` with frontmatter (`name`, `description`, optional `allowed-tools`) and imperative instructions.
2. Wire it to its owning agent (mention it in that agent's file) and add it to the playbook table + README.
3. Run the validator.

## Validate and build locally

```bash
pip install pyyaml
python3 scripts/validate.py                    # repo rules — must pass before committing
claude plugin validate --strict plugins/vital  # official schema + directory checks

# Try it locally without installing:
claude --plugin-dir plugins/vital

# Build the installable .plugin (same as CI does on a tag) — the plugin folder only:
(cd plugins/vital && zip -r ../../vital.plugin . -x "*.DS_Store")
```

## Releasing

1. Bump `version` in **both** `plugins/vital/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (semver) — `scripts/validate.py` fails if they drift.
2. Commit, then tag: `git tag v0.8.0 && git push origin v0.8.0`.
3. The **Release** workflow validates, builds `vital.plugin`, and attaches it to a GitHub Release automatically.

## Commit style

Small, focused commits. Reference the version when bumping. CI (`Validate`) runs on every push and PR to `main`.
