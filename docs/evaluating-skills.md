# Evaluating Vital's skills

Eval-driven iteration for the skills in this plugin, following the
[agentskills.io methodology](https://agentskills.io/skill-creation/evaluating-skills).
The question each eval answers: **does this skill make Claude produce a
materially better deliverable than Claude with no skill at all?**

## What's tracked vs. generated

- **Tracked (source):** `skills/<name>/evals/evals.json` — the test cases and
  assertions for each skill. Author and commit these.
- **Generated (gitignored):** `evals-workspace/` — run outputs, timings,
  gradings, and benchmarks. Reproducible from the tracked evals, never committed.

## `evals.json` schema

```json
{
  "skill_name": "positioning",
  "evals": [
    {
      "id": 1,
      "prompt": "realistic user message someone would actually type",
      "expected_output": "human-readable description of success",
      "files": ["evals/files/optional-input.csv"],
      "assertions": [
        "Specific, observable, objectively-gradeable statement",
        "Names at least 3 real competitors",
        "Does not contain the words 'innovative', 'seamless', or 'next-generation'"
      ]
    }
  ]
}
```

## Writing assertions that measure something

Assertions test **judgment, not format**. The first version of this suite derived
its assertions from each skill's own Output / Deliverable-standards checklist,
which meant they only asked "did the output contain a section named X." Fifteen
of nineteen skills scored a perfect 1.00 with_skill. At 1.00 an eval is inert: it
cannot detect a regression, and it cannot tell a good deliverable from one that
merely hit its marks.

Bad — a presence check, passes on any output with the right heading:

> "Contains a distinct pressure-test section"

Good — a judgment check, anchored to this prompt's specifics:

> "The pressure test names a counterargument specific to this product's weakness —
> that a browser blocker is trivially circumvented and has near-zero switching
> cost — rather than a generic 'the market is competitive' objection"

Rules for each eval's assertion set:

- **Objectively gradeable** by a judge reading only the output. Never "is insightful".
- **Anchored to prompt specifics** — the named competitors, the stated numbers,
  the declared segment, the user's own stated worry.
- **At least two** an unaided-but-competent Claude would plausibly pass. Without
  these the suite is stacked and the delta is meaningless.
- **At least two** that test what the skill's method uniquely produces and a
  naive run reliably omits.
- Keep the mechanical checks (banned adjectives, no fabricated figures) but do
  not let them dominate the set.

## Adversarial evals

Every skill carries a **id 4 adversarial case**: a prompt where the correct
behaviour is to push back, refuse, or state an uncomfortable truth rather than
produce the deliverable as asked. These test whether a skill's own honesty and
boundary instructions actually fire under pressure — the `press-kit` rule to say
so when a launch is not newsworthy, `rfp-response`'s refusal to claim a
certification the client lacks, `fundraising`'s instruction to route a founder to
`bootstrapping` and stop.

Happy-path evals measure whether a skill produces good work. Adversarial evals
measure whether it does the right thing when the client is asking for the wrong
one — which is where a go-to-market agent does real damage. Each adversarial set
must include at least one assertion that **fails if the model simply complies**.

## The workspace layout (per methodology)

```
evals-workspace/<skill>/iteration-<N>/
  eval-<id>-<slug>/
    with_skill/    run-1/ outputs/  timing.json  grading.json
                   run-2/ ...
                   run-3/ ...
    without_skill/ run-1/ ...
  benchmark.json
```

**Three runs per config, not one.** A single run cannot separate a real delta
from run-to-run variance — and the variance is not small. Between iterations 1
and 2 the `brand-messaging` *without_skill* baseline moved 0.877 to 0.767, even
though the baseline never sees the skill. That 0.11 of noise is larger than
several skills' entire reported delta. `--repeats` defaults to 3 for this reason.

## Running an iteration

Each run must start from a **clean context** so the agent follows only what the
skill says — spawn an isolated subagent (Claude Code Task) per run.

1. **Scaffold + get the run manifest.**
   ```bash
   python3 scripts/prepare_eval_run.py <skill> --iteration 1     # one skill
   python3 scripts/prepare_eval_run.py --all --iteration 1       # every skill
   python3 scripts/prepare_eval_run.py --all --iteration 1 --repeats 5
   ```
   This creates the per-repeat `with_skill/run-K/` and `without_skill/run-K/`
   dirs and prints a JSON manifest listing every run to execute (prompt, skill
   path or none, repeat number, output dir, where to write grading/timing).

2. **Execute each run in an isolated subagent.** Every repeat is an independent
   subagent on the same prompt — never reuse one run's output for another.
   - `with_skill`: give the agent the skill's `SKILL.md` and the prompt.
   - `without_skill`: give the agent only the prompt (the baseline).
   Save the deliverable to the run's `outputs/`, and record
   `timing.json` = `{"total_tokens": N, "duration_ms": N}` (the subagent
   completion notification carries both).

3. **Grade each run against its assertions** → `grading.json`:
   ```json
   {
     "assertion_results": [
       {"text": "Names at least 3 real competitors", "passed": true,
        "evidence": "Names Continue.dev Hub, cursor.directory, Smithery"}
     ],
     "summary": {"passed": 5, "failed": 1, "total": 6, "pass_rate": 0.83}
   }
   ```
   Use an LLM judge for prose assertions; require concrete quoted evidence for a
   PASS. Prefer a script for mechanical checks (word bans, section presence).

4. **Aggregate → `benchmark.json`** and read the delta:
   ```bash
   python3 scripts/aggregate_evals.py evals-workspace/<skill>/iteration-1
   python3 scripts/aggregate_evals.py --all --iteration 1   # + a rollup
   ```
   The `delta.pass_rate` is the payoff: what the skill buys. Tokens/duration
   deltas are what it costs. Each eval row also carries `pass_rate_runs` and
   `pass_rate_spread` per config — **read the spread before believing the
   delta.** A delta of 0.15 with a per-config spread of 0.20 is noise.

## The improvement loop

1. Feed failed assertions + human feedback + the current `SKILL.md` to an LLM and
   ask for changes. Generalize fixes; keep the skill lean; explain the *why*.
2. Apply, then rerun into `iteration-<N+1>/`.
3. Aggregate, review, repeat. Stop when feedback is consistently empty or the
   delta stops improving.

## Analysis notes

- **A with_skill score of 1.00 is a problem, not a win.** It means the suite has
  no headroom left: it can no longer detect a regression, and it cannot tell a
  strong deliverable from an adequate one. When a skill saturates, the fix is
  harder assertions, not a victory lap.
- Read `pass_rate_spread` before `delta`. A delta smaller than the spread has
  not been measured, only observed once.
- Drop assertions that pass in **both** configs — they don't measure skill value.
- Investigate assertions that fail in **both** — broken assertion or too-hard test.
- Study assertions that pass **with** and fail **without** — that's the skill working.
- High variance across runs → ambiguous instructions; tighten with an example.
