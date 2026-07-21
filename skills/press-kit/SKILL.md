---
name: press-kit
description: >
  Use this skill for press and launch communications — the newsworthy angle,
  press release, media list, tailored journalist pitches, and launch-platform
  copy (Product Hunt, Hacker News, communities). Triggers include "get press",
  "press release", "media list", "pitch journalists", "announcement", "PR for
  my launch", or "Product Hunt launch copy".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Earn third-party attention for the launch. Coverage comes from a specific story a specific audience cares about — never a generic blast. Pull the message from brand and the launch timing from the launch plan.

Tailor the press approach to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. For enterprise, weight **analyst relations** (Gartner, Forrester, IDC briefings), trade/vertical press, and named-customer proof; for mid-market, tech and vertical press plus founder narrative; for small business, launch platforms, niche newsletters, and community-driven attention over analyst relations.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

## 1. Find the angle

"We launched a product" is not news. Tie the launch to something a journalist's readers care about: a trend, a tension or conflict, a surprising data point, a genuinely new capability, or a notable founder story. Draft two or three candidate angles and pick the strongest. If the launch is honestly not newsworthy to press, say so and redirect effort to launch platforms and communities.

## 2. Media list

Build a tailored list of outlets and specific journalists who cover this beat and this kind of story. For each: name, outlet, what they cover, a recent relevant piece, and why they fit. Ten well-matched names beat two hundred generic ones. Research with web search; cite what you find.

## 3. Press release / announcement

Write the announcement in inverted-pyramid form: a headline that states the news, a lead that answers who/what/why-it-matters, supporting detail, a founder quote (drafted for the client to approve — never fabricated or attributed to anyone who has not said it), boilerplate, and contact/links. Keep it factual; strip hype adjectives.

## 4. Pitches

Write a short, tailored pitch per priority journalist. Lead with their reader's interest, reference their beat specifically, keep it to a few sentences, make the ask easy, and offer what they need (demo, exclusive, assets, founder time). Include a subject line built to be opened.

## 5. Launch-platform copy

For Product Hunt, Hacker News, and relevant communities: write the copy and first comment in the tone that platform rewards, and note the etiquette (HN dislikes marketing speak; Product Hunt rewards a clear maker story). Sequence when each posts relative to launch hour. Never manufacture inauthentic upvotes or comments.

## 6. Press kit

Assemble the simple kit: fact sheet, boilerplate, founder bio, logo/screenshot links, and where to reach the client.

## Output

Deliver the chosen angle, a tailored media list with rationale and sources, the press release, per-outlet pitches, launch-platform copy, and the press-kit contents. Keep everything verifiable and free of fabricated quotes or endorsements; do not attribute persuasive statements to real named public figures. Include a Sources section for media research. Save materials to `.vital/press-kit/`.
