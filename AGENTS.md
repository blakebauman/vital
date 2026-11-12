# AGENTS.md

Guidance for AI coding agents (Claude Code, etc.) working in this repository.

This repo is the **Vital** plugin marketplace. The plugin itself — everything users install — lives in `plugins/vital/`; the repo root holds only the marketplace, tooling, and contributor docs. Paths below are relative to `plugins/vital/` unless they start at the repo root. When editing it, follow `CONTRIBUTING.md` in full. The critical invariants (enforced by `scripts/validate.py` and CI) are:

- **Agent names**: 3–50 chars, kebab-case, unique. Never a 2-char name.
- **Agent colors**: only `red, blue, green, yellow, purple, orange, pink, cyan`. Never `magenta`. Repeats allowed.
- **Plugin folder holds only what ships.** Never put `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `scripts/`, or CI files inside `plugins/vital/` (the validator rejects it).
- **Manifest description**: `plugins/vital/.claude-plugin/plugin.json` `description` must be ≤ 500 characters.
- **Manifest version**: bump it in **both** `plugins/vital/.claude-plugin/plugin.json` and the root `.claude-plugin/marketplace.json` — the validator fails if they disagree.
- **Skills**: each `skills/<name>/` needs a `SKILL.md` whose frontmatter `name` matches the directory name, plus a `description`. Any `allowed-tools` must name real tools.
- **Reference paths**: every `references/*.md` path written in an agent or skill body must be `${CLAUDE_PLUGIN_ROOT}/skills/<skill>/references/<file>`. A bare `references/foo.md` resolves against the *user's* cwd once installed and silently fails to load — the validator rejects it and checks the file exists.
- **Descriptions**: agent and skill descriptions are loaded into every session. Keep them under 1024 chars (the validator enforces it) and as short as still triggers reliably.
- **Host capabilities**: skills may reference `pptx`, `xlsx`, `dataviz`, or `my-writing-style`, but only with a stated fallback for when that skill is absent — Vital must degrade, never silently drop a deliverable. Declare any new external skill in `EXTERNAL_SKILLS` in `scripts/validate.py`.
- **Agent skills**: each agent lists the skills it owns under `skills:` (preloaded at start). A skill has one owning agent; the owner changes only with the team table.
- **Hooks**: `hooks/hooks.json` holds only local, read-only, silent-when-irrelevant hooks; scripts live in `hooks/` and use no environment variables other than `${CLAUDE_PLUGIN_ROOT}` (the directory holds anything else for review).
- **Name is permanent.** `name: vital` never changes (installs are keyed on it); change `displayName` for the label.
- **No bundled MCP servers.** Vital ships none by design; installing a go-to-market plugin must not add network endpoints. Connectors are documented in `CONNECTORS.md` for the user to opt into.
- **Evals**: each skill's `evals/evals.json` carries ids 1-3 (happy path) and id 4 (adversarial — the correct answer is to push back or refuse). Assertions test judgment anchored to the prompt's specifics, never section presence. See `docs/evaluating-skills.md`.
- **Design**: reference the **impeccable** design system only — never `stardust` (the validator fails on it).
- **Capital discipline** (`capital` agent; `incorporation`, `fundraising`, `bootstrapping`, `pitch-deck` skills): advisory only. Keep the "not legal/tax/financial/investment advice; consult a qualified attorney/CPA" boundary in every one.

Before committing, always run:

```bash
pip install pyyaml && python3 scripts/validate.py
claude plugin validate --strict plugins/vital   # official schema + directory checks
```

Keep `<example>` blocks in agent **bodies**, not frontmatter, so YAML stays valid. Keep `SKILL.md` files lean and put long material in `references/`. When you add or rename an agent or skill, update the team table in `skills/vital-playbook/SKILL.md`, the roster in `agents/vital-lead.md`, and `README.md` to match.

The plugin's entry points (`/vital:launch`, `/vital:status`, `/vital:readiness`) are user-invoked skills — `skills/launch`, `skills/status`, `skills/readiness` with `disable-model-invocation: true` — not `commands/` (legacy; don't reintroduce it). Deliverables land in the client's `.vital/` workspace under the protocol in `skills/vital-playbook/references/workspace.md` — read before generating, write back, update `.vital/INDEX.md`.
