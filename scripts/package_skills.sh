#!/usr/bin/env bash
# Package each skill as its own .zip (skill folder at the top level, as claude.ai requires)
# plus one zip of the whole toolkit. Output goes to dist/.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$ROOT/dist"
rm -rf "$DIST" && mkdir -p "$DIST"

for plugin_skills in "$ROOT"/plugins/*/skills; do
  (
    cd "$plugin_skills"
    for skill in */; do
      skill="${skill%/}"
      zip -qr -X "$DIST/$skill.zip" "$skill" -x '*.DS_Store'
      echo "packaged $skill.zip"
    done
    zip -qr -X "$DIST/all-skills.zip" . -x '*.DS_Store'
  )
done

echo "done -> $DIST"
ls -1 "$DIST"
