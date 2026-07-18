---
name: brand-messaging
description: >
  Use this skill for naming, messaging architecture, and voice and tone.
  Triggers include "name my product", "naming", "messaging framework",
  "value proposition", "website copy sounds generic", "brand voice", "tone
  guide", or turning positioning into the words and names a product goes to
  market with.
metadata:
  version: "0.1.0"
---

Turn positioning into the verbal identity: the value proposition, the message hierarchy, the voice, and (when needed) the name. Require positioning first — pull it from the project or run the `positioning` skill. Do the parts the request calls for.

Tune the message and voice to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Enterprise messaging is credible and proof-heavy with security/compliance/integration pillars and low hype; mid-market is benefit-forward with proof close behind; small-business messaging is plain, direct, and outcome-first with a warmer voice.

## Messaging architecture

Build top-down; do not move to a lower level until the one above is sharp.

1. **Value proposition** — one line: the core promise, in the customer's language, that no competitor can copy verbatim. Draft several; pick the sharpest.
2. **Message pillars** — three to five supporting themes that prove the value proposition. Each is a benefit, not a feature.
3. **Proof** — under each pillar, the concrete evidence (capability, metric, testimonial, mechanism). A pillar without proof is a slogan; cut it or find proof.
4. **Headline system** — a set of headline/subhead pairs the value prop and pillars generate, ready for the site, deck, and ads.
5. **Audience flex** — how the message adjusts per ICP segment or channel without losing the core.

## Voice & tone

- Define three to five voice traits (e.g., "direct, technically credible, warm, no hype").
- State what the brand sounds like and explicitly what it never sounds like.
- Show, don't tell: give before/after rewrites of a real sentence demonstrating the voice.
- Note how tone shifts by context (landing page vs. error message vs. launch announcement) while the voice stays constant.

## Naming (when requested)

1. Generate broadly across naming approaches: descriptive, evocative, invented, metaphor, founder/real-word. Aim wide before filtering.
2. Screen the shortlist for meaning, memorability, pronounceability, spelling-on-hearing, and rough .com/handle availability.
3. Deliver a shortlist of five to eight with a one-line rationale each and any obvious risks flagged. Note that you cannot perform legal trademark clearance — recommend the client do so before committing.

## Output

Deliver the value proposition, message hierarchy with pillars and proof, headline system, and voice-and-tone guide with examples; plus a named shortlist when naming was requested. Keep every line specific and ownable — strike anything that could sit unchanged on a competitor's homepage. Save the messaging system to `.vital/brand.md` so design, marketing, and PR execute against one source of truth.
