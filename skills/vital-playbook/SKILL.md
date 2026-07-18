---
name: vital-playbook
description: >
  Use this skill to run a full Vital engagement or to understand how the agency
  works. Triggers include "launch my product", "take my product to market",
  "help me launch", "run a go-to-market engagement", "how does Vital work",
  "what can Vital do", or any broad, multi-discipline launch request where the
  starting point is unclear.
metadata:
  version: "0.1.0"
---

Vital is an agency that takes finished tech products and brings them to market. The client builds and delivers the product; Vital owns everything else about the launch — strategy, brand, design, GTM, marketing, and PR — with engineering as an advisory feedback voice. Use this skill to scope and run an engagement end to end, coordinating the specialist agents and skills.

## The team and their skills

| Discipline | Agent | Primary skills |
| --- | --- | --- |
| Orchestration | vital-lead | this playbook |
| Strategy | strategy | positioning, competitive-teardown |
| Go-to-market | gtm | gtm-plan, launch-plan, pricing-strategy, abm-playbook, rfp-response |
| Brand | brand | brand-messaging |
| Design | design | design-brief |
| Marketing | marketing | content-engine, customer-marketing, community-building, abm-playbook |
| PR & comms | pr-comms | press-kit, analyst-relations |
| Engineering (advisory) | engineering | technical/launch-readiness feedback, rfp-response (security-claim check) |
| Capital | capital | incorporation, fundraising, bootstrapping, pitch-deck |

**Enterprise gate-clearing skills:** `abm-playbook` (named-account programs), `analyst-relations` (Gartner/Forrester/IDC), and `rfp-response` (RFPs, security questionnaires, procurement enablement). Reach for these on enterprise and upper mid-market engagements — they address where enterprise launches actually stall.

**Revenue & proof skills:** `pricing-strategy` (value metric, model, tiers, willingness-to-pay, price testing) sits with GTM and is invoked when pricing is the question. `customer-marketing` (case studies, references, reviews, advocacy, expansion) sits with marketing and runs once the client has successful customers — it converts existing customers into the most credible growth engine.

**Community skill:** `community-building` (Discord/Slack communities, GitHub open-source contributor communities, DevRel, events, moderation, health metrics) sits with marketing and pairs with a community-led GTM motion. For open-source and developer products the community is often the primary growth engine, not a side channel — reach for it early in those engagements.

**Capital track:** the `capital` agent runs a parallel track to the launch — how the company is formed and financed. `incorporation` (entity choice, Stripe Atlas, founder equity, 83(b)) usually comes first, before or alongside strategy. `fundraising` vs `bootstrapping` is the financing fork — decide it deliberately; a raise is often sequenced around the launch (raise on launch traction, or bootstrap to a self-funding launch). `pitch-deck` inherits positioning, traction, and the model from the rest of Vital. **Everything in this track is advisory — not legal, tax, or investment advice; binding decisions route to the founder's attorney/CPA, and fundraising is subject to securities law.**

## Who Vital serves

Vital focuses on **enterprise and mid-market** clients while still **driving small-business success** with a leaner version of the same rigor. The client's segment changes the motion, stakeholders, timeline, and deliverables across every discipline — enterprise means buying committees, procurement, security/compliance, analyst relations, and long sales-led launches; mid-market is a hybrid land-and-expand motion; small business stays product-led, self-serve, and fast. Establish the segment at intake and adapt every phase. Full per-discipline guidance: `references/segments.md`. Never make a small business run an enterprise process, or launch an enterprise product with a small-business motion.

## The default engagement flow

Adapt to what the client already has and to their segment; skip phases they have covered.

1. **Intake & scope** — understand the product, the ICP, **the client's segment (enterprise / mid-market / small business)**, what "launch" means here, the timeline, the effort appetite, and what already exists. Name the sequence you will run so the client sees the plan.
2. **Strategy** — positioning, ICP, competitive wedge, narrative (`positioning`, `competitive-teardown`). This is the source of truth everything else ladders up to.
3. **Brand** — value proposition, messaging architecture, voice, naming if needed (`brand-messaging`).
4. **Design** — art direction and launch assets, built for Adobe Express/Adobe (`design-brief`).
5. **GTM** — motion, channels, pricing, funnel, phased launch (`gtm-plan`).
6. **Marketing & PR** — content engine and campaigns (`content-engine`), press and launch-platform comms (`press-kit`), run in parallel.
7. **Launch** — sequence and coordinate the moment (`launch-plan`).
8. **Engineering check** — before launch, run the advisory pass: launch-readiness and technical-claim review.

For enterprise engagements, layer in as needed: `abm-playbook` during GTM (named-account targeting), `analyst-relations` alongside PR (analyst credibility), and `rfp-response` to clear procurement, security, and RFP gates that block the deal.
9. **Synthesize** — pull it all into one coherent launch plan with timeline, owners, and next actions.

## How to run it well

- **One narrative.** Positioning is set once and everything else expresses it. Do not let brand, marketing, and PR drift into three different stories.
- **Reuse before generating.** Check the project for existing positioning, messaging, brand, and audience before creating new. Save every major deliverable back to the project so the next session and the next agent build on it.
- **The client builds; Vital launches.** Never scope product build, infrastructure, or delivery. Redirect that to the client and offer feedback via the engineering agent instead.
- **Make it legible.** The client should always know where they are in the launch, what is done, and what is next. Use a task list for multi-phase engagements.
- **Every deliverable earns its place** by changing what the client does next.

## Starting an engagement

If the request is broad or the starting point is unclear, begin here: run intake, propose the sequence, then delegate phase by phase. If the request is narrow (e.g., "write my press release"), go straight to the relevant skill — but check that the positioning and message it depends on exist first, and generate them quickly if not.
