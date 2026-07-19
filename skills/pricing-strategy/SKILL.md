---
name: pricing-strategy
description: >
  Use this skill to design or refine product pricing and packaging. Triggers
  include "what should I charge", "pricing strategy", "how should I package
  this", "pricing tiers", "value metric", "willingness to pay", "should I
  offer a free plan", "raise prices", "discounting", or turning positioning and
  GTM motion into a defensible price and package structure.
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Design pricing and packaging that captures the value the product creates without choking adoption. Pricing is a positioning decision, not a spreadsheet exercise — the number tells the market what the product is. Require positioning, ICP, and GTM motion first; pull them from the project or run `positioning` and `gtm-plan`. Anchor everything to the client's segment — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`.

## 1. Value metric

Identify the value metric — the unit the customer pays for that scales with the value they get (seats, usage, records, transactions, outcomes). A good value metric aligns price with value received, is easy to understand, and grows with the account. This is the single most important pricing decision; get it right before anything else.

## 2. Model

Choose the pricing model and justify it from the value metric, motion, and segment:

- **Per-seat** — value scales with users; simple; can penalize adoption.
- **Usage-based** — value scales with consumption; aligns cost to value; less predictable for the buyer.
- **Tiered/flat** — bundled tiers at set prices; predictable; simple to buy.
- **Hybrid** — a platform fee plus usage, or seats plus a usage meter.

Note the trade-off each model imposes on predictability, expansion, and sales friction.

## 3. Willingness to pay

Estimate willingness to pay from the alternatives (what the customer pays today, including labor and status quo), the value created (time saved, revenue gained, risk reduced — quantify it), and competitor price points. Research competitor pricing with web search and cite it. Frame price as a fraction of the value delivered, not a markup on cost.

## 4. Packaging & tiers

Design the tier structure:

- **Good-better-best** — usually three tiers; each adds value for a distinct segment. Anchor with a higher tier so the middle looks reasonable.
- **Feature fences** — which capabilities gate which tier, chosen so buyers self-select up as they grow, not so core value is crippled.
- **Free / trial / freemium** — decide deliberately: free plan (acquisition + loops, PLG), free trial (time-boxed proof), reverse trial, or sales-led demo. Tie the choice to the motion and segment. Free is a customer-acquisition strategy with real cost — justify it.
- **Entry point** — the price and package that gets the first "yes" fast, especially for self-serve segments.

## 5. Price points

Recommend specific starting numbers and the psychology behind them: anchoring, the decoy/high tier, charm pricing where appropriate, annual-vs-monthly discount, and the "talk to sales" threshold for enterprise. Give a defensible starting point and explicitly frame it as a hypothesis to iterate, not a permanent answer — most first prices are too low.

## 6. Expansion & discounting

Define how revenue grows within an account (the expansion path built into packaging) and a disciplined discounting stance: default list price, where discounts are allowed (annual commit, multi-year, logo/reference value), and the floor. Undisciplined discounting destroys the price anchor — set the rules before the first negotiation.

## 7. Test & iterate plan

Recommend how to validate: qualitative willingness-to-pay conversations, Van Westendorp-style price sensitivity questions, A/B on the pricing page (for self-serve), win/loss on price objections, and a cadence for revisiting. Name the signals that say the price is too low (no one hesitates, everyone says yes) or too high (price is the top lost-deal reason).

## Segment notes

- **Enterprise**: quote/negotiated pricing, annual contracts, value-based ROI justification, procurement expects a list price to anchor from. Tie price to a business outcome.
- **Mid-market**: transparent tiers with a clear "contact sales" path for the top tier; land-and-expand packaging.
- **Small business**: transparent, self-serve, monthly option, low entry price, minimize decision friction; churn sensitivity means the entry tier must deliver fast value.

## Output

Deliver: the value metric, the recommended model with rationale, a willingness-to-pay estimate with cited comparisons, the tier/packaging structure with feature fences and free/trial decision, specific starting price points, the expansion and discounting stance, and a test plan. Consider delivering the tier comparison as a pricing-page table (design-brief for the visual) or a spreadsheet (xlsx skill). Include a Sources section for competitor pricing. Save the pricing model to `.vital/pricing.md`.
