---
name: incorporation
description: >
  Use this skill to help a founder incorporate and structure a startup —
  entity choice, Delaware C-corp formation via Stripe Atlas and alternatives,
  EIN, founder equity and vesting, 83(b), cap table basics, and the
  post-incorporation checklist. Triggers include "incorporate", "form a
  company", "Stripe Atlas", "Delaware C-corp", "LLC vs C-corp", "set up my
  startup", "founder equity split", "83(b)", or "registered agent".
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "0.1.0"
---

Help a founder choose a legal structure and incorporate cleanly. Get this right early — fixing a bad structure or equity split after the fact is expensive and sometimes fatal to a raise.

> **Not legal or tax advice.** Vital provides information and frameworks only. Entity, equity, and tax choices are binding and jurisdiction-specific. Tell the founder to have a qualified startup attorney and CPA review before filing, issuing equity, or signing anything. Incorporation services referenced here (Stripe Atlas and others) are not law firms.

## 1. Entity choice

Match the entity to the company's path:

- **Delaware C-corporation** — the default for venture-track startups. Investors (VCs, most angels) expect it; it supports preferred stock, option pools, QSBS eligibility, and clean equity. The right choice if raising institutional capital is likely.
- **LLC** — simpler and cheaper to run, pass-through taxation, flexible. Good for bootstrapped, services, or lifestyle businesses. Most VCs will not invest in an LLC, so it is a poor fit if a priced round is on the horizon (conversion is possible but costly).
- **S-corp** — a tax election (often on an LLC or corp), US-persons-only, limited shareholders; rarely the venture path.

Decide from: likelihood of raising venture capital, number and type of owners, tax situation, and whether founders are US persons. When in doubt for a venture-track startup, the Delaware C-corp is the safe default — but confirm with counsel.

## 2. Incorporation path

For a Delaware C-corp, compare the common formation routes and recommend based on budget, whether the founder is US-based, and how much hand-holding they want. Research current pricing/features before quoting — these change.

- **Stripe Atlas** — ~$500 one-time (+ ~$100/yr Delaware registered agent). Files the Delaware C-corp (or LLC), gets the EIN, issues founder equity with share-purchase agreements, files the **83(b) election**, and provides operating/legal document templates. Bundles startup perks (e.g., Stripe credits and $50k+ partner discounts). Works for founders in 140+ countries. Not a law firm; does not give legal/tax advice or open the bank account for you (guides you to it).
- **Alternatives** — Clerky (lawyer-favored paperwork), Firstbase, Doola, LegalZoom, or a startup attorney doing the formation directly. Note the trade-offs (price, non-resident support, legal review, ongoing compliance).

Present a short recommendation with the reason, not a generic list.

## 3. Founder equity & vesting

- **Equity split** — help founders reason about a fair split (contribution, risk, role, commitment) and warn against reflexive 50/50 without thinking. This is a relationship decision as much as a math one.
- **Vesting** — standard is 4-year vesting with a 1-year cliff, even for founders. It protects the cap table if a co-founder leaves early. Recommend it.
- **83(b) election** — when founders buy restricted stock subject to vesting, filing an 83(b) within **30 days** of the stock issuance can have major tax consequences. This deadline is unforgiving; flag it hard and route to a CPA. (Atlas files this as part of setup.)

## 4. Cap table & equity housekeeping

Explain the starting cap table (founders' shares, authorized vs. issued, par value), the option pool (created when hiring/raising), and why keeping the cap table clean matters for future rounds. Recommend a cap-table tool (e.g., Carta, Pulley, or the formation provider's) once there is more than founder stock. Deliver a simple starting cap-table view if useful (xlsx skill).

## 5. Post-incorporation checklist

Produce the checklist: EIN obtained, bank account opened, founder equity issued and 83(b) filed, IP/assignment agreements signed (founders assign prior work to the company), registered agent active, state/franchise-tax obligations noted (Delaware franchise tax + annual report), accounting set up, and any required foreign-qualification if operating in another state.

## Output

Deliver: an entity recommendation with reasoning, a recommended incorporation path with current pricing and trade-offs (cite sources), founder equity and vesting guidance, the 83(b) deadline flagged, cap-table basics, and the post-incorporation checklist — all with the not-legal/tax-advice boundary stated and a prompt to engage an attorney and CPA. Include a Sources section for any pricing/feature research. Save the plan to the project.
