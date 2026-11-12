---
name: readiness
description: >
  The advisory pre-launch engineering pass — launch-readiness risks graded by
  severity and a defensible/soften/cut verdict on every technical claim in the
  launch copy. Invoked by the user as /vital:readiness.
argument-hint: "[optional: path or URL to the product, page, or copy to review]"
disable-model-invocation: true
allowed-tools: Read, Glob, Grep, WebFetch, Write
compatibility: >
  Built for the Vital plugin in Claude Code and Cowork, where it runs through the
  read-only engineering agent. Elsewhere it runs inline under the same
  advisory-only rules.
metadata:
  version: "0.2.0"
---

Run Vital's advisory engineering pass before launch. Target: **$ARGUMENTS**
(if blank, review the product in this project plus any launch copy in `.vital/`).

Use the `engineering` agent. If that agent is not available, run the pass
yourself under the same rules. It is advisory only — never build, fix, edit, or
ship product code, even when a fix is obvious or the user asks for one; describe
the fix for the client to make. The only file this pass writes is the review.

1. **Read what is being claimed.** Pull the messaging and launch copy from
   `.vital/brand.md`, `.vital/marketing.md`, `.vital/press-kit/`, and any landing
   page in `.vital/design/`, plus the product itself.
2. **Assess launch readiness** — reliability, scale, onboarding, and first-run
   risks, framed as things for the client to check, not as a build backlog.
   Group by severity: blocker, should-fix, nice-to-have.
3. **Review every technical claim** in the messaging and PR. For each: the claim,
   a verdict (defensible / soften / cut), the reason, and — for soften — the
   honest rewrite. Assume a hostile technical reader. Compliance and
   certification claims (SOC 2, HIPAA, ISO 27001) are defensible only with the
   report or certificate in hand; "in progress" is never "compliant".
4. **Save the review** to `.vital/engineering-review.md` and update
   `.vital/INDEX.md`.

Be specific and honest. Vague reassurance is worse than no review.
