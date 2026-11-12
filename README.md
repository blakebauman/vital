# Vital

An AI go-to-market agency for Claude Code, Cowork, and claude.ai — a lead orchestrator and 12 specialist agents (strategy, GTM, sales, partnerships, brand, design, marketing, community, PR, analytics, engineering advisory, capital) with 25 skills from company formation through launch. You build the product; Vital takes it to market.

**The plugin and its full documentation live in [`plugins/vital/`](plugins/vital/README.md).**

## Install

```
/plugin marketplace add blakebauman/vital
/plugin install vital@vital
```

On claude.ai or in Cowork: **Customize → Plugins → Add → Add marketplace** → `blakebauman/vital`. Other agents (Cursor, Codex CLI, Gemini CLI) and manual installs: [docs/install.md](docs/install.md).

## Repository layout

```
.claude-plugin/marketplace.json   # the marketplace — lists plugins/vital
plugins/vital/                    # the plugin: everything users install
  .claude-plugin/plugin.json      #   manifest
  agents/  skills/  hooks/        #   components
  README.md  CONNECTORS.md        #   user-facing docs (README is the directory listing)
scripts/validate.py               # repo validator (runs in CI)
docs/                             # install and eval guides
CONTRIBUTING.md  AGENTS.md        # contributor rules — not shipped
```

Contributing: [CONTRIBUTING.md](CONTRIBUTING.md). License: [MIT](LICENSE).
