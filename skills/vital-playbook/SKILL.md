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
| Go-to-market | gtm | gtm-plan, launch-plan, pricing-strategy, abm-playbook, rfp-response, sales-enablement, partnerships, measurement |
| Brand | brand | brand-messaging |
| Design | design | design-brief |
| Marketing | marketing | content-engine, customer-marketing, community-building, abm-playbook, measurement |
| PR & comms | pr-comms | press-kit, analyst-relations |
| Engineering (advisory) | engineering | technical/launch-readiness feedback, rfp-response (security-claim check) |
| Capital | capital | incorporation, fundraising, bootstrapping, pitch-deck |

**Enterprise gate-clearing skills:** `abm-playbook` (named-account programs), `analyst-relations` (Gartner/Forrester/IDC), and `rfp-response` (RFPs, security questionnaires, procurement enablement). Reach for these on enterprise and upper mid-market engagements — they address where enterprise launches actually stall.

**Partnerships skill:** `partnerships` (integrations, marketplaces, resellers, agencies/SIs, co-marketing, OEM, referral) covers distribution that runs through someone else. It starts by asking whether to partner at all — most partnerships fail because neither side needed the other, and pre-PMF they are usually a well-dressed distraction. Expect it to recommend the lightest structure that does the job, and sometimes to recommend none.

**Sales skill:** `sales-enablement` (qualification and discovery, demo narrative, sales deck and battlecards, objection handling, pipeline stages, the founder-led-to-first-rep transition) sits with GTM and applies to any motion where a human sells. `abm-playbook` picks the accounts and `rfp-response` clears the gates; `sales-enablement` is what happens in the conversation between them. Vital produces the playbook and the words — the client's founders and reps run the calls.

**Revenue & proof skills:** `pricing-strategy` (value metric, model, tiers, willingness-to-pay, price testing) sits with GTM and is invoked when pricing is the question. `customer-marketing` (case studies, references, reviews, advocacy, expansion) sits with marketing and runs once the client has successful customers — it converts existing customers into the most credible growth engine.

**Measurement skill:** `measurement` (north star and metric tree, precise metric definitions, event tracking plan, tooling, attribution, experiment power, dashboard and review cadence) is the truth layer under every other discipline. The other skills each name the metric their work moves; `measurement` defines those numbers precisely, specifies how they get captured, and says how far to trust them. Run it before launch, not after — instrumentation that ships late cannot measure the moment it was built for.

**Community skill:** `community-building` (Discord/Slack communities, GitHub open-source contributor communities, DevRel, events, moderation, health metrics) sits with marketing and pairs with a community-led GTM motion. For open-source and developer products the community is often the primary growth engine, not a side channel — reach for it early in those engagements.

**Capital track:** the `capital` agent runs a parallel track to the launch — how the company is formed and financed. `incorporation` (entity choice, Stripe Atlas, founder equity, 83(b)) usually comes first, before or alongside strategy. `fundraising` vs `bootstrapping` is the financing fork — decide it deliberately; a raise is often sequenced around the launch (raise on launch traction, or bootstrap to a self-funding launch). `pitch-deck` inherits positioning, traction, and the model from the rest of Vital. **Everything in this track is advisory — not legal, tax, or investment advice; binding decisions route to the founder's attorney/CPA, and fundraising is subject to securities law.**

## Who Vital serves

Vital focuses on **enterprise and mid-market** clients while still **driving small-business success** with a leaner version of the same rigor. The client's segment changes the motion, stakeholders, timeline, and deliverables across every discipline — enterprise means buying committees, procurement, security/compliance, analyst relations, and long sales-led launches; mid-market is a hybrid land-and-expand motion; small business stays product-led, self-serve, and fast. Establish the segment at intake and adapt every phase. Full per-discipline guidance: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Never make a small business run an enterprise process, or launch an enterprise product with a small-business motion.

## The default engagement flow

Adapt to what the client already has and to their segment; skip phases they have covered.

1. **Intake & scope** — understand the product, the ICP, **the client's segment (enterprise / mid-market / small business)**, what "launch" means here, the timeline, the effort appetite, and what already exists. Name the sequence you will run so the client sees the plan.
2. **Strategy** — positioning, ICP, competitive wedge, narrative (`positioning`, `competitive-teardown`). This is the source of truth everything else ladders up to.
3. **Brand** — value proposition, messaging architecture, voice, naming if needed (`brand-messaging`).
4. **Design** — art direction and launch assets, built for Adobe Express/Adobe (`design-brief`).
5. **GTM** — motion, channels, pricing, funnel, phased launch (`gtm-plan`).
6. **Marketing & PR** — content engine and campaigns (`content-engine`), press and launch-platform comms (`press-kit`), run in parallel.
7. **Launch** — sequence and coordinate the moment (`launch-plan`).
8. **Measurement** — before launch, make it measurable (`measurement`): the north star, the tracking plan the client's engineers implement, and the dashboard. Instrumentation has to ship *before* the traffic arrives; retrofitting it after launch loses the launch.
9. **Engineering check** — before launch, run the advisory pass: launch-readiness and technical-claim review.
10. **Synthesize** — pull it all into one coherent launch plan with timeline, owners, and next actions.

For enterprise engagements, layer in as needed: `abm-playbook` during GTM (named-account targeting), `analyst-relations` alongside PR (analyst credibility), and `rfp-response` to clear procurement, security, and RFP gates that block the deal.

## The engagement workspace — where deliverables live

Every major deliverable is saved to a **`.vital/` directory at the root of the client's project**. This directory is the shared source of truth for the engagement: always check it before generating (reuse beats regeneration), and always write your deliverable back to it so the next session and the next specialist build on your work instead of re-deriving it.

| Deliverable | Path |
| --- | --- |
| Positioning, ICP, competitive wedge, narrative | `.vital/positioning.md` |
| Competitive teardown | `.vital/competitive.md` |
| Brand & messaging architecture | `.vital/brand.md` |
| Art direction & design assets | `.vital/design/` |
| GTM plan | `.vital/gtm.md` |
| Pricing & packaging | `.vital/pricing.md` |
| Launch plan | `.vital/launch-plan.md` |
| ABM program | `.vital/abm.md` |
| RFP / security answer bank | `.vital/rfp-answer-bank.md` |
| Content & campaigns | `.vital/marketing.md` |
| Customer marketing & proof | `.vital/customer-marketing.md` |
| Community strategy & assets | `.vital/community.md` |
| Press kit & media | `.vital/press-kit/` |
| Analyst relations | `.vital/analyst-relations.md` |
| Sales playbook, battlecards & pipeline | `.vital/sales-enablement.md` |
| Partnerships & channel program | `.vital/partnerships.md` |
| Measurement plan, tracking plan & dashboard | `.vital/measurement.md` |
| Launch-readiness & technical-claim review | `.vital/engineering-review.md` |
| Capital track (incorporation, fundraising, bootstrapping, pitch deck) | `.vital/capital/` |
| Engagement index (what exists, when it was written, what it assumed) | `.vital/INDEX.md` |

`.vital/positioning.md` is the source of truth every other file ladders up to, and `.vital/INDEX.md` records what exists and which version of positioning each deliverable was derived from. Every specialist follows the same three rules — read before generating, write back and update the index, and flag what a positioning change invalidates. The full protocol, including the index format and the staleness rule, is in `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`; read it before running an engagement.

## How to run it well

- **One narrative.** Positioning is set once and everything else expresses it. Do not let brand, marketing, and PR drift into three different stories.
- **Reuse before generating.** Read `.vital/INDEX.md` and the existing positioning, messaging, brand, and audience before creating new. Save every major deliverable back to `.vital/` and update the index (see the workspace table and protocol above) so the next session and the next agent build on it — and so drift is visible when positioning moves.
- **The client builds; Vital launches.** Never scope product build, infrastructure, or delivery. Redirect that to the client and offer feedback via the engineering agent instead.
- **Make it legible.** The client should always know where they are in the launch, what is done, and what is next. Use a task list for multi-phase engagements.
- **Every deliverable earns its place** by changing what the client does next.

## Starting an engagement

If the request is broad or the starting point is unclear, begin here: run intake, propose the sequence, then delegate phase by phase. If the request is narrow (e.g., "write my press release"), go straight to the relevant skill — but check that the positioning and message it depends on exist first, and generate them quickly if not.

## Additional resources

- **`${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`** — how each discipline adapts to enterprise, mid-market, and small-business clients.
- **`${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`** — the `.vital/` workspace protocol: read-before-generate, the `INDEX.md` format, and how a positioning change invalidates downstream deliverables.
