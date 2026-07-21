---
name: measurement
description: >
  Use this skill to make a launch measurable — the north-star and metric tree,
  funnel and lifecycle metric definitions, the event instrumentation and
  tracking plan, analytics tooling choice, attribution, experiment design and
  significance, the dashboard, and the review cadence. Triggers include "how do
  I know if this worked", "what should I track", "set up analytics",
  "instrumentation", "tracking plan", "event schema", "attribution", "north star
  metric", "KPI dashboard", "A/B test", "is this result significant", or
  "measure the launch".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Make the launch measurable. Every other Vital skill names the metric its work
moves; this skill is the layer that makes those numbers real, trustworthy, and
actually consulted. A plan with metrics nobody can compute is a plan with no
feedback loop.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

**Do not re-pick the metrics.** The funnel comes from `gtm-plan`, the launch goal
from `launch-plan`, program metrics from `content-engine`, account metrics from
`abm-playbook`, community health from `community-building`, price tests from
`pricing-strategy`. Pull those, then do the job those skills do not: define each
metric precisely, specify how it gets captured, and say how much to trust it.

Scale the apparatus to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Enterprise measures account and committee engagement, pipeline influence, and deal velocity over long cycles, and must satisfy procurement's own reporting; mid-market tracks land-and-expand and lifecycle conversion; small business tracks self-serve funnel conversion, activation speed, and churn, with far less tooling.

## 1. The metric tree

Pick **one north-star metric** — the number that best proxies delivered customer
value, not revenue and not a vanity count. Then decompose it:

- **Inputs** — the two to four levers that actually move the north star. These are
  what teams work on.
- **Guardrails** — what must not degrade while you push the north star (churn,
  refunds, support load, latency, unsubscribe rate). Every growth push has a
  failure mode; name it before it happens.

State plainly what is a vanity metric here — impressions, raw signups, GitHub
stars, follower count — and why it is not the north star. If the client has
already committed to a vanity target, say so and offer the replacement rather
than optimizing for it.

## 2. Metric definitions

For each metric in the tree and each funnel stage, write a definition precise
enough that two people compute the same number:

| Field | Example |
| --- | --- |
| Name | Activated account |
| Exact definition | Account with ≥1 project created **and** ≥3 members invited within 14 days of signup |
| Source | `project_created`, `member_invited` events |
| Window / grain | Rolling 14 days, per account, weekly cohort |
| Owner | Who is accountable for the number |

Ambiguous definitions ("active user") are how two dashboards disagree and
everyone stops trusting both. Nail the edge cases: trials, internal accounts,
churned-and-returned, multi-seat.

## 3. Instrumentation / tracking plan

Specify what gets captured, **before** anything is built:

- **Naming convention** — pick one and hold it (`object_action`, snake_case:
  `checkout_completed`, not `Completed Checkout`). Inconsistency here is
  unfixable later without a migration.
- **Event table** — for each event: name, when it fires, properties and their
  types, and which metric it feeds. Cut any event no metric needs.
- **Identity** — anonymous ID, user ID, account ID, and how they stitch at
  signup. Get this wrong and every funnel is wrong.
- **What not to track** — no PII in event properties, no free-text fields that
  will contain it.

Deliver the tracking plan as a spreadsheet via the `xlsx` skill when available,
and as a markdown table otherwise. The client's engineers implement it — Vital
specifies, and does not build.

## 4. Tooling

Recommend a stack sized to the client's stage and budget, not to what is
fashionable. Cover the layers — product analytics, web analytics, warehouse, BI,
session replay, attribution — and say which layers the client can skip for now.
Research current pricing and free tiers before quoting them; they change.

State the honest minimum: a pre-launch startup needs the tracking plan, one
product analytics tool, and one dashboard. Buying a warehouse and a BI seat
before there is traffic is a way to feel measured rather than be measured.

## 5. Attribution

Explain the models (last touch, first touch, linear, time decay, data-driven)
and pick one, with its bias stated. Then be honest about the ceiling:

- Attribution is **directional, not causal.** Cookie loss, dark social, iOS
  restrictions, and multi-device journeys mean the numbers under-credit exactly
  the channels that build brand.
- **Self-reported attribution** ("How did you hear about us?" on signup) is
  underrated and often more truthful than the tracked model. Recommend it.
- The trustworthy causal tools are **holdouts and geo tests**, not the dashboard.
  Say when the client is too small to run one.

Never let a launch be declared a success or failure on a single attribution
model's read.

## 6. Experiments and significance

When a test is proposed, check it can actually resolve before it runs: baseline
rate, minimum detectable effect worth acting on, sample needed, and how long that
takes at current traffic. If the answer is "eleven months", say so and recommend
a qualitative or sequential approach instead.

Guard against the standard failures: calling a winner at n=40, peeking daily and
stopping at the first significant reading, testing five variants and celebrating
the one that cleared p<0.05, and ignoring novelty effects in the first week.
Most early-stage launches should be making obvious changes, not running
underpowered tests.

## 7. Dashboard and cadence

Specify **one** dashboard: the north star, its inputs, the guardrails, and the
funnel — on a single screen. For each number, state the decision it drives; a
number nobody acts on comes off the dashboard.

Then set the review rhythm: what gets looked at weekly, what monthly, who is in
the room, and the trigger thresholds that demand action rather than discussion.
Include the launch-week view — what to watch hour by hour on launch day, from
`launch-plan`.

## 8. Privacy and consent

Tracking plans have legal weight. Cover consent (GDPR/ePrivacy, CCPA/CPRA),
cookie banners and consent mode, data residency, retention, and processor
agreements — and flag that a consent-gated setup will under-count, so the
baseline must account for it. Keep PII out of event properties by default.

> **Not legal advice.** Vital provides frameworks and information only. Privacy
> obligations vary by jurisdiction and by what data the client actually collects.
> Route the tracking plan and consent design past qualified counsel or a privacy
> professional before launch.

## Output

Deliver: the metric tree with the north star and its guardrails, precise metric
definitions, the event tracking plan, a stage-appropriate tooling recommendation
with cited pricing, the attribution model with its stated limits, an experiment
feasibility check where a test was proposed, the one-page dashboard spec, and the
review cadence. Name explicitly which numbers are trustworthy and which are
directional — a measurement plan that oversells its own precision is worse than
none. Include a Sources section for tooling and pricing research. Save the plan
to `.vital/measurement.md`.
