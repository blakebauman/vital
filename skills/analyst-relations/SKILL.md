---
name: analyst-relations
description: >
  Use this skill to build an industry-analyst relations program for enterprise
  credibility. Triggers include "analyst relations", "AR", "Gartner",
  "Forrester", "IDC", "Magic Quadrant", "Forrester Wave", "analyst briefing",
  "get on the analyst's radar", or preparing to engage industry analysts to
  influence enterprise buyers.
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Build an analyst-relations program that earns enterprise credibility by influencing the analysts enterprise buyers trust. AR is a long game — it compounds over quarters, not days. Use for enterprise motions where buyers consult Gartner, Forrester, or IDC — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`.

## 1. Set the objective

Clarify what AR is for: getting on an analyst's radar, being included in a landscape/market report, competing for a Magic Quadrant / Forrester Wave position, or simply getting expert validation for the sales cycle. Objectives drive who you engage and how. Be realistic about timelines — inclusion in ranked reports often takes 12+ months of relationship.

## 2. Map the analysts

Identify the specific analysts and firms who cover this category and whose opinion the client's target buyers actually read. For each: firm, the market/category they cover, relevant recent reports, and their apparent point of view. Prioritize a short list — a few deep relationships beat many shallow ones. Research with web search; cite reports and coverage found.

## 3. Craft the narrative

Build the analyst-facing narrative (distinct from press and marketing): the market shift, where the category is going, the problem with the status quo, and how the client's approach fits the future the analyst already believes in. Analysts respond to a credible market thesis and evidence, not product hype. Anchor to strategy's positioning and back claims with data, customer proof, and roadmap.

## 4. Build the briefing kit

Assemble the briefing deck and materials: market context, the client's differentiated approach, proof (customers, metrics, architecture where relevant), roadmap, and the specific questions to leave the analyst thinking about. Keep it tight and evidence-led. Route deck production to the pptx skill and visuals to `design-brief`. Prepare a short pre-read and a concise leave-behind.

## 5. Engagement plan

Sequence the engagement: initial briefing, follow-up inquiry, ongoing updates, and (if pursuing a ranked report) the evaluation process and its requirements. Define the cadence (e.g., quarterly briefings, update on major milestones) and who from the client presents. Note the etiquette: briefings are not sales pitches; inquiries are the client asking the analyst; keep commitments and follow through.

## 6. Prep for ranked evaluations (when relevant)

If competing for a Magic Quadrant or Wave: identify the evaluation criteria, honestly assess the client against each, close the credible gaps that can be closed in time, line up customer references, and prepare the survey/demo responses. Be candid where the client is not yet ready — a premature push wastes the relationship.

## 7. Measurement

Track leading indicators: briefings held, analyst sentiment shift, mentions/inclusions in reports, inquiries from the client's prospects that cite an analyst, and (lagging) ranked-report position. 

## Output

Deliver the AR objective, a prioritized analyst map with sources, the analyst narrative, the briefing kit outline (and deck if requested), a sequenced engagement plan with cadence, ranked-evaluation prep when relevant, and metrics. Coordinate with the `press-kit` skill so AR and press reinforce one story. Include a Sources section. Save the program to `.vital/analyst-relations.md`.
