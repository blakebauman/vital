---
name: partnerships
description: >
  Use this skill to build a partnerships and channel program — integration and
  technology partners, resellers and VARs, agencies and system integrators,
  marketplace and ecosystem listings, co-marketing, OEM/embed, and referral
  programs. Covers partner selection, the pitch to the partner, deal structure
  and economics, enablement, and partner-sourced pipeline metrics. Triggers
  include "partnerships", "channel strategy", "reseller", "integration partner",
  "co-marketing", "co-sell", "referral program", "affiliate", "list on the AWS
  or Salesforce marketplace", "should we partner with", or "a big company wants
  to partner with us".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Build partnerships that produce customers, not logos on a slide. Most
partnerships fail for one reason: neither side actually needed the other, so
after the announcement nobody does the work. This skill exists to prevent that —
start with whether to partner at all, and only then design the program.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

Pull the ICP from `.vital/positioning.md`, the motion from `.vital/gtm.md`, the
margin room from `.vital/pricing.md`, and the competitive set from
`.vital/competitive.md` — a partner who competes with the client's wedge is not a
partner.

> **Not legal advice.** Partner agreements, reseller contracts, revenue-share
> terms, and OEM licensing are binding commercial documents with real liability.
> Vital drafts the commercial *shape* — economics, responsibilities, term — and
> the founder's attorney drafts and reviews the agreement itself.

Adapt to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Enterprise partnering runs through SIs, VARs, and platform ecosystems with co-sell motions and long enablement cycles; mid-market leans on integrations and agency partners; small business is mostly marketplace listings, integrations, and referral programs — a reseller channel is almost always the wrong shape at that price point.

## 1. Should you partner at all?

Answer this before anything else, honestly.

- **What job is the partnership doing?** Distribution (their audience), product
  completeness (their capability), credibility (their brand), or access (their
  relationships). If you cannot name one in a sentence, there is no partnership —
  there is a meeting.
- **What does the partner get, in their own metrics?** If you cannot state their
  side as clearly as yours, they will not prioritize it. This is the single
  most common reason partnerships die quietly.
- **Are you too early?** Pre-product-market-fit, partnerships are usually a
  well-dressed distraction. A big-company partnership takes six to eighteen
  months, consumes senior time and scarce engineering, and the effort is
  asymmetric — you need them far more than they need you. Say so plainly when
  that is the situation, and recommend the client win customers directly first.
- **Is the alternative cheaper?** Many "partnership" goals are better served by
  an integration nobody signed a contract for, a marketplace listing, or a
  content collaboration. Recommend the lightest structure that does the job.

If the honest answer is "not yet", say it and stop. Do not design a program to
be polite.

## 2. Partnership types

Match the type to the job. Each has a different cost, timeline, and failure mode:

- **Integration / technology** — you work with their product. Cheapest, fastest,
  most durable. Usually the right first move.
- **Marketplace / ecosystem listing** — AWS, Salesforce AppExchange, HubSpot,
  Shopify, Atlassian. A distribution channel with search mechanics, not a
  relationship. Treat it like SEO, not like BD.
- **Referral / affiliate** — they send leads for a fee. Simple, low commitment,
  low volume.
- **Agency / SI / consulting** — they implement for clients. Powerful in
  enterprise; requires margin and real enablement.
- **Reseller / VAR** — they sell your product as their own line item. Needs
  genuine margin, deal registration, and a support model.
- **Co-marketing** — joint content, webinars, events. Route execution to
  `content-engine`; joint customer stories to `customer-marketing`.
- **OEM / embed** — your product inside theirs. Highest leverage, highest lock-in,
  hardest terms. Watch for becoming a dependent supplier to one customer.

## 3. Target selection

Define the partner profile before building a list: same customer, non-competing,
complementary job-to-be-done, and a real reason to care. Then score candidates on
three axes and rank:

- **Reach** — how much of the client's ICP they actually touch. Not company size.
- **Motivation** — how much they need what the client provides. This is the axis
  everyone under-weights and it predicts success better than the other two.
- **Effort** — integration work, contracting friction, enablement burden.

Recommend a deliberately short list. Five partnerships worked properly beat
fifty announced. Research candidates and cite what you find.

## 4. The pitch to the partner

Write the partner-facing pitch, and write it in **their** terms: the problem
their customers have that the client solves, what it does for their retention,
attach rate, deal size, or roadmap gap — and what specifically you are asking
for. Include the ask, the effort estimate on their side, and what the client does
so the burden is not symmetric.

Include a one-page partner brief the internal champion at the partner can forward
— the same job the champion does in a sales cycle. Route design to
`design-brief`.

## 5. Deal structure and economics

Specify the commercial shape and check it against the client's actual margin
(`.vital/pricing.md`) — a 30% reseller margin on a product with 40% gross margin
is not a channel, it is a loss:

- **Economics** — referral fee, revenue share, reseller discount, co-sell
  splits, or nothing at all. Say which and why.
- **Who owns what** — the customer relationship, billing, renewals, support tier
  one, and the data. Get this explicit before signing, not after the first
  escalation.
- **Term and exit** — length, exclusivity (avoid it early — it caps the channel
  for one unproven partner), termination, and what happens to shared customers.
- **Deal registration** — how channel conflict with the client's own sellers is
  resolved. Without this the partner stops trusting you the first time it
  happens. Coordinate with `sales-enablement`.

## 6. Enablement and activation

**Signed is not launched.** A partnership produces nothing until a specific
human at the partner can explain, demo, and sell the product. Specify the
onboarding: partner training, a demo environment, the collateral and battlecards
they need, the named contact on each side, the launch moment, and the first
ninety days of joint activity. If nobody at the partner owns it by name, the
partnership does not exist.

## 7. Measurement and pruning

Metric definitions go through the `measurement` skill; the partner-specific ones
that matter:

- **Partner-sourced** vs **partner-influenced** pipeline — defined separately and
  never conflated, because conflating them is how a channel looks productive
  while producing nothing.
- **Activation rate** — the share of signed partners who have ever produced a
  single deal. Expect it to be low; most programs are carried by a handful of
  partners while the rest are overhead.
- **Time to first deal**, and partner-sourced CAC versus direct.

Set a review cadence and a **sunset rule**: a partner that has produced nothing
by an agreed date gets wound down or explicitly reset. Dead partnerships are not
free — they consume enablement, support, and the client's attention.

## Output

Deliver: the should-we-partner verdict with its reasoning, the partnership type
matched to the job, a scored and ranked target shortlist with sources, the
partner-facing pitch in the partner's own terms, the deal structure with
economics checked against real margin, the enablement and activation plan with
named owners, and the metrics with a sunset rule. Be willing to conclude that the
client should not run a partner program yet. Include a Sources section for
partner and marketplace research. Save the program to `.vital/partnerships.md`.
