---
name: community-building
description: >
  Use this skill to build and grow a community around a product or open-source
  project — Discord/Slack communities, GitHub open-source contributor
  communities, forums, and developer relations. Triggers include "build a
  community", "Discord community", "open source community", "grow my GitHub
  project", "get contributors", "DevRel", "developer community", "community
  strategy", "ambassador program", or "community-led growth".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Build a community that compounds: a place where users help each other, contributors improve the product, and advocates bring the next wave. Community is a long game and a growth loop, not a launch tactic — design for retention and contribution, not vanity metrics. Coordinates with the community-led GTM motion (`gtm-plan`), advocacy (`customer-marketing`), content (`content-engine`), and launch-platform comms (`press-kit`). Anchor to the client's segment — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`.

## 1. Purpose and strategy

Establish why the community exists — its primary job drives every other decision:

- **Support** — users help users; deflects load, improves retention.
- **Advocacy/growth** — members bring members; a growth loop.
- **Product feedback** — a fast signal channel from real users.
- **Contribution (open source)** — users become contributors who improve the product.
- **Belonging/identity** — members identify with a mission or craft.

Most communities serve two or three of these; name the primary. A community without a clear job becomes a dead channel.

## 2. Platform selection

Choose platforms from where the audience already is and the community's job, not from novelty:

- **Discord** — real-time, social, great for developer and creator communities, events, and casual help. Needs active moderation and a clear channel structure.
- **Slack** — real-time, more professional/B2B; weaker for large public communities (history limits, discovery).
- **GitHub** — the home of open-source communities: Issues, Discussions, Pull Requests, and the repo itself. Where contribution happens.
- **Forum (Discourse)** — searchable, async, durable knowledge; better than chat for support that should persist and rank in search.
- **Reddit / X / LinkedIn** — reach and top-of-funnel, less ownership.

Recommend one primary home plus, at most, one or two satellites. Splitting a small community across many platforms kills momentum.

## 3. Open-source community (when relevant)

Design the contributor funnel: **user → engaged user → first-time contributor → repeat contributor → maintainer**. For each step, remove the friction:

- **README** that sells the project and shows value in under a minute.
- **Great docs and DX** — the biggest lever for adoption and contribution. A confusing setup loses contributors silently.
- **CONTRIBUTING.md** — how to set up, run tests, and submit a PR.
- **Good first issues** — a labeled, curated on-ramp of small, well-scoped tasks with context.
- **Issue and PR templates** — so reports and contributions arrive usable.
- **Responsiveness** — a target time-to-first-response on issues and PRs; slow response is the top contributor killer. Even "thanks, we'll look" matters.
- **Recognition** — contributors credited (all-contributors, release notes, shout-outs).
- **Governance and licensing** — a clear license, a CODE_OF_CONDUCT.md, and a lightweight governance/decision model (maintainers, RFCs for big changes) as the project grows.
- **Release cadence and changelog** — visible, regular progress signals the project is alive.

Guide on healthy signals vs. vanity: stars are awareness, not health. Track contributors, repeat contributors, time-to-first-response, time-to-first-contribution, and issue/PR throughput.

## 4. Chat community (Discord/Slack) structure

- **Channel architecture** — a small, legible set: welcome/rules, announcements, general, help/support, show-and-tell, and topic channels only as needed. Start minimal; add channels when a real need emerges, not preemptively.
- **Onboarding** — a clear welcome flow, rules, roles, and a first action for new members (introduce yourself, pick a role, ask a question). The first five minutes decide whether they stay.
- **Roles & permissions** — member, contributor, moderator, team; optional levels/badges for engagement.
- **Rituals** — recurring moments that create habit: office hours, community calls, weekly show-and-tell, AMAs, release parties.
- **Moderation & safety** — a published code of conduct, a moderation team and escalation path, anti-spam measures, and clear enforcement. Safety is the foundation; a toxic channel empties fast.

## 5. Seeding and early growth

A community of zero is the hardest. Seed it: invite existing power users and design partners first, ensure every early message gets a response, and have the team present daily until momentum is self-sustaining. Cross-promote from the product (in-app, docs, README), content, and launch platforms. Do not open a large empty server publicly — a quiet room reads as abandoned.

## 6. Programs that compound

- **Ambassador / champion program** — recognize and empower top members to onboard others, run local/virtual events, and create content.
- **Events** — hackathons, community calls, workshops, contributor sprints, meetups.
- **Content loop** — turn community activity (great questions, showcases, contributions) into content that draws the next members; coordinate with `content-engine`.
- **Recognition systems** — leaderboards, badges, contributor spotlights, swag — tied to the behaviors you want (helping, contributing), not just posting.

## 7. Health metrics

Measure health, not vanity:

- **Activity**: active members (DAU/WAU/MAU of the community), messages/threads, % lurkers vs. participants.
- **Retention**: do new members come back in week 2, week 4?
- **Response**: time-to-first-response on questions/issues; % questions answered.
- **Contribution** (OSS): first-time and repeat contributors, time-to-first-contribution, PR merge rate.
- **Sentiment**: tone, moderation incidents, NPS of members.

Name the two or three that matter most for this community's job and a realistic first-quarter target.

## Segment notes

- **Open-source / developer-led**: GitHub-centric, DX and responsiveness are everything, contributor funnel is the core, Discord for real-time. Community often IS the GTM motion.
- **Enterprise**: a more curated customer community or user group — advisory boards, private Slack, executive roundtables; overlaps heavily with the reference program in `customer-marketing`.
- **Small business / prosumer**: lighter-weight, social, creator-style community; recognition and events drive stickiness.

## Output

Deliver: the community purpose, the platform recommendation with rationale, the structure (channel architecture or contributor funnel + OSS assets like CONTRIBUTING.md / good-first-issues / code of conduct), a seeding and early-growth plan, compounding programs, and a health-metrics dashboard with targets. Draft the concrete assets requested (welcome flow, CONTRIBUTING.md, code of conduct, channel list, event plan). Offer to set up recurring scheduled tasks for community rituals (office hours, community calls). Include a Sources section for any community research. Save the strategy and assets to the project.
