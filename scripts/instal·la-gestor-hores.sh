#!/usr/bin/env bash
# instal·la-gestor-hores.sh — instal·la el skill de control horari (gestor-hores)
# a tots els entorns d'agents de la màquina, a partir de la còpia versionada
# al repositori (.agents/skills/gestor-hores).
#
# Ús:
#   scripts/instal·la-gestor-hores.sh             # copia el skill a ~/.agents/skills i ~/.claude/skills
#   scripts/instal·la-gestor-hores.sh --link      # enllaços simbòlics (les actualitzacions del repo es propaguen)
#   scripts/instal·la-gestor-hores.sh --uninstall # treu el skill de les destinacions
#
# Idempotent. No toca els registres d'hores (.taques/), que són dades locals.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if git -C "$SCRIPT_DIR" rev-parse --show-toplevel >/dev/null 2>&1; then
  REPO_ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"
else
  REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
fi

SRC="$REPO_ROOT/.agents/skills/gestor-hores"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "No trobo el skill a $SRC" >&2
  exit 1
fi

MODE="copy"
ACTION="install"
for arg in "$@"; do
  case "$arg" in
    --link) MODE="link" ;;
    --copy) MODE="copy" ;;
    --uninstall) ACTION="uninstall" ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "Opció desconeguda: $arg" >&2; exit 2 ;;
  esac
done

TARGETS=(
  "$HOME/.agents/skills/gestor-hores"
  "$HOME/.claude/skills/gestor-hores"
)

install_one() {
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  if [ "$MODE" = "link" ]; then
    ln -s "$SRC" "$dest"
    echo "  enllaç: $dest -> $SRC"
  else
    mkdir -p "$dest"
    cp -R "$SRC/." "$dest/"
    echo "  còpia:  $dest"
  fi
}

desinstall_one() {
  local dest="$1"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    rm -rf "$dest"
    echo "  eliminat: $dest"
  else
    echo "  ja era fora: $dest"
  fi
}

echo "Skill font: $SRC"
if [ "$ACTION" = "uninstall" ]; then
  for t in "${TARGETS[@]}"; do desinstall_one "$t"; done
else
  for t in "${TARGETS[@]}"; do install_one "$t"; done
fi
echo "Fet. Reinicia l'entorn d'agents perquè torni a carregar el catàleg de skills."
