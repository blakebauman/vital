# The `.vital/` workspace protocol

Every Vital deliverable lives in a `.vital/` directory at the root of the
**client's** project. The workspace is what makes an engagement compound instead
of restarting: the next session and the next specialist build on what already
exists rather than re-deriving it.

Three rules, in order.

## 1. Read before you generate

Before producing anything, read `.vital/INDEX.md` if it exists, then read the
deliverables it lists that your work depends on. At minimum, read
`.vital/positioning.md` — it is the source of truth every other file ladders up
to.

- If a dependency exists, **use it**. Do not re-derive positioning, messaging, or
  ICP that another specialist already set.
- If a dependency is missing, say so and either run the skill that produces it or
  state the assumption you are proceeding on.
- If a dependency is **stale** (see rule 3), reconcile it before building on it.

## 2. Write back, and update the index

Save your deliverable to its canonical path (the workspace table in
`SKILL.md`), then add or update its row in `.vital/INDEX.md`. Create the index if
it does not exist. The format:

```markdown
# Vital engagement index

| Deliverable | Path | Updated | Derived from |
| --- | --- | --- | --- |
| Positioning, ICP, wedge, narrative | `.vital/positioning.md` | 2026-03-04 | — |
| Brand & messaging architecture | `.vital/brand.md` | 2026-03-06 | positioning @ 2026-03-04 |
| GTM plan | `.vital/gtm.md` | 2026-03-07 | positioning @ 2026-03-04 |
```

`Derived from` records the **positioning version your work assumed** — its
`Updated` date at the time you read it. That single column is what makes
staleness detectable.

Use the real current date. Never invent one; if you cannot determine it, write
`unknown` rather than guessing.

## 3. When positioning changes, flag what it invalidates

Specialists are empowered to challenge and override an assumption in the brief.
When that happens and `.vital/positioning.md` changes:

1. Update `.vital/positioning.md` and bump its `Updated` date in the index.
2. Scan the index for any row whose `Derived from` points at the **older**
   positioning date. Those deliverables are now stale.
3. **Tell the client explicitly which files are stale and what changed**, and
   offer to refresh them. Do not silently rewrite downstream work, and do not
   silently leave it contradicting the new positioning.

Staleness is a flag, not an automatic rewrite. The client decides what to
refresh; Vital's job is to make sure they never discover the drift by accident.

## Canonical paths

The full deliverable-to-path table lives in the `vital-playbook` skill. Use those
paths exactly — consistency is what lets the next session find prior work.
