---
name: pitch-deck
description: >
  Use this skill to build a fundraising pitch deck. Covers the narrative and
  the standard slide sequence (problem, solution, why now, market, product,
  traction, business model, GTM, competition, team, ask/use of funds), plus
  the story, common mistakes, and the data-room companion. Triggers include
  "pitch deck", "investor deck", "fundraising deck", "seed deck", "demo day
  deck", or "deck for investors".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Build a fundraising pitch deck that earns the next meeting. A deck is not a document — it is the argument for why this company is a venture-scale opportunity, told in a sequence an investor can follow in ten minutes. Inherit the positioning from `strategy`, the messaging from `brand`, the model from `gtm`/`pricing-strategy`, and the raise details from `fundraising`. Production goes through the `design` agent and the pptx skill.

> **Not investment advice.** Vital helps craft the narrative and materials. Any figures (traction, financials, projections) must be true and the founder's own; investors diligence them. Fundraising is regulated — the founder's attorney should review what goes to investors.

## 1. The story first

Before slides, nail the throughline: the world is changing (why now), which creates a painful problem for a specific customer, which this product uniquely solves, and there is a large, reachable market and a team uniquely able to win it. Every slide advances this argument. A deck that is a feature list, not an argument, fails. Write the one-sentence thesis first.

## 2. The standard sequence

Adapt to stage and company, but the proven seed/Series A sequence is:

1. **Cover / one-liner** — company, the single-sentence what-and-for-whom.
2. **Problem** — the specific, painful, urgent problem and who has it. Make it visceral.
3. **Solution** — what the product is and the "aha" of how it solves the problem.
4. **Why now** — the shift (technology, regulation, behavior) that makes this possible and urgent today.
5. **Market** — the size and shape of the opportunity (bottom-up TAM/SAM/SOM, not just a huge top-down number). Show the reachable wedge and the expansion.
6. **Product** — how it works, the magic, a real screenshot or demo. Show, don't describe.
7. **Traction** — the most important slide once you have any: growth, revenue/MRR, users, retention, logos. Momentum sells. If pre-traction, lead with evidence of demand and validation.
8. **Business model** — how you make money, pricing, unit economics.
9. **Go-to-market** — how you acquire customers repeatably (the motion and the early proof).
10. **Competition** — the honest landscape and your defensible wedge; position against the status quo too. Avoid the empty 2×2 with you alone in the top-right.
11. **Team** — why this team wins: founder-market fit, relevant edge, key hires. Investors bet on people at early stages.
12. **The ask / use of funds** — how much you're raising, the milestone it buys, and the rough allocation. Tie it to the next round.

Optionally: a financial projection slide, a vision/closing slide, and an appendix for diligence detail.

## 3. Two decks

Distinguish the **send deck** (read alone, more self-explanatory text) from the **present deck** (talked over, sparse visuals). Note which the founder needs; often both. Keep either tight — investors spend seconds per slide.

## 4. Common mistakes to avoid

Too many words per slide; leading with the product instead of the problem; a top-down "1% of a $B market" TAM; a competition slice that pretends no one else exists; hiding weak traction instead of framing the demand evidence; no clear ask; inconsistent numbers between deck, model, and data room. Fix these before it goes out.

## 5. Design & production

Route art direction and build to the `design` agent / `design-brief` skill (and the pptx skill for the actual file). The deck must be visually clean and credible — investors read production quality as a signal — but substance and clarity beat decoration. Run the impeccable anti-slop check on the visuals.

## Output

Deliver: the one-sentence thesis, the slide-by-slide content (headline + key points + what data goes on each), guidance on send vs. present versions, a mistakes check against the draft, and the hand-off to design/pptx for production. Ensure every figure is the founder's own and consistent across deck, model, and data room. Save the deck content and file to `.vital/capital/pitch-deck.md`.
