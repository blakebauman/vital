---
name: content-engine
description: >
  Use this skill to build the content and demand engine — content strategy and
  calendars, multi-channel campaigns, SEO clusters, email flows, social plans,
  and growth loops. Triggers include "content plan", "content calendar",
  "launch campaign", "email sequence", "SEO strategy", "social plan", "build
  an audience", or designing repeatable programs that create and capture demand.
metadata:
  version: "0.1.0"
---

Design repeatable programs — not one-off posts — that create and capture demand, each mapped to a funnel stage. Pull the ICP from strategy and the messaging and voice from brand. Build the parts the request calls for; when drafting copy the client will publish as themselves, check for a saved `my-writing-style` profile first.

Match the content program to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Enterprise leans on thought leadership, whitepapers, webinars, case studies, and account-based campaigns to named targets with longer nurture; mid-market on comparison content, ROI calculators, and lifecycle email; small business on high-velocity SEO, social, and self-serve education.

## 1. Objective and funnel map

State the objective (build pre-launch audience, drive launch signups, activate users, retain) and which funnel stage it serves: awareness, consideration, activation, or retention. Keep effort balanced across stages rather than piling all of it on awareness.

## 2. Content strategy

Define the content pillars (three to five themes tied to the message pillars), the formats that fit the ICP and the client's capacity, the channels, and the cadence. Favor formats that compound and can be repurposed across channels.

## 3. Calendar

Produce a concrete, dated calendar: for each slot, the date, channel, format, working title/hook, pillar, and funnel stage. Make it real enough to execute — not a themes-by-week abstraction. Cover the window requested (e.g., 4–8 weeks pre-launch through launch).

## 4. Campaign build (when a campaign is the ask)

For a launch or feature campaign: the objective and success metric, the single message, and the sequenced assets across channels with timing. Draft the key pieces — email subject lines and body, social posts, ad copy variants — in the brand voice.

## 5. SEO (when relevant)

Identify the topic clusters the ICP actually searches, the pillar page and supporting pages per cluster, and the priority order by intent and winnability. Anchor to real search behavior, not vanity keywords.

## 6. Email flows (when relevant)

Design the lifecycle flows needed: welcome/nurture, launch, activation, re-engagement. For each, the trigger, the sequence, the goal of each message, and drafts of the critical emails.

## 7. Growth loops

Identify at least one loop where output feeds input (referral, user-generated content, content-to-audience, product-generated). Prefer loops that compound over tactics that decay.

## Output

Deliver the objective and funnel map, content pillars, a dated calendar, and the specific campaign/SEO/email/social plans requested — with real draft copy where it helps and the metric each program moves. Route graphics to the `design-brief` skill. Consider delivering the calendar as a spreadsheet (xlsx skill) or a shareable tracker. Offer to set up recurring scheduled tasks for ongoing content cadence. Save the plan to `.vital/marketing.md`.
