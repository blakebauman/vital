---
name: rfp-response
description: >
  Use this skill to clear the enterprise buying gates: RFP responses, security
  questionnaires, and procurement/buyer-enablement materials. Triggers include
  "RFP", "RFI", "security questionnaire", "vendor assessment", "SOC 2", "SSO
  SAML", "DPA", "procurement", "vendor review", "InfoSec review", or preparing
  the documents an enterprise buyer's procurement, security, and legal teams
  require before they can say yes.
metadata:
  version: "0.1.0"
---

Help the client clear the process gates that stall enterprise deals — procurement, security review, and formal RFPs. These are not marketing; they are trust-and-compliance documents that must be accurate. Use for enterprise and upper mid-market motions — see `${CLAUDE_PLUGIN_ROOT}/skills/vital-playbook/references/segments.md`.

> **Accuracy is non-negotiable.** Never state a certification, control, or capability the client does not actually have. Overstating on a security questionnaire is a broken deal (or worse) later. Where the client lacks something, say so and frame the roadmap or compensating control honestly. When a claim is unverified, flag it for the client to confirm — and consider routing technical claims through the `engineering` agent for a credibility check.

## 1. Establish what's being asked

Determine which gate this is:

- **RFP/RFI** — a structured buyer request; win by answering precisely and differentiating within their format.
- **Security questionnaire** (e.g., SIG, CAIQ, custom) — InfoSec due diligence on data handling and controls.
- **Procurement/legal** — MSA, DPA, pricing, terms, vendor onboarding.

Gather the client's real posture: certifications (SOC 2 Type I/II, ISO 27001, HIPAA, GDPR/CCPA readiness), auth (SSO/SAML/SCIM), data handling (encryption at rest/in transit, data residency, retention, subprocessors), architecture (tenancy, backups, DR), and access controls.

## 2. Build a reusable answer bank

Create a structured answer bank the client can reuse across deals: each common question, the approved answer, the evidence/link, and a "status" (yes / roadmap / no). This is the highest-leverage asset — most questionnaires overlap heavily. Deliver it as a spreadsheet (xlsx skill) so the client maintains it.

## 3. Draft the responses

- **RFP**: answer every requirement directly, then differentiate. Mirror the buyer's language and structure. Lead each answer with the direct response, follow with proof, and weave positioning without ignoring the question.
- **Security questionnaire**: answer factually and consistently with the answer bank. For gaps, state the compensating control or roadmap date. Do not leave blanks; do not bluff.
- **Procurement**: prepare the standard artifacts and flag terms likely to need negotiation.

## 4. Buyer-enablement kit

Produce the assets that help the champion sell internally and clear the gates faster:

- **Security one-pager** — certifications, architecture summary, data handling, and where to get the full docs. Route design to `design-brief`.
- **Trust/security overview** — the narrative version for the security team.
- **ROI / business-case one-pager** — for the economic buyer and procurement.
- **Implementation & onboarding overview** — to de-risk adoption for the buyer.

## 5. Close the gaps

List the missing items that block enterprise deals (e.g., no SOC 2 yet, no SSO, no DPA template) with the effort to close each and the interim compensating story. This is advisory — the client remediates; Vital makes sure they see the gap and can speak to it.

## Output

Deliver the reusable answer bank, the drafted RFP/questionnaire responses, the buyer-enablement kit, and the gap list with honest framing. Keep every claim accurate and flag anything the client must verify. Note that Vital advises on these documents but the client owns the accuracy of security and legal representations. Save the answer bank and assets to the project so they compound across deals.
