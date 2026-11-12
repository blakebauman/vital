---
name: launch-plan
description: >
  Planning and sequencing a launch moment — timeline, asset checklist, channel
  plan, contingencies. For "launch plan", "launch checklist", "launch week",
  "how do I launch", "Product Hunt launch", "coordinate my launch".
metadata:
  version: "0.1.0"
---

Build a coordinated launch: the timeline, the assets, the channels, and the owners, so nothing is missed on launch day. Pull the message from brand and the motion from GTM; this skill sequences the moment.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

## 1. Define the launch

Establish the launch type and goal:

- **Type** — private beta, waitlist open, public launch, big feature, funding, or platform launch (Product Hunt, Hacker News, app store).
- **Goal** — the one primary metric this launch must move (signups, revenue, press, waitlist, upvotes). Secondary goals noted but subordinate.
- **Date and constraints** — target date, hard dependencies, and what the client must finish first (their build/delivery is theirs, not Vital's).

Scale the launch shape to the **client's segment** — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`. Enterprise launches are longer and phased (design partners → pilots → GA), gated by security/procurement, and often paired with analyst briefings; mid-market blends a public moment with a sales-assist follow-through; small-business launches are fast, single-moment, and platform/community-driven.

## 2. Message and offer

State the single launch message (from brand's messaging) and the specific call to action. One launch, one message, one primary CTA.

## 3. Channel plan

List every channel the launch fires on — owned (site, email, social), earned (press, communities, launch platforms), and paid if any. For each: the asset, the message adaptation, and the timing relative to launch hour.

## 4. Asset checklist

Enumerate every asset needed, with owner and status: landing/launch page, announcement post, email(s), social posts and graphics, launch-platform copy and media, press materials, demo or video, and internal FAQ. Route creative to the `design-brief` skill, press to `press-kit`, and campaign copy to `content-engine`.

## 5. Timeline

Build a dated timeline across three windows:

- **Pre-launch** (T-minus weeks/days) — audience building, press embargoes, waitlist, asset production, dry run.
- **Launch day** (hour by hour) — the sequence of what fires when, who pushes it, and how the team responds to momentum.
- **Post-launch** (T-plus days/weeks) — follow-up, thank-yous, retrospective, and converting attention into retained users.

## 6. Roles and readiness

Assign an owner to each item. List the go/no-go readiness checks (product works, page live, tracking in place, support ready). Flag anything the client must complete.

Include launch-day **traffic readiness** as a go/no-go check: the page served as cached static assets, the signup path load-tested, Turnstile on forms, a rate limit on the most expensive endpoint, and analytics verified before traffic arrives. If the client has no stack, use the Cloudflare free-plan checklist and upgrade triggers in `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/cloudflare-stack.md`. If the product itself can only handle so many users at once, decide before launch day how overflow is handled: a Waiting Room (a queue page that admits people as capacity frees up, Business plan only) or a free waitlist page that invites people in batches.

## 7. Contingencies

Note the two or three most likely things to go wrong (site down, low traction, negative comment) and the pre-agreed response to each.

## Output

Deliver a launch plan with type/goal, message and CTA, channel plan, asset checklist with owners, a dated three-window timeline, readiness checks, and contingencies. Consider delivering it as a shareable HTML tracker the client will revisit. Offer to set up scheduled reminders for key launch milestones if the host supports scheduling. Save the plan to `.vital/launch-plan.md`.
