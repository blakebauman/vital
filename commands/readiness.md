---
description: Run the pre-launch engineering pass — launch readiness and technical-claim review
argument-hint: "[optional: path or URL to the product, page, or copy to review]"
---

Run Vital's advisory engineering pass before launch. Target: **$ARGUMENTS**
(if blank, review the product in this project plus any launch copy in `.vital/`).

Use the `engineering` agent. It is advisory only — it must not build, fix, or
ship anything. It should:

1. **Read what is being claimed.** Pull the messaging and launch copy from
   `.vital/brand.md`, `.vital/marketing.md`, `.vital/press-kit/`, and any landing
   page in `.vital/design/`, plus the product itself.
2. **Assess launch readiness** — reliability, scale, onboarding, and first-run
   risks, framed as things for the client to check, not as a build backlog.
   Group by severity: blocker, should-fix, nice-to-have.
3. **Review every technical claim** in the messaging and PR. For each: the claim,
   a verdict (defensible / soften / cut), and the reason. Assume a hostile
   technical reader.
4. **Save the review** to `.vital/engineering-review.md` and update
   `.vital/INDEX.md`.

Be specific and honest. Vague reassurance is worse than no review.
