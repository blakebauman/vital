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

Assertions are derived from each skill's own **Output / Deliverable standards**
section — they check the things the skill *promises* but a naive run usually
omits (an explicit pressure-test, a cited Sources section, the advisory-boundary
disclaimer, a named wedge). That gap is exactly what the with/without-skill
comparison measures.

## The workspace layout (per methodology)

```
evals-workspace/<skill>/iteration-<N>/
  eval-<id>-<slug>/
    with_skill/    outputs/  timing.json  grading.json
    without_skill/ outputs/  timing.json  grading.json
  benchmark.json
```

## Running an iteration

Each run must start from a **clean context** so the agent follows only what the
skill says — spawn an isolated subagent (Claude Code Task) per run.

1. **Scaffold + get the run manifest.**
   ```bash
   python3 scripts/prepare_eval_run.py <skill> --iteration 1     # one skill
   python3 scripts/prepare_eval_run.py --all --iteration 1       # every skill
   ```
   This creates the `with_skill/` and `without_skill/` dirs and prints a JSON
   manifest listing every run to execute (prompt, skill path or none, output dir,
   where to write grading/timing).

2. **Execute each run in an isolated subagent.**
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
   deltas are what it costs.

## The improvement loop

1. Feed failed assertions + human feedback + the current `SKILL.md` to an LLM and
   ask for changes. Generalize fixes; keep the skill lean; explain the *why*.
2. Apply, then rerun into `iteration-<N+1>/`.
3. Aggregate, review, repeat. Stop when feedback is consistently empty or the
   delta stops improving.

## Analysis notes

- Drop assertions that pass in **both** configs — they don't measure skill value.
- Investigate assertions that fail in **both** — broken assertion or too-hard test.
- Study assertions that pass **with** and fail **without** — that's the skill working.
- High variance across runs → ambiguous instructions; tighten with an example.
