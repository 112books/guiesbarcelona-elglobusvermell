#!/usr/bin/env bash
# Mostra l'estat dels últims workflows de GitHub Actions (deploy + pa11y).
set -uo pipefail
cd "$(git rev-parse --show-toplevel)"
echo "Branca: $(git branch --show-current) · Commit: $(git rev-parse --short HEAD)"
echo ""
gh run list --limit 8 --json name,headSha,status,conclusion,createdAt \
  --jq '.[] | "\(.name) — \(.headSha[0:7]) — \(.status) \(.conclusion // "")"'
