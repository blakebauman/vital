# Installing Vital

Vital is a public repo — `github.com/blakebauman/vital`. It ships two kinds of content:

- **9 agents** (`agents/*.md`) — Claude Code subagents. Claude Code only.
- **3 commands** (`commands/*.md`) — `/vital:launch`, `/vital:status`, `/vital:readiness`. Claude Code only.
- **19 skills** (`skills/*/SKILL.md`) — the portable [Agent Skills](https://code.claude.com/docs/en/skills) format, which Cursor, Codex CLI, Gemini CLI and others also read.

Pick the section for your tool.

---

## Claude Code — plugin (recommended)

Installs the agents and skills in one step, and keeps them updatable. Vital ships no MCP servers — connectors are opt-in, see [`CONNECTORS.md`](../CONNECTORS.md).

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
cp -R agents/* ~/.claude/agents/
cp -R skills/* ~/.claude/skills/

# or project scope — this repo only
mkdir -p .claude/agents .claude/skills
cp -R /path/to/vital/agents/* .claude/agents/
cp -R /path/to/vital/skills/* .claude/skills/
```

Connectors are configured separately either way — see [`CONNECTORS.md`](../CONNECTORS.md).

---

## Claude.ai and Claude Desktop

Skills only — subagents are a Claude Code concept and won't load here.

Zip an individual skill folder and upload it under **Settings → Capabilities → Skills**:

```bash
cd skills && zip -r press-kit.zip press-kit
```

Repeat per skill you want. Start with `vital-playbook`, then add the disciplines you actually use.

---

## Cursor

Cursor reads the same `SKILL.md` format, but skills are **project-scoped only** — there is no global skills directory.

```bash
mkdir -p .cursor/skills
cp -R /path/to/vital/skills/* .cursor/skills/
```

Skills then activate on their own when a request matches, and appear in the slash-command menu. The `agents/` files are not used by Cursor.

---

## Codex CLI

Skills are behind a feature flag:

```bash
codex --enable skills

# personal — all projects
mkdir -p ~/.codex/skills && cp -R /path/to/vital/skills/* ~/.codex/skills/

# or project-local
mkdir -p .codex/skills && cp -R /path/to/vital/skills/* .codex/skills/
```

Invoke a skill in chat with `@`, e.g. `@press-kit`.

---

## Gemini CLI

No flag needed — skills are discovered at session start.

```bash
# user scope
mkdir -p ~/.gemini/skills && cp -R /path/to/vital/skills/* ~/.gemini/skills/

# or workspace scope
mkdir -p .gemini/skills && cp -R /path/to/vital/skills/* .gemini/skills/
```

Manage them with `/skills enable` and `/skills disable` (add `--scope workspace` for the project copy).

---

## Other agents (opencode, Windsurf, Aider, …)

The pattern is identical everywhere: drop the contents of `skills/` into whatever directory your tool reads skills from. `SKILL.md` frontmatter is the shared standard; nothing in Vital's skills is Claude-specific.

To keep one clone serving several tools, symlink instead of copying:

```bash
git clone https://github.com/blakebauman/vital.git ~/src/vital
ln -s ~/src/vital/skills ~/.codex/skills     # adapt the target path per tool
```

Then `git pull` in `~/src/vital` updates every tool at once.

---

## What travels, and what doesn't

- **Agents don't travel.** `agents/*.md` are Claude Code subagent definitions (`color`, `model: inherit`, `tools`). Only Claude Code loads them.
- **Outside Claude Code you get the skills.** That's most of the value, but the `vital-lead` orchestration becomes manual: invoke `vital-playbook` yourself and name the discipline you want rather than letting the lead sequence specialists for you.
- **`allowed-tools` pre-approvals are Claude Code-specific.** Elsewhere the research and production skills will still work, they'll just ask for permission the way that tool normally does.
- **MCP connectors are per-tool and opt-in.** Vital installs no MCP servers of its own; Slack, Google Workspace, and anything else are configured in your own settings. See [`CONNECTORS.md`](../CONNECTORS.md).
