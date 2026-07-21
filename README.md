# Vital

**An AI agency that takes the tech products you build and brings them to market.**

You build and deliver the product. Vital owns everything else about the launch — strategy, brand, design, go-to-market, marketing, and PR — with an engineering advisor as a technical feedback voice. It's a team of specialist agents coordinated by a lead, plus skills for each core workflow from positioning through press.

**Who Vital serves:** primarily **enterprise and mid-market** clients, while still **driving small-business success** with a leaner version of the same rigor. The client's segment reshapes the whole launch — enterprise means buying committees, procurement, security/compliance, analyst relations, and phased sales-led launches; mid-market is a hybrid land-and-expand motion; small business stays product-led, self-serve, and fast. The per-discipline playbook lives in `skills/vital-playbook/references/segments.md`, and every relevant skill adapts to it.

## Install

In Claude Code:

```
/plugin marketplace add blakebauman/vital
/plugin install vital@vital
```

Prefer to vendor the files, or using a different agent? The 20 skills are the portable `SKILL.md` format and work in Cursor, Codex CLI, Gemini CLI and others — copy `skills/*` into that tool's skills directory. Full per-tool instructions, team-wide pinning, and what does and doesn't travel: **[docs/install.md](docs/install.md)**.

## The team

| Agent | Role |
| --- | --- |
| `vital-lead` | Managing partner. Scopes the engagement, sequences the specialists, and synthesizes everything into one launch plan. Start here when in doubt. |
| `strategy` | Positioning, ICP, competitive analysis, product-market-fit framing, the core narrative. |
| `gtm` | Go-to-market motion, channels, pricing and packaging, funnel, launch sequencing. |
| `brand` | Naming, messaging architecture, voice and tone. |
| `design` | Art direction and launch creative, built for Adobe Express and the Adobe suite. |
| `marketing` | Content engine, campaigns, SEO, email, social, growth loops. |
| `pr-comms` | Press strategy, releases, media lists, pitches, launch-platform comms. |
| `engineering` | Advisory only — launch-readiness feedback and a credibility check on technical claims. Does not build or ship. |
| `capital` | Incorporation (Stripe Atlas), raise-vs-bootstrap, running a fundraise, and the pitch deck. Advisory only — not legal/financial advice. |

## The skills

| Skill | What it does |
| --- | --- |
| `vital-playbook` | Runs a full engagement end to end; explains how the agency works. |
| `positioning` | Positioning statement, ICP, PMF framing, narrative. |
| `competitive-teardown` | Structured competitive analysis and the wedge to own. |
| `gtm-plan` | Full go-to-market plan: motion, channels, pricing, funnel, 90-day actions. |
| `launch-plan` | Launch timeline, asset checklist, channel plan, contingencies. |
| `brand-messaging` | Value proposition, messaging hierarchy, voice, naming. |
| `design-brief` | Art direction and build-ready creative specs for Adobe Express. |
| `content-engine` | Content strategy, calendar, campaigns, SEO, email, growth loops. |
| `press-kit` | Angle, media list, press release, pitches, launch-platform copy. |
| `abm-playbook` | *(Enterprise)* Named-account targeting, buying-committee maps, orchestrated plays. |
| `analyst-relations` | *(Enterprise)* Gartner/Forrester/IDC briefings, narrative, ranked-report prep. |
| `rfp-response` | *(Enterprise)* RFPs, security questionnaires (SOC 2/SSO), procurement enablement. |
| `pricing-strategy` | Value metric, model, tiers/packaging, willingness-to-pay, price points, and a test plan. |
| `customer-marketing` | Case studies, testimonials, references, reviews (G2/Capterra), advocacy, and expansion. |
| `community-building` | Discord/Slack + open-source (GitHub) communities, DevRel, events, moderation, health metrics. |
| `measurement` | North star and metric tree, metric definitions, event tracking plan, tooling, attribution, experiment power, dashboard. |
| `incorporation` | *(Capital)* Entity choice, Delaware C-corp via Stripe Atlas, founder equity/vesting, 83(b), cap table. |
| `fundraising` | *(Capital)* Raise-vs-bootstrap, stage/amount, SAFEs, valuation/dilution, investor list, data room. |
| `bootstrapping` | *(Capital)* Default-alive, unit economics, customer-funded growth, non-dilutive funding. |
| `pitch-deck` | *(Capital)* Fundraising narrative and slide sequence; produced via design. |

## Commands

| Command | What it does |
| --- | --- |
| `/vital:launch [what you're launching]` | Scopes the engagement, sequences the specialists, and runs it end to end. |
| `/vital:status` | Read-only. Reports what Vital has produced, what has gone stale, and what is next. |
| `/vital:readiness` | Runs the pre-launch engineering pass: launch readiness plus a technical-claim review. |

## How to use it

Just describe what you need. Broad requests ("take my product to market", "help me launch") route to the lead, which scopes and runs the whole engagement. Narrow requests ("write my press release", "build a content calendar") go straight to the right skill.

Positioning is the source of truth — set once by strategy, everything else ladders up to it. Vital saves every major deliverable into a `.vital/` directory in your project and indexes it in `.vital/INDEX.md`, recording which version of the positioning each one assumed. Specialists read that index before generating, so each session builds on the last — and when positioning changes, Vital tells you which downstream deliverables it just invalidated instead of letting them quietly contradict each other.

## Built to Claude Code spec

Agents and skills use the documented [subagent](https://code.claude.com/docs/en/sub-agents) and [skill](https://code.claude.com/docs/en/skills) frontmatter. Each agent declares a valid `color` (blue, cyan, green, purple, pink, orange, yellow, red — one per specialist), a `model` (`inherit`, so the team runs at your session's model tier), and `tools` where access should be restricted (the engineering advisor is read-only + web). The research skills (`competitive-teardown`, `analyst-relations`, `press-kit`) pre-approve `WebSearch`/`WebFetch` via `allowed-tools`, and the production skills (`design-brief`) pre-approve `Read`/`Write`, so those turns don't stop for permission prompts.

## Setup

Installation lives in [docs/install.md](docs/install.md). Once Vital is installed:

- **Connectors** (optional but recommended): Google Workspace (Gmail, Calendar, Drive) via your Claude connector settings; Slack or Teams via your own MCP config. Vital ships no MCP servers of its own. See `CONNECTORS.md`.
- **Adobe**: The design work is built for Adobe Express and the Adobe suite — Vital hands you build-ready specs you execute there. No connection required.
- **Impeccable** (optional): Vital's design uses the [impeccable](https://github.com/pbakaus/impeccable) design-quality system (Apache-2.0) as its craft layer — direction dimensions and an anti-slop checklist applied to every asset. If you install the impeccable skill/plugin, Vital's design agent defers to its commands (`/impeccable init | shape | craft | critique | audit | polish`) and detector; if not, it applies the principles by hand. For a full existing-site redesign, hand off to impeccable directly. See `skills/design-brief/references/impeccable.md`.

## Extending Vital

This is v1. Adding a new agent (e.g., build, sales, partnerships) is a new file in `agents/`; a new workflow is a new folder in `skills/`. The lead and playbook are designed to absorb new specialists as the agency grows.

## What Vital does not do

Build, ship, or deliver the product. That's yours — Vital takes it from finished to launched.

The `capital` discipline (incorporation, fundraising, bootstrapping) is advisory only: Vital provides information, frameworks, benchmarks, and drafts — **not legal, tax, financial, or investment advice.** Binding decisions (entity, equity, securities, taxes) belong with a qualified startup attorney and CPA, and fundraising is subject to securities law.
