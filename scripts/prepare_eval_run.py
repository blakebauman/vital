#!/usr/bin/env python3
"""Scaffold an eval-run workspace for a skill and emit a run manifest.

Follows the agentskills.io "Evaluating skills" workspace convention:

    evals-workspace/<skill>/iteration-<N>/
      eval-<id>-<slug>/
        with_skill/    run-1/ outputs/  (timing.json, grading.json added later)
                       run-2/ ...
        without_skill/ run-1/ outputs/
      benchmark.json   (added later by aggregate_evals.py)

A single run per config cannot separate signal from run-to-run variance, so
--repeats defaults to 3. Each repeat is an independent isolated subagent on the
same prompt; aggregate_evals.py averages within a config before comparing.

Reads skills/<skill>/evals/evals.json, creates the directory tree for the
given iteration, and prints a JSON manifest of the runs an orchestrator
(the main agent, spawning isolated subagents) must execute — one with_skill
and one without_skill per test case.

Usage:
    python3 scripts/prepare_eval_run.py <skill-name> [--iteration N] [--repeats K]
    python3 scripts/prepare_eval_run.py --all [--iteration N] [--repeats K]
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
WORKSPACE = ROOT / "evals-workspace"


def slug(text: str, words: int = 5) -> str:
    toks = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(toks[:words]) or "case"


def load_evals(skill: str) -> dict:
    path = SKILLS_DIR / skill / "evals" / "evals.json"
    if not path.exists():
        raise FileNotFoundError(f"no evals.json for skill '{skill}' at {path}")
    return json.loads(path.read_text())


def scaffold(skill: str, iteration: int, repeats: int) -> list[dict]:
    data = load_evals(skill)
    iter_dir = WORKSPACE / skill / f"iteration-{iteration}"
    runs = []
    for ev in data["evals"]:
        eid = ev["id"]
        eval_dir = iter_dir / f"eval-{eid}-{slug(ev['prompt'])}"
        for cfg in ("with_skill", "without_skill"):
            for k in range(1, repeats + 1):
                run_dir = eval_dir / cfg / f"run-{k}"
                (run_dir / "outputs").mkdir(parents=True, exist_ok=True)
                runs.append(
                    {
                        "skill": skill,
                        "eval_id": eid,
                        "config": cfg,
                        "repeat": k,
                        "skill_path": str(SKILLS_DIR / skill) if cfg == "with_skill" else None,
                        "prompt": ev["prompt"],
                        "files": ev.get("files", []),
                        "assertions": ev.get("assertions", []),
                        "expected_output": ev.get("expected_output", ""),
                        "output_dir": str(run_dir / "outputs"),
                        "grading_path": str(run_dir / "grading.json"),
                        "timing_path": str(run_dir / "timing.json"),
                    }
                )
    return runs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("skill", nargs="?", help="skill name (or use --all)")
    ap.add_argument("--all", action="store_true", help="scaffold every skill with evals.json")
    ap.add_argument("--iteration", type=int, default=1)
    ap.add_argument(
        "--repeats",
        type=int,
        default=3,
        help="independent runs per config (default 3; 1 cannot separate signal from variance)",
    )
    args = ap.parse_args()
    if args.repeats < 1:
        ap.error("--repeats must be at least 1")

    if args.all:
        skills = sorted(
            p.parent.parent.name
            for p in SKILLS_DIR.glob("*/evals/evals.json")
        )
    elif args.skill:
        skills = [args.skill]
    else:
        ap.error("provide a skill name or --all")

    manifest = []
    for skill in skills:
        manifest.extend(scaffold(skill, args.iteration, args.repeats))

    print(json.dumps({"iteration": args.iteration, "repeats": args.repeats, "run_count": len(manifest), "runs": manifest}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
