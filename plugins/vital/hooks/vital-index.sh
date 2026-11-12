#!/usr/bin/env bash
# SessionStart hook: if the project has a Vital engagement workspace, put its
# index in context so specialists reuse existing deliverables instead of
# regenerating them. Reads local files under ./.vital only — no network, no
# writes, no environment variables. Silent when there is no workspace.
# Hooks run from the session's project directory, so .vital is relative to it.
[ -d .vital ] || exit 0
echo "Vital engagement workspace found (.vital/). Read the relevant deliverables before generating; write back and update .vital/INDEX.md (protocol: skills/vital-playbook/references/workspace.md in the Vital plugin)."
echo
if [ -f .vital/INDEX.md ]; then
  head -c 8000 .vital/INDEX.md
else
  echo ".vital/INDEX.md is missing — rebuild it from these files before relying on them:"
  find .vital -type f -name '*.md' | sort | head -60 | sed 's|^|- |'
fi
exit 0
