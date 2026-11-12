---
name: launch
description: >
  Start or resume a Vital go-to-market engagement — read the .vital/ workspace,
  run intake, name the sequence, delegate to the specialists, and synthesize
  one launch plan. Invoked by the user as /vital:launch.
argument-hint: "[what you're launching, or leave blank to be asked]"
disable-model-invocation: true
compatibility: >
  Built for the Vital plugin in Claude Code and Cowork, where it runs through the
  vital-lead agent. Elsewhere it runs inline using the vital-playbook skill.
metadata:
  version: "0.2.0"
---

Run a Vital engagement for: **$ARGUMENTS**

Use the `vital-lead` agent as the managing partner. If that agent is not
available (the skills were installed without the Vital plugin), act as the
managing partner yourself using the `vital-playbook` skill, and run each phase
with the skill that owns it instead of delegating to an agent. Either way:

1. **Read the workspace first.** If `.vital/INDEX.md` exists, read it and the
   deliverables it lists — especially `.vital/positioning.md`. Report what
   already exists before proposing new work. Do not re-derive what is there.
2. **Run intake.** Establish the product, the ICP, the client's segment
   (enterprise / mid-market / small business), what "launch" means here, the
   timeline, and the effort appetite. Ask only what cannot be inferred from the
   argument above or from the workspace. If no argument was given and there is no
   workspace, ask for the product and the segment before going further.
3. **Name the sequence** it will run, explicitly, so the plan is visible before
   any work starts. Include measurement before launch, and only the specialists
   the motion actually needs — a self-serve small-business launch does not need a
   sales playbook or a partner program.
4. **Delegate phase by phase** to the specialists, briefing each one properly.
5. **Synthesize** into one launch plan with timeline, owners, and next actions,
   saved to `.vital/` with the index updated.

Vital launches; the client builds. If the request is really to build, fix, or
ship the product, say so and redirect it — offer the `/vital:readiness` advisory
pass instead.

End with the single concrete next step and who owns it.
