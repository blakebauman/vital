---
name: fundraising
description: >
  Use this skill to plan and run a startup fundraise, or to decide whether to
  raise at all. Covers the raise-vs-bootstrap decision, stage and amount,
  instruments (post-money SAFE, convertible note, priced round), valuation and
  dilution, investor targeting and outreach, the data room, term sheets, and
  the close. Triggers include "raise a round", "seed round", "pre-seed",
  "SAFE", "how much should I raise", "investor list", "term sheet", "valuation",
  "dilution", or "should I raise or bootstrap".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Help a founder decide whether to raise, then run the raise well if they do. A fundraise is a sales process with a specific buyer, a specific narrative, and a specific close — treat it like one.

> **Not investment, legal, or financial advice.** Vital provides information, benchmarks, and drafts only. Fundraising is regulated by securities law and every deal has binding legal and tax consequences. Tell the founder to engage a startup attorney for any financing documents and to understand the securities rules before soliciting investors. Nothing here is a recommendation to raise, to invest, or a valuation opinion.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

## 1. The fork: raise or bootstrap?

Before any raise mechanics, help the founder decide honestly. Venture capital suits a minority of companies — those with a large market, a path to venture-scale outcomes, and a need for capital to win before competitors. If the business can grow on revenue, or the market can't support a venture outcome, bootstrapping keeps control and optionality. Reason from market size, capital intensity, growth ambition, competitive dynamics, and the founder's own goals. If bootstrapping fits better, route to the `bootstrapping` skill and stop — do not talk them into a raise.

## 2. Stage, amount, and milestone

Tie the raise to the **specific milestone that unlocks the next round**, not to a generic runway number. Under-raising starves the milestone; over-raising over-dilutes and raises the bar for the next round.

**Research the current numbers before you quote any.** Round sizes, valuations, and dilution shift with the market, and a stale figure stated confidently is worse than no figure. Look them up, cite the source, and use `${CLAUDE_PLUGIN_ROOT}/skills/fundraising/references/benchmarks.md` only as a sanity check on what you find — that file carries a "last verified" date and is stale by default. Benchmarks tell you whether an ask is unusual; the milestone tells you whether it is right.

## 3. Instrument

Explain the choice and recommend:

- **Post-money SAFE** (YC standard) — fast, cheap, founder-friendly for early rounds; the cap sets effective ownership; watch **SAFE stacking** (multiple SAFEs at different caps quietly compound dilution — model the as-converted cap table).
- **Convertible note** — like a SAFE but debt (interest, maturity date). Less common now at the earliest stage.
- **Priced round** — actual equity sold at a set valuation with a term sheet; standard at seed $3M+ and Series A. More legal work, more certainty, sets a real valuation and board/pro-rata terms.

Always model dilution as-converted, including the option pool and all outstanding SAFEs, before the founder commits to caps.

## 4. Investor targeting

Build a targeted investor list, not a spray. Identify the funds and angels that invest at this stage, in this category, in this geography, with dry powder and no competing portfolio conflict. For each: check size range, stage focus, thesis fit, notable relevant investments, and the warmest intro path. Research with web tools and cite. A tight, well-matched list with warm intros beats a mass cold campaign. Prioritize into tiers and sequence outreach (start with a few to calibrate, not your top choice first).

## 5. Materials & data room

- **Pitch deck** — route to the `pitch-deck` skill.
- **Narrative & one-liner** — inherit from `strategy` positioning and `brand` messaging.
- **Data room** — the organized set investors will diligence: incorporation docs, cap table, financial model and metrics, key contracts, IP assignments, product/traction data, team. Build the checklist and structure; note that content must be real and accurate.
- **The model** — a simple, credible financial model showing the milestone the raise buys and the trajectory — the `xlsx` skill when available, a markdown table with stated assumptions otherwise.

## 6. Process & close

Run it as a process: warm intros → first meetings → partner meetings/diligence → term sheet → close. Create urgency with a concentrated timeline rather than an open-ended drip. Explain term-sheet basics at a high level (valuation, option pool, pro-rata, board, liquidation preference, anti-dilution) — and route the actual terms to the founder's attorney. After a term sheet, diligence and legal close the round.

## Output

Deliver: the raise-vs-bootstrap recommendation; if raising, the stage/amount tied to a milestone, the instrument recommendation with dilution modeled, a tiered and warm-intro-mapped investor list, the materials and data-room checklist, and a process plan with timeline — all with the not-investment/legal-advice boundary stated and a prompt to engage an attorney. Include a Sources section for benchmarks and investor research. Save the plan to `.vital/capital/fundraising.md`.

## Additional resources

- **`${CLAUDE_PLUGIN_ROOT}/skills/fundraising/references/benchmarks.md`** — pre-seed and seed round-size, valuation, and dilution anchors with a "last verified" date. Stale by default; re-research before quoting.
