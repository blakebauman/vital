#!/usr/bin/env python3
"""Validate the Vital plugin against Claude Code's plugin rules.

Checks the invariants that have broken installs before:
- plugin.json is valid JSON, name is kebab-case, description <= 500 chars
- marketplace.json is valid, lists the plugin, and agrees with plugin.json on version
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
VALID_TOOLS = {
    "Bash", "Edit", "Glob", "Grep", "NotebookEdit", "Read", "Task",
    "TodoWrite", "WebFetch", "WebSearch", "Write",
}
MAX_DESCRIPTION = 1024
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
    pj = {}

# --- marketplace.json ---
# This is what makes `/plugin marketplace add blakebauman/vital` work. Drift
# between it and plugin.json is the failure mode that breaks installs.
try:
    mp = json.load(open(".claude-plugin/marketplace.json", encoding="utf-8"))
    mp_name = mp.get("name", "")
    if not KEBAB.fullmatch(mp_name):
        errors.append(f"marketplace.json: name '{mp_name}' must be kebab-case")
    if not mp.get("owner", {}).get("name"):
        errors.append("marketplace.json: missing owner.name")
    entries = mp.get("plugins") or []
    if not entries:
        errors.append("marketplace.json: plugins must list at least one plugin")
    for entry in entries:
        en = str(entry.get("name", ""))
        if not KEBAB.fullmatch(en):
            errors.append(f"marketplace.json: plugin name '{en}' must be kebab-case")
        if not entry.get("source"):
            errors.append(f"marketplace.json: plugin '{en}' is missing source")
        if en == pj.get("name") and entry.get("version") != pj.get("version"):
            errors.append(
                f"marketplace.json: plugin '{en}' version {entry.get('version')!r} "
                f"does not match plugin.json {pj.get('version')!r}"
            )
    if pj.get("name") and pj["name"] not in [str(e.get("name", "")) for e in entries]:
        errors.append(f"marketplace.json: no entry for plugin '{pj['name']}'")
except Exception as e:  # noqa: BLE001
    errors.append(f"marketplace.json: {e}")

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
    sk_name = str(fm.get("name", ""))
    if not sk_name:
        errors.append(f"{skill_md}: missing name")
    elif sk_name != os.path.basename(d.rstrip("/")):
        errors.append(
            f"{skill_md}: name '{sk_name}' does not match its directory "
            f"'{os.path.basename(d.rstrip('/'))}'"
        )
    if not fm.get("description"):
        errors.append(f"{skill_md}: missing description")
    for tool in [t.strip() for t in str(fm.get("allowed-tools", "")).split(",") if t.strip()]:
        if tool not in VALID_TOOLS:
            errors.append(f"{skill_md}: allowed-tools names unknown tool '{tool}'")

# --- description length ---
# Every agent and skill description is loaded into every session. Long ones are
# both a token cost and, past the harness limit, a truncation risk.
for f in sorted(glob.glob("agents/*.md")) + sorted(glob.glob("skills/*/SKILL.md")):
    fm = frontmatter(f) or {}
    desc = " ".join(str(fm.get("description", "")).split())
    if len(desc) > MAX_DESCRIPTION:
        errors.append(f"{f}: description is {len(desc)} chars (max {MAX_DESCRIPTION})")

# --- reference paths must resolve at runtime ---
# A bare `references/foo.md` is resolved against the *user's* cwd, not the skill
# directory, so it silently fails to load once the plugin is installed. Only
# ${CLAUDE_PLUGIN_ROOT}-prefixed paths are expanded by the harness.
REF_MENTION = re.compile(r"`([^`]*references/[^`]+\.md)`")
for f in sorted(glob.glob("agents/*.md")) + sorted(glob.glob("skills/*/SKILL.md")):
    for path in REF_MENTION.findall(open(f, encoding="utf-8").read()):
        if not path.startswith("${CLAUDE_PLUGIN_ROOT}/"):
            errors.append(
                f"{f}: reference path '{path}' must start with ${{CLAUDE_PLUGIN_ROOT}}/ "
                "or it will not resolve once installed"
            )
            continue
        rel = path[len("${CLAUDE_PLUGIN_ROOT}/"):]
        if not os.path.isfile(rel):
            errors.append(f"{f}: reference path '{path}' points at a missing file")

# --- referenced skills must exist ---
# Catches hand-offs to a skill that was renamed, or to a skill that only exists
# in another host (the pptx/xlsx family). External ones must be declared here so
# the dependency is explicit and the skill text carries a fallback.
EXTERNAL_SKILLS = {"pptx", "xlsx", "dataviz", "my-writing-style", "impeccable"}
local_skills = {os.path.basename(p.rstrip("/")) for p in glob.glob("skills/*/")}
SKILL_MENTION = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`\s+skill")
for f in sorted(glob.glob("agents/*.md")) + sorted(glob.glob("skills/*/SKILL.md")):
    for ref in set(SKILL_MENTION.findall(open(f, encoding="utf-8").read())):
        if ref not in local_skills and ref not in EXTERNAL_SKILLS:
            errors.append(
                f"{f}: references skill '{ref}', which is neither a Vital skill "
                "nor a declared external skill (see EXTERNAL_SKILLS in this script)"
            )

# --- no stardust references in plugin content ---
# Scope to shipped plugin content; the meta files (CONTRIBUTING/AGENTS/this
# script) legitimately name the rule and are excluded.
content_files = (
    glob.glob("agents/**/*", recursive=True)
    + glob.glob("skills/**/*", recursive=True)
    + [
        "README.md",
        "CONNECTORS.md",
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
    ]
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
