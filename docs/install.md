# Installing Vital

Vital is a public repo — `github.com/blakebauman/vital`. It ships two kinds of content:

- **13 agents** (`plugins/vital/agents/*.md`) — subagents. Claude Code and Cowork (not claude.ai chat).
- **1 hook** (`plugins/vital/hooks/hooks.json`) — a `SessionStart` hook that surfaces `.vital/INDEX.md` when a workspace exists. Claude Code and Cowork.
- **25 skills** (`plugins/vital/skills/*/SKILL.md`) — the portable [Agent Skills](https://agentskills.io/specification) format, which Cursor, Codex CLI, Gemini CLI and others also read. Three are user-invoked entry points — `/vital:launch`, `/vital:status`, `/vital:readiness` — that never trigger on their own (`disable-model-invocation`).

Pick the section for your tool.

---

## Claude Code — plugin (recommended)

Installs the agents and skills in one step, and keeps them updatable. Vital ships no MCP servers — connectors are opt-in, see [`CONNECTORS.md`](../plugins/vital/CONNECTORS.md).

```
/plugin marketplace add blakebauman/vital
/plugin install vital@vital
```

Same thing from a shell, without opening a session:

```bash
claude plugin marketplace add blakebauman/vital
claude plugin install vital@vital
```

**Update** to the latest published version:

```
/plugin marketplace update vital
```

then `/reload-plugins` (or restart the session).

**Remove:**

```
/plugin uninstall vital@vital
/plugin marketplace remove vital
```

The marketplace and the plugin are both named `vital`, which is why the install ref is `vital@vital`.

### Pinning Vital for a whole team or project

Commit this to the project's `.claude/settings.json`. Anyone who trusts the project gets the marketplace registered and the plugin enabled automatically.

```json
{
  "extraKnownMarketplaces": {
    "vital": {
      "source": { "source": "github", "repo": "blakebauman/vital" }
    }
  },
  "enabledPlugins": {
    "vital@vital": true
  }
}
```

Use `~/.claude/settings.json` instead if you want it everywhere rather than per project.

---

## Claude Code — manual copy (no plugin system)

If you'd rather vendor the files, or want to edit them in place:

```bash
git clone https://github.com/blakebauman/vital.git
cd vital

# user scope — available in every project
mkdir -p ~/.claude/agents ~/.claude/skills
cp -R plugins/vital/agents/* ~/.claude/agents/
cp -R plugins/vital/skills/* ~/.claude/skills/

# or project scope — this repo only
mkdir -p .claude/agents .claude/skills
cp -R /path/to/vital/plugins/vital/agents/* .claude/agents/
cp -R /path/to/vital/plugins/vital/skills/* .claude/skills/
```

Connectors are configured separately either way — see [`CONNECTORS.md`](../plugins/vital/CONNECTORS.md).

---

## Claude.ai, the desktop app, and Cowork

Vital installs as a whole plugin, saved to your account, so it also appears in Cowork and syncs to Claude Code (as `vital@synced`).

1. Open **Customize → Plugins** in claude.ai or the desktop app.
2. **Add → Add marketplace**, enter `blakebauman/vital`, then add **Vital GTM Agency**. To pick up new releases, select **Check for updates** or turn on **Sync automatically**.
3. Or **Add → Upload plugin** with the `vital.plugin` file attached to each [GitHub release](https://github.com/blakebauman/vital/releases).

What loads where: **Cowork** loads skills, entry points, agents, and the hook. **claude.ai chat** loads skills and entry points only — the specialists become manual (start from `vital-playbook`), and `/vital:launch` and `/vital:readiness` run inline.

**Team and Enterprise:** an Owner can sync this repository for the whole organization and set Vital to *Available*, *Installed by default*, or *Required* — see [Manage plugins for your organization](https://claude.com/docs/plugins/admin).

---

## Cursor

Cursor reads the same `SKILL.md` format, but skills are **project-scoped only** — there is no global skills directory.

```bash
mkdir -p .cursor/skills
cp -R /path/to/vital/plugins/vital/skills/* .cursor/skills/
```

Skills then activate on their own when a request matches, and appear in the slash-command menu. The `agents/` files are not used by Cursor.

---

## Codex CLI

Skills are behind a feature flag:

```bash
codex --enable skills

# personal — all projects
mkdir -p ~/.codex/skills && cp -R /path/to/vital/plugins/vital/skills/* ~/.codex/skills/

# or project-local
mkdir -p .codex/skills && cp -R /path/to/vital/plugins/vital/skills/* .codex/skills/
```

Invoke a skill in chat with `@`, e.g. `@press-kit`.

---

## Gemini CLI

No flag needed — skills are discovered at session start.

```bash
# user scope
mkdir -p ~/.gemini/skills && cp -R /path/to/vital/plugins/vital/skills/* ~/.gemini/skills/

# or workspace scope
mkdir -p .gemini/skills && cp -R /path/to/vital/plugins/vital/skills/* .gemini/skills/
```

Manage them with `/skills enable` and `/skills disable` (add `--scope workspace` for the project copy).

---

## Other agents (opencode, Windsurf, Aider, …)

The pattern is identical everywhere: drop the contents of `skills/` into whatever directory your tool reads skills from. `SKILL.md` frontmatter is the shared standard; nothing in Vital's skills is Claude-specific.

To keep one clone serving several tools, symlink instead of copying:

```bash
git clone https://github.com/blakebauman/vital.git ~/src/vital
ln -s ~/src/vital/plugins/vital/skills ~/.codex/skills     # adapt the target path per tool
```

Then `git pull` in `~/src/vital` updates every tool at once.

---

## What travels, and what doesn't

- **Agents travel only to Claude Code and Cowork.** `plugins/vital/agents/*.md` are subagent definitions (`color`, `model: inherit`, `skills`, `tools`). claude.ai chat and non-Claude tools ignore them.
- **Outside Claude Code and Cowork you get the skills.** That's most of the value, but the `vital-lead` orchestration becomes manual: invoke `vital-playbook` yourself and name the discipline you want rather than letting the lead sequence specialists for you.
- **The entry-point skills degrade, not break.** `launch` and `readiness` run through the `vital-lead` and `engineering` agents when they exist, and inline under the same rules when they don't. In hosts that ignore `disable-model-invocation`, invoke them by name (`/launch`, `/status`, `/readiness`); the `/vital:` prefix is the Claude Code plugin namespace.
- **`allowed-tools` pre-approvals are Claude Code-specific.** Elsewhere the research and production skills will still work, they'll just ask for permission the way that tool normally does.
- **MCP connectors are per-tool and opt-in.** Vital installs no MCP servers of its own; Slack, Google Workspace, and anything else are configured in your own settings. See [`CONNECTORS.md`](../plugins/vital/CONNECTORS.md).
