# AGENTS.md

Guidance for AI coding agents (Claude Code, etc.) working in this repository.

This repo is the **Vital** plugin — agents and skills for an AI go-to-market agency. When editing it, follow `CONTRIBUTING.md` in full. The critical invariants (enforced by `scripts/validate.py` and CI) are:

- **Agent names**: 3–50 chars, kebab-case, unique. Never a 2-char name.
- **Agent colors**: only `red, blue, green, yellow, purple, orange, pink, cyan`. Never `magenta`. Repeats allowed.
- **Manifest description**: `.claude-plugin/plugin.json` `description` must be ≤ 500 characters.
- **Manifest version**: bump it in **both** `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` — the validator fails if they disagree.
- **Skills**: each `skills/<name>/` needs a `SKILL.md` with `name` + `description` frontmatter.
- **Design**: reference the **impeccable** design system only — never `stardust` (the validator fails on it).
- **Capital discipline** (`capital` agent; `incorporation`, `fundraising`, `bootstrapping`, `pitch-deck` skills): advisory only. Keep the "not legal/tax/financial/investment advice; consult a qualified attorney/CPA" boundary in every one.

Before committing, always run:

```bash
pip install pyyaml && python3 scripts/validate.py
```

Keep `<example>` blocks in agent **bodies**, not frontmatter, so YAML stays valid. Keep `SKILL.md` files lean and put long material in `references/`. When you add or rename an agent or skill, update the team table in `skills/vital-playbook/SKILL.md`, the roster in `agents/vital-lead.md`, and `README.md` to match.
