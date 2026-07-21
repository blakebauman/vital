---
description: Report where the launch stands — what Vital has produced, what is stale, what is next
allowed-tools: Read, Glob, Grep
---

Report the state of the Vital engagement in this project. Do not generate any new
deliverables — this is a read-only status pass.

1. **Find the workspace.** Read `.vital/INDEX.md`. If it does not exist, glob
   `.vital/**` and reconstruct what you can from the files present; say that the
   index is missing and offer to create it.
2. **Report what exists.** For each deliverable: what it is, its path, when it was
   last updated, and a one-line summary of what it actually says. Keep it scannable.
3. **Report what is stale.** Compare each deliverable's `Derived from` positioning
   version against the current `Updated` date on `.vital/positioning.md`. Anything
   derived from an older version is stale — name it and say what changed in
   positioning that it has not absorbed.
4. **Report what is missing.** Against the default engagement flow in the
   `vital-playbook` skill, name the phases with no deliverable yet.
5. **Name the next step.** One concrete action, the skill or specialist that owns
   it, and why it is next.

If `.vital/` does not exist at all, say so plainly and point at `/vital:launch`
to start an engagement.
