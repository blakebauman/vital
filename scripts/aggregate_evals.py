#!/usr/bin/env python3
"""Aggregate graded eval runs into a benchmark.json (with/without-skill delta).

Walks an iteration directory produced by prepare_eval_run.py and, for each
eval, reads every repeat run under with_skill/ and without_skill/ (run-1/,
run-2/, ...), plus the legacy flat layout when no run-* dirs are present.
Computes per-config mean/stddev of pass_rate, tokens, and duration, and the
with-minus-without delta — the number that tells you what the skill buys and
what it costs.

Repeats matter: a single run per config cannot separate a real delta from
run-to-run variance. Each eval row also reports the spread across its repeats,
so a wide spread is visible rather than averaged away.

Grading files follow the agentskills.io schema:
    {"summary": {"passed": N, "failed": M, "total": T, "pass_rate": 0.xx}}

Usage:
    python3 scripts/aggregate_evals.py evals-workspace/<skill>/iteration-<N>
    python3 scripts/aggregate_evals.py --all --iteration N   # every skill, roll up
"""
import argparse
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "evals-workspace"
CONFIGS = ("with_skill", "without_skill")


def _read(path: Path):
    return json.loads(path.read_text()) if path.exists() else None


def _mean(vals):
    vals = [v for v in vals if v is not None]
    return round(statistics.mean(vals), 4) if vals else None


def _stats(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    return {
        "mean": round(statistics.mean(vals), 4),
        "stddev": round(statistics.stdev(vals), 4) if len(vals) > 1 else 0.0,
        "n": len(vals),
    }


def _run_dirs(cfg_dir: Path) -> list[Path]:
    """Repeat dirs for a config, newest layout first, legacy flat as fallback."""
    runs = sorted(p for p in cfg_dir.glob("run-*") if p.is_dir())
    return runs or ([cfg_dir] if cfg_dir.is_dir() else [])


def collect(iter_dir: Path) -> dict:
    per_cfg = {c: {"pass_rate": [], "tokens": [], "duration_ms": []} for c in CONFIGS}
    evals = []
    for eval_dir in sorted(p for p in iter_dir.glob("eval-*") if p.is_dir()):
        row = {"eval": eval_dir.name}
        for cfg in CONFIGS:
            prs, toks, durs = [], [], []
            for run_dir in _run_dirs(eval_dir / cfg):
                grading = _read(run_dir / "grading.json")
                timing = _read(run_dir / "timing.json")
                prs.append((grading or {}).get("summary", {}).get("pass_rate"))
                toks.append((timing or {}).get("total_tokens"))
                durs.append((timing or {}).get("duration_ms"))
            clean = [v for v in prs if v is not None]
            row[cfg] = {
                "pass_rate": round(statistics.mean(clean), 4) if clean else None,
                "pass_rate_runs": prs,
                "pass_rate_spread": round(max(clean) - min(clean), 4) if clean else None,
                "tokens": _mean(toks),
                "duration_ms": _mean(durs),
                "repeats": len(prs),
            }
            # Every repeat feeds the config-level stats, so stddev reflects real
            # run-to-run variance rather than only between-eval variance.
            per_cfg[cfg]["pass_rate"].extend(prs)
            per_cfg[cfg]["tokens"].extend(toks)
            per_cfg[cfg]["duration_ms"].extend(durs)
        evals.append(row)

    run_summary = {}
    for cfg in CONFIGS:
        run_summary[cfg] = {
            "pass_rate": _stats(per_cfg[cfg]["pass_rate"]),
            "tokens": _stats(per_cfg[cfg]["tokens"]),
            "duration_ms": _stats(per_cfg[cfg]["duration_ms"]),
        }

    def delta(metric):
        w = run_summary["with_skill"][metric]
        wo = run_summary["without_skill"][metric]
        if not w or not wo:
            return None
        return round(w["mean"] - wo["mean"], 4)

    return {
        "iteration_dir": str(iter_dir.relative_to(ROOT)),
        "eval_count": len(evals),
        "run_summary": run_summary,
        "delta": {
            "pass_rate": delta("pass_rate"),
            "tokens": delta("tokens"),
            "duration_ms": delta("duration_ms"),
        },
        "evals": evals,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("iteration_dir", nargs="?", help="evals-workspace/<skill>/iteration-<N>")
    ap.add_argument("--all", action="store_true", help="aggregate every skill for --iteration")
    ap.add_argument("--iteration", type=int, default=1)
    args = ap.parse_args()

    if args.all:
        dirs = sorted(WORKSPACE.glob(f"*/iteration-{args.iteration}"))
        rollup = {}
        for d in dirs:
            bench = collect(d)
            (d / "benchmark.json").write_text(json.dumps(bench, indent=2))
            rollup[d.parent.name] = {
                "eval_count": bench["eval_count"],
                "with_skill_pass": (bench["run_summary"]["with_skill"]["pass_rate"] or {}).get("mean"),
                "without_skill_pass": (bench["run_summary"]["without_skill"]["pass_rate"] or {}).get("mean"),
                "delta_pass_rate": bench["delta"]["pass_rate"],
            }
        out = WORKSPACE / f"rollup-iteration-{args.iteration}.json"
        out.write_text(json.dumps(rollup, indent=2))
        print(json.dumps(rollup, indent=2))
        print(f"\nWrote {out.relative_to(ROOT)} and per-skill benchmark.json ({len(dirs)} skills).")
        return 0

    if not args.iteration_dir:
        ap.error("provide an iteration dir or --all")
    iter_dir = Path(args.iteration_dir)
    if not iter_dir.is_absolute():
        iter_dir = ROOT / iter_dir
    bench = collect(iter_dir)
    (iter_dir / "benchmark.json").write_text(json.dumps(bench, indent=2))
    print(json.dumps(bench, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
