---
name: abm-playbook
description: >
  Use this skill to build an account-based marketing and go-to-market program
  for named enterprise (and upper mid-market) accounts. Triggers include "ABM",
  "account-based marketing", "target named accounts", "enterprise pipeline",
  "buying committee", "account plan", "land named logos", or coordinating
  marketing and sales against a specific target account list.
metadata:
  version: "0.1.0"
---

Build a focused account-based program that concentrates effort on a small set of high-value accounts and orchestrates marketing and sales against each buying committee. ABM inverts the funnel: pick the accounts first, then generate demand within them. Use for enterprise and upper mid-market motions — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`.

**Workspace.** Read `.vital/INDEX.md` and the deliverables it lists that this work depends on (always `.vital/positioning.md`) before generating; write your output back and update the index. Protocol: `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/workspace.md`.

## 1. Account selection

Define the ideal account profile (firmographics: industry, size, tech stack, triggers) from strategy's ICP, then build a target list. Recommend a deliberately small list per tier — quality over volume. Score accounts on fit (match to profile) and intent (observable buying signals: hiring, funding, tech changes, leadership moves, competitor churn).

## 2. Tiering

Split the list into tiers by value and effort:

- **Tier 1 (1:1)** — highest-value accounts; fully bespoke plays and content per account.
- **Tier 2 (1:few)** — clustered by shared attribute; lightly personalized plays per cluster.
- **Tier 3 (1:many)** — programmatic personalization at scale.

State how many accounts and how much effort each tier gets.

## 3. Buying-committee map

For each Tier 1 account (and archetypally for clusters), map the committee: economic buyer, champion, technical evaluator, end users, and blockers (procurement, security, legal). For each role: what they care about, their success metric, their objection, and the content that moves them. Enterprise deals stall because one unaddressed stakeholder says no — surface them early.

## 4. Plays

Design the plays that engage each account and role: executive outreach, tailored content and landing pages, targeted ads to committee members, events/dinners, customer-reference intros, and sales-marketing coordinated sequences. Tie each play to a committee role and a funnel stage (identify → engage → advance → close → expand).

## 5. Orchestration

Define how marketing and the client's sales motion work as one on each account: shared account plan, agreed signals that trigger sales action, service-level handoffs, and a single view of account status. If the client has no sales team yet, note that ABM assumes founder-led or assisted selling and design for that.

## 6. Content and personalization

List the account/cluster-specific assets to produce (custom one-pagers, ROI models, tailored demos, account-specific landing pages) and route production to `design-brief`. Personalize on the account's actual context (their industry, their stack, their trigger), not just a merged company name.

## 7. Measurement

Recommend account-level metrics, not lead volume: account engagement/coverage (how much of the committee is engaged), pipeline created and influenced, deal velocity, win rate, and expansion. Define what "good" looks like for the first quarter.

## Output

Deliver the account profile, a tiered target list with scoring logic, buying-committee maps for Tier 1, a play library mapped to roles and stages, the marketing-sales orchestration model, the personalized content list, and account-level metrics. Deliver the target list and account plans as a spreadsheet via the `xlsx` skill when available, and as a markdown table otherwise. Save the program to `.vital/abm.md`.
