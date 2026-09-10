#!/usr/bin/env bash
# sync-memory.sh — sincronitza la memòria de Claude entre el repo i ~/.claude/projects/
# Ús: sync-memory.sh import | export
#
# import: .ai/memory/ (repo) → ~/.claude/projects/.../memory/
# export: ~/.claude/projects/.../memory/ → .ai/memory/ (repo) + git commit + push

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_MEMORY="$REPO_ROOT/.ai/memory"

# Deriva el path de memòria de Claude a partir de la ruta absoluta del repo
# Ex: /Users/joan/Documents/Obsidian/elglobusvermell.org → -Users-joan-Documents-Obsidian-elglobusvermell-org
ENCODED_PATH="${REPO_ROOT//\//-}"
CLAUDE_MEMORY="$HOME/.claude/projects/${ENCODED_PATH}/memory"

cmd="${1:-}"

case "$cmd" in
  import)
    if [ ! -d "$REPO_MEMORY" ] || [ -z "$(ls -A "$REPO_MEMORY" 2>/dev/null)" ]; then
      exit 0
    fi
    mkdir -p "$CLAUDE_MEMORY"
    rsync -a --delete "$REPO_MEMORY/" "$CLAUDE_MEMORY/"
    ;;

  export)
    if [ ! -d "$CLAUDE_MEMORY" ] || [ -z "$(ls -A "$CLAUDE_MEMORY" 2>/dev/null)" ]; then
      exit 0
    fi
    mkdir -p "$REPO_MEMORY"
    rsync -a --delete "$CLAUDE_MEMORY/" "$REPO_MEMORY/"

    cd "$REPO_ROOT"
    git pull --rebase --quiet 2>/dev/null || true
    if ! git diff --quiet HEAD -- .ai/memory/ 2>/dev/null || git ls-files --others --exclude-standard .ai/memory/ | grep -q .; then
      git add .ai/memory/
      git commit -m "memory: sync automàtic $(date -u +%Y-%m-%dT%H:%MZ)" --quiet
      git push --quiet
    fi
    ;;

  *)
    echo "Ús: $0 import | export" >&2
    exit 1
    ;;
esac
