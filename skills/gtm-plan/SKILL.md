---
name: gtm-plan
description: >
  Use this skill to build a go-to-market plan for a product. Triggers include
  "go-to-market plan", "GTM strategy", "how do I reach customers", "which
  channels should I use", "pricing and packaging", "launch strategy", or
  turning positioning into a concrete plan to acquire and convert customers.
metadata:
  version: "0.1.0"
---

Turn positioning into a concrete, sequenced plan to reach, convert, and retain customers. Require positioning and ICP first — if they are missing, run the `positioning` skill before proceeding. Work through the sections in order.

Anchor the whole plan to the **client's segment** (enterprise / mid-market / small business) — it drives motion, pricing, cycle length, and launch shape. See `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Broadly: enterprise → sales-led/ABM with pilots, procurement, security review, annual contracts; mid-market → hybrid self-serve + sales-assist, land-and-expand; small business → product-led, self-serve, transparent monthly pricing.

## 1. Motion

Choose the dominant go-to-market motion and justify it from the price point, buyer, product complexity, **and the client's segment**:

- **Product-led** — user self-serves and activates; low price, low friction, fast time-to-value.
- **Sales-led** — a person sells; higher price, complex buyer, longer cycle.
- **Community-led** — audience and word-of-mouth drive acquisition.
- **Hybrid** — a deliberate combination, with the primary motion named.

The motion constrains channels, pricing, content, and team. Pick it first.

## 2. Channels

List candidate acquisition channels, then rank by fit to the ICP and speed to signal. Recommend testing one or two first — where the ICP already is, and where you can learn fastest. For each recommended channel: the hypothesis, the first test, and the signal that means it is working.

## 3. Pricing & packaging

Recommend the model (usage, seat, tier, flat), the value metric to price against (the unit the customer already thinks in), starting price points, the tier structure, and the free/trial strategy. Give a defensible starting point and a plan to iterate — not a permanent answer. Anchor to willingness-to-pay and competitor pricing from the teardown, not cost-plus.

## 4. Funnel

Map the path from first touch to activated, paying, retained customer. Name each stage, the key conversion point, and what must be true to move to the next. Identify the one or two stages most likely to leak.

## 5. Launch sequence

Sequence the rollout in phases (e.g., private beta → design partners → public launch → scale). For each phase: the goal, who is in it, what it must prove, and the go/no-go signal to advance.

## 6. First 90 days

Translate the plan into a concrete 90-day action list: what to do, in what order, and the metric each action moves.

## Output

Deliver: chosen motion with rationale, ranked channels with first tests, pricing and packaging, the funnel with leak points, the phased launch sequence, and a 90-day action list. Everything should be actionable this quarter. For the launch phase specifically, hand off to the `launch-plan` skill. Save the plan to the project.
