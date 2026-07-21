---
name: positioning
description: >
  Use this skill to develop product positioning, define the ideal customer
  profile (ICP), and frame product-market fit. Triggers include "help me
  position my product", "who is this for", "what's my ICP", "how do I
  describe what makes us different", "positioning statement", or framing a
  product's value and differentiation before going to market.
metadata:
  version: "0.1.0"
---

Develop sharp, honest positioning that every other launch discipline will build on. Work through the sections below in order. Anchor on the customer and their alternatives, not the product's feature list.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

## 1. Intake

Establish, asking only what you cannot infer from context or prior work:

- What the product does, concretely, in one sentence.
- Who it is for and what problem it solves for them.
- What those people use today instead (including "do nothing").
- Any traction, feedback, or usage signals that already exist.

Tailor depth and framing to the **client's segment** (enterprise / mid-market / small business) — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. For enterprise, separate the user, economic buyer, and champion and map the buying committee; for mid-market, center a primary buyer who is also a heavy user, mapping the small committee (2–3) around them when they can block; for small business, nail one persona and one job.

## 2. ICP definition

Define the ideal customer profile — the segment that feels the pain most acutely and is easiest to reach:

- Who they are (role, company type/size, or consumer segment).
- The trigger that makes them look for a solution now.
- The alternatives they currently use and why those fall short.
- Where they are reachable (channels, communities, search terms).

Prefer a narrow, specific beachhead over a broad "anyone who…". Win the beachhead first.

## 3. Competitive frame

Identify the real competitive set — direct products, adjacent tools, manual workarounds, and the status quo. For each, state the position they occupy in the customer's mind. Then find the **wedge**: the narrow place where this product is clearly the best choice. Position against the true alternative, which is often inertia.

## 4. Positioning statement

Write a positioning statement in this shape, then also as one natural sentence:

> For [ICP] who [need/trigger], [product] is a [category] that [key benefit]. Unlike [primary alternative], [product] [key differentiator].

The category choice is a strategic decision — the frame you claim shapes who you are compared to. Choose it deliberately.

## 5. Product-market-fit framing

State the value hypothesis (who gets what value, and why it is a must-have not a nice-to-have), the "very disappointed" test, and the two or three signals that would prove fit is real.

## 6. Narrative

Write a one-paragraph narrative — the throughline story that makes the positioning land emotionally: the shift in the world, the tension it creates for the customer, and how the product resolves it.

## 7. Pressure test

State the single strongest argument against this positioning and answer it honestly. If you cannot answer it, the positioning needs work — say so.

## Output

Deliver: ICP definition, competitive frame with the wedge named, the positioning statement (both forms), PMF framing, and the narrative paragraph. Be concrete — name real competitors and real segments. Strike empty adjectives ("innovative", "seamless", "next-generation"). For a deeper competitor pass, use the `competitive-teardown` skill. Save the final positioning to `.vital/positioning.md` so brand, GTM, marketing, and PR can build on it.
