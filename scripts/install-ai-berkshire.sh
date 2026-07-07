#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BERKSHIRE="$ROOT/ai-berkshire"
DEST="$ROOT/.cursor/skills"

if [ ! -d "$BERKSHIRE" ]; then
  echo "ai-berkshire not found. Run: git submodule update --init --recursive"
  exit 1
fi

python3 "$BERKSHIRE/scripts/sync-codex-skills.py"
mkdir -p "$DEST"

for skill_dir in "$BERKSHIRE"/codex-skills/*; do
  [ -d "$skill_dir" ] || continue
  name="$(basename "$skill_dir")"
  rm -rf "$DEST/$name"
  cp -R "$skill_dir" "$DEST/$name"
done

chmod +x "$BERKSHIRE"/tools/*.py "$BERKSHIRE"/tools/*.sh 2>/dev/null || true

echo "Installed AI Berkshire skills to $DEST"
