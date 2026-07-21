---
name: sales-enablement
description: >
  Use this skill to equip the people who actually sell — the qualification and
  discovery framework, the pitch and demo script, the sales deck and one-pager,
  competitive battlecards, objection handling, the pipeline stages and exit
  criteria, and the founder-led-to-first-rep transition. Triggers include "sales
  deck", "sales playbook", "discovery questions", "qualification", "MEDDIC",
  "BANT", "demo script", "battlecard", "objection handling", "how do I sell
  this", "pipeline stages", "founder-led sales", or "when should I hire a
  salesperson".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Equip the people who sell. GTM decides the motion, ABM picks the accounts, and
`rfp-response` clears the procurement gates — this skill produces what happens in
the conversation itself: what the seller asks, what they show, what they say when
the buyer pushes back, and how a deal is judged real.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

Pull the narrative from `.vital/positioning.md`, the message pillars from
`.vital/brand.md`, the competitive set and wedge from `.vital/competitive.md`,
the motion and price from `.vital/gtm.md` and `.vital/pricing.md`, and proof from
`.vital/customer-marketing.md`. Sales collateral that contradicts the positioning
is how one narrative becomes three.

**Vital does not sell for the client.** This skill produces the playbook, the
words, and the materials. The client's founders and reps run the conversations.
Never write outreach that fabricates urgency, invents a deadline or scarcity that
does not exist, or claims a capability the product lacks — route technical claims
through the `engineering` agent when they are load-bearing.

Adapt to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Enterprise needs multi-stakeholder discovery, a business case for the economic buyer, and a champion who can sell internally when the seller is not in the room; mid-market runs a compressed cycle with a sales-assist overlay on self-serve; small business should mostly not have a sales conversation at all — if a rep is needed to close a $40/month product, the problem is the funnel, not the pitch.

## 1. Who sells, and when to hire

Start with the honest answer for this stage. **Founders should sell first** —
until the motion is repeatable, discovery findings are the product roadmap and no
rep can learn what the founder has not yet figured out. Name the signals that
say it is time for the first sales hire (a repeatable close, a known cycle
length, the founder as the bottleneck rather than the differentiator) and the
ones that say it is not (no closed-won pattern, price still moving, the founder
still learning why deals die). Hiring a VP Sales to find product-market fit is
the expensive version of this mistake.

## 2. Qualification

Pick **one** framework and adapt it — MEDDIC/MEDDPICC for complex enterprise,
SPICED or a simple pain/authority/timing test for shorter cycles. Do not
cargo-cult an enterprise framework onto a two-call sale.

Define what each letter means *for this product*: what counts as a metric here,
who the economic buyer actually is in this buying committee, what a real
compelling event looks like versus a manufactured one. Then define
**disqualification** just as explicitly. A fast no is worth more than a slow
maybe — bad-fit deals consume the quarter, churn out, and poison the reference
pool. Name the three profiles this client should walk away from.

## 3. Discovery

Write the discovery script: the questions that surface the pain, its cost, the
status quo, the buying process, and the people. Good discovery is diagnosis, not
a survey — each question should change what the seller does next.

- **Pain and stakes** — what breaks today, how often, what it costs. Push for a
  number the buyer states themselves; a self-quantified pain is the whole
  business case.
- **Status quo and alternatives** — what they do now, what else they are
  evaluating, and what happens if they do nothing (the most common competitor).
- **Process** — who else must say yes, what the approval path is, whether budget
  exists or must be created, and what has killed similar purchases here before.
- **Champion test** — can this person articulate the value to their CFO without
  the seller present? If not, there is no champion yet.

Include the follow-up email template that plays discovery back to the buyer in
their own words — the single highest-leverage artifact in a complex sale.

## 4. The pitch and demo

Build the demo as a **narrative, not a feature tour**. Open on the pain the
buyer just described, show the shortest path to the "aha", then earn the right to
show depth. Specify:

- The one-sentence value statement, inherited from positioning.
- The three-to-five beat demo flow, with the moment that lands the aha named.
- What to cut. Most demos are twice as long as they should be, and the buyer
  decides in the first few minutes.
- The trap questions this product invites, and honest answers to each.

## 5. Collateral

Produce what the seller and the champion actually need — route design to
`design-brief` and deck production to the `pptx` skill when available, slide-by-
slide markdown otherwise:

- **Sales deck** — the argument, not the company brochure.
- **One-pager / leave-behind** — what the champion forwards internally.
- **Business case / ROI model** — the economic buyer's artifact. Build it from
  the buyer's own numbers, with assumptions visible and conservative. An ROI
  model the buyer cannot audit is a model they will not defend.
- **Battlecards** — one per named competitor from `.vital/competitive.md`: where
  they genuinely win, where the client wins, the trap questions to ask, and the
  honest response when the competitor is the better fit. Never write a battlecard
  that misrepresents a competitor; buyers check, and a caught exaggeration costs
  the deal and the reputation.

## 6. Objection handling

List the objections this product will actually hit — price, incumbent, build-vs-
buy, security and compliance, timing, "we'll revisit next quarter" — and write the
honest response to each. Structure: acknowledge, understand the objection behind
the objection, respond with evidence, confirm it landed.

Separate objections to **answer** from objections to **respect**. When the buyer
is genuinely a bad fit, or the timing is genuinely wrong, the correct move is to
disqualify or park the deal — not to overcome it. Route security and procurement
objections to `rfp-response`, price objections to `pricing-strategy`, and
credibility objections to customer references.

## 7. Pipeline and process

Define the stages by **buyer evidence, not seller optimism**. Each stage gets an
exit criterion that is an observable buyer action — "champion introduced us to
the economic buyer", "security review scheduled" — never "prospect seems
interested". This is the single change that makes a forecast mean anything.

Specify the CRM fields worth maintaining (few, and each tied to a decision),
the handoff points to `rfp-response` and `customer-marketing`, and a simple
win/loss review: ask the buyer why, including on losses, and feed what you learn
back to `positioning` and `pricing-strategy`. Pipeline metrics and definitions go
through the `measurement` skill — stage conversion, cycle length, win rate, and
average deal size, defined precisely enough to be trusted.

## Output

Deliver: the who-sells recommendation for this stage, the adapted qualification
framework with explicit disqualification criteria, the discovery script and
recap-email template, the demo narrative with the aha moment named, the collateral
set (deck, one-pager, business case, battlecards per named competitor), objection
handling split into answer-versus-respect, and pipeline stages with
buyer-evidence exit criteria. Keep every claim consistent with the positioning
and truthful about both the product and the competitors. Include a Sources
section for any competitor or framework research. Save the playbook to
`.vital/sales-enablement.md`.
