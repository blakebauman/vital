#!/usr/bin/env python3
"""Scaffold an eval-run workspace for a skill and emit a run manifest.

Follows the agentskills.io "Evaluating skills" workspace convention:

    evals-workspace/<skill>/iteration-<N>/
      eval-<id>-<slug>/
        with_skill/    outputs/  (timing.json, grading.json added later)
        without_skill/ outputs/
      benchmark.json   (added later by aggregate_evals.py)

Reads skills/<skill>/evals/evals.json, creates the directory tree for the
given iteration, and prints a JSON manifest of the runs an orchestrator
(the main agent, spawning isolated subagents) must execute — one with_skill
and one without_skill per test case.

Usage:
    python3 scripts/prepare_eval_run.py <skill-name> [--iteration N]
    python3 scripts/prepare_eval_run.py --all [--iteration N]
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


def scaffold(skill: str, iteration: int) -> list[dict]:
    data = load_evals(skill)
    iter_dir = WORKSPACE / skill / f"iteration-{iteration}"
    runs = []
    for ev in data["evals"]:
        eid = ev["id"]
        eval_dir = iter_dir / f"eval-{eid}-{slug(ev['prompt'])}"
        for cfg in ("with_skill", "without_skill"):
            (eval_dir / cfg / "outputs").mkdir(parents=True, exist_ok=True)
            runs.append(
                {
                    "skill": skill,
                    "eval_id": eid,
                    "config": cfg,
                    "skill_path": str(SKILLS_DIR / skill) if cfg == "with_skill" else None,
                    "prompt": ev["prompt"],
                    "files": ev.get("files", []),
                    "assertions": ev.get("assertions", []),
                    "expected_output": ev.get("expected_output", ""),
                    "output_dir": str(eval_dir / cfg / "outputs"),
                    "grading_path": str(eval_dir / cfg / "grading.json"),
                    "timing_path": str(eval_dir / cfg / "timing.json"),
                }
            )
    return runs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("skill", nargs="?", help="skill name (or use --all)")
    ap.add_argument("--all", action="store_true", help="scaffold every skill with evals.json")
    ap.add_argument("--iteration", type=int, default=1)
    args = ap.parse_args()

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
        manifest.extend(scaffold(skill, args.iteration))

    print(json.dumps({"iteration": args.iteration, "run_count": len(manifest), "runs": manifest}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
