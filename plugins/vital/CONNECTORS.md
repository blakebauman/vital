# Connectors

Vital's agents and skills work with files and the web out of the box. Connecting the tools below lets them do more — send outreach, schedule, produce assets, and post updates — without leaving your session.

## Recommended connectors

| Purpose | Tool | How Vital uses it |
| --- | --- | --- |
| Email & outreach | Gmail (Google Workspace) | Draft and send journalist pitches, partner outreach, and launch emails. |
| Scheduling | Google Calendar | Book launch milestones, embargo dates, and design-partner calls. |
| Docs & storage | Google Drive / Docs | Store and share positioning, plans, and press materials. |
| Team chat | Slack (opt-in, see below) | Post launch updates, plans, and reports to a channel. |
| Design production | Adobe Express + Adobe suite | Build on-brand launch assets from the design briefs. |

## Notes

- **Google Workspace** (Gmail, Calendar, Drive) connects through your Claude connector settings. Once enabled in this workspace, Vital's agents use it automatically.
- **Chat**: Vital deliberately ships **no MCP servers** — installing a go-to-market plugin should not add network endpoints to your session. To wire up Slack yourself, add this to your own `.mcp.json` or project settings:

  ```json
  { "mcpServers": { "slack": { "type": "http", "url": "https://slack.mcp.claude.com/mcp" } } }
  ```

  If your team uses **Microsoft Teams** instead, point the same entry at your Teams MCP server.
- **Adobe**: Adobe Express and the Adobe apps are used by the `design` agent and `design-brief` skill. Vital produces build-ready specs and directions you execute in Express; no MCP connection is required.
- Nothing here is mandatory. Every skill degrades gracefully to working with files and the web when a connector is not present.
