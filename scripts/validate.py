#!/usr/bin/env python3
"""Validate the Vital plugin against Claude Code's plugin rules.

Checks the invariants that have broken installs before:
- plugin.json is valid JSON, name is kebab-case, description <= 500 chars
- every agent has valid YAML frontmatter, a 3-50 char kebab-case name,
  a description, a valid color, and (if set) a valid model; names are unique
- every skill dir has a SKILL.md with valid frontmatter (name + description)
- no leftover 'stardust' references

Usage: python3 scripts/validate.py   (exit 0 = ok, 1 = errors, 2 = setup)
Requires: pyyaml  (pip install pyyaml)
"""
import glob
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Run: pip install pyyaml")
    sys.exit(2)

VALID_COLORS = {"red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"}
VALID_MODELS = {"inherit", "sonnet", "opus", "haiku", "fable"}
KEBAB = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

# Run from the repo root regardless of where the script is invoked.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

errors = []


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


# --- plugin.json ---
try:
    pj = json.load(open(".claude-plugin/plugin.json", encoding="utf-8"))
    name = pj.get("name", "")
    if not KEBAB.fullmatch(name):
        errors.append(f"plugin.json: name '{name}' must be kebab-case")
    desc = pj.get("description", "")
    if len(desc) > 500:
        errors.append(f"plugin.json: description is {len(desc)} chars (max 500)")
    if not desc:
        errors.append("plugin.json: missing description")
except Exception as e:  # noqa: BLE001
    errors.append(f"plugin.json: {e}")

# --- agents ---
agent_names = []
for f in sorted(glob.glob("agents/*.md")):
    fm = frontmatter(f)
    if fm is None:
        errors.append(f"{f}: no YAML frontmatter")
        continue
    n = str(fm.get("name", ""))
    agent_names.append(n)
    if not (3 <= len(n) <= 50):
        errors.append(f"{f}: name '{n}' must be 3-50 characters")
    if not KEBAB.fullmatch(n):
        errors.append(f"{f}: name '{n}' must be kebab-case")
    if not fm.get("description"):
        errors.append(f"{f}: missing description")
    color = fm.get("color")
    if color is not None and color not in VALID_COLORS:
        errors.append(f"{f}: color '{color}' invalid (valid: {', '.join(sorted(VALID_COLORS))})")
    model = fm.get("model")
    if model is not None and model not in VALID_MODELS and not str(model).startswith("claude-"):
        errors.append(f"{f}: model '{model}' invalid")
dups = sorted({x for x in agent_names if agent_names.count(x) > 1})
if dups:
    errors.append(f"agents: duplicate names: {', '.join(dups)}")

# --- skills ---
for d in sorted(glob.glob("skills/*/")):
    skill_md = os.path.join(d, "SKILL.md")
    if not os.path.exists(skill_md):
        errors.append(f"{d}: missing SKILL.md")
        continue
    fm = frontmatter(skill_md)
    if fm is None:
        errors.append(f"{skill_md}: no YAML frontmatter")
        continue
    if not fm.get("name"):
        errors.append(f"{skill_md}: missing name")
    if not fm.get("description"):
        errors.append(f"{skill_md}: missing description")

# --- no stardust references in plugin content ---
# Scope to shipped plugin content; the meta files (CONTRIBUTING/AGENTS/this
# script) legitimately name the rule and are excluded.
content_files = (
    glob.glob("agents/**/*", recursive=True)
    + glob.glob("skills/**/*", recursive=True)
    + ["README.md", "CONNECTORS.md", ".mcp.json", ".claude-plugin/plugin.json"]
)
for f in content_files:
    if not os.path.isfile(f):
        continue
    try:
        if "stardust" in open(f, encoding="utf-8", errors="ignore").read().lower():
            errors.append(f"{f}: contains a 'stardust' reference (should reference only impeccable)")
    except Exception:  # noqa: BLE001
        pass

# --- report ---
if errors:
    print("Plugin validation FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

n_agents = len(glob.glob("agents/*.md"))
n_skills = len(glob.glob("skills/*/SKILL.md"))
print(f"Plugin validation passed: {n_agents} agents, {n_skills} skills, all rules OK.")
sys.exit(0)
