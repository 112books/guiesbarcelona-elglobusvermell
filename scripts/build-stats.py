#!/usr/bin/env python3
"""Fetch GoatCounter stats and write static/admin/stats/analytics.json.

Executat per GitHub Actions (goatcounter.yml) amb les variables d'entorn:
  GC_TOKEN  → token API de GoatCounter (GitHub Secret)
  GC_SITE   → nom del compte (ex: guiesbarcelona)
  DAYS      → dies a incloure (per defecte: 365)
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta, timezone

try:
    import requests
except ImportError:
    print("ERROR: cal instal·lar requests: pip install requests", file=sys.stderr)
    sys.exit(1)

GC_TOKEN = os.environ.get("GC_TOKEN", "")
GC_SITE  = os.environ.get("GC_SITE", "")
DAYS     = int(os.environ.get("DAYS", "365"))
OUT_PATH = "static/admin/stats/analytics.json"

if not GC_TOKEN or not GC_SITE:
    print("WARN: GC_TOKEN o GC_SITE no configurats. S'escriu un fitxer buit.", file=sys.stderr)
    out = {
        "generated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "period": {"start": "", "end": ""},
        "total": 0, "total_unique": 0,
        "hits_by_day": [], "hits": [],
        "by_section": {}, "by_lang": {},
        "browsers": [], "systems": [], "sizes": [], "locations": [], "refs": [],
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2)
    sys.exit(0)

BASE    = f"https://{GC_SITE}.goatcounter.com/api/v0"
HEADERS = {"Authorization": f"Bearer {GC_TOKEN}"}

now   = datetime.now(timezone.utc)
end   = (now - timedelta(days=1)).strftime("%Y-%m-%d")
start = (now - timedelta(days=DAYS)).strftime("%Y-%m-%d")
PARAMS = {"start": start, "end": end, "limit": 200}

LANGS = {"ca", "es", "en", "fr", "de", "it", "pt"}


def _gc_get(endpoint: str, params: dict | None = None) -> dict:
    url = BASE + endpoint
    resp = requests.get(url, headers=HEADERS, params=params or PARAMS, timeout=20)
    resp.raise_for_status()
    return resp.json()


def _norm_stats(stats: list) -> list:
    out = []
    for item in stats:
        name  = item.get("name") or item.get("id") or "Desconegut"
        count = item.get("count", 0)
        if count > 0:
            out.append({"name": name, "id": item.get("id", name), "count": count})
    return sorted(out, key=lambda x: x["count"], reverse=True)


def _extract_section(path: str) -> str:
    if not path:
        return "inici"
    parts = [p for p in path.strip("/").split("/") if p]
    if not parts:
        return "inici"
    idx = 1 if parts[0] in LANGS else 0
    return parts[idx] if idx < len(parts) else "inici"


def safe_fetch(endpoint: str) -> list:
    try:
        data = _gc_get(endpoint)
        return _norm_stats(data.get("stats", []))
    except Exception as exc:
        print(f"WARN: {endpoint} fallat: {exc}", file=sys.stderr)
        return []


# ── Hits per pàgina ───────────────────────────────────────────────────────────
try:
    hits_raw = _gc_get("/stats/hits", {**PARAMS, "limit": 200}).get("hits", [])
except Exception as exc:
    print(f"WARN: hits fetch fallat: {exc}", file=sys.stderr)
    hits_raw = []

by_section: dict[str, int] = {}
total = 0
hits_by_day_map: dict[str, int] = {}
hits_pages: dict[str, int] = {}

for path_item in hits_raw:
    path    = path_item.get("path", "")
    section = _extract_section(path)
    path_total = 0

    for stat in path_item.get("stats", []):
        date  = (stat.get("day") or "")[:10]
        count = stat.get("daily", 0)
        if not count:
            continue
        total += count
        path_total += count
        by_section[section] = by_section.get(section, 0) + count
        if date:
            hits_by_day_map[date] = hits_by_day_map.get(date, 0) + count

    if path_total > 0:
        hits_pages[path] = hits_pages.get(path, 0) + path_total

hits_by_day = [{"date": k, "count": v} for k, v in sorted(hits_by_day_map.items())]
hits_top    = sorted(
    [{"path": k, "count": v} for k, v in hits_pages.items()],
    key=lambda x: x["count"], reverse=True
)[:30]

# ── Estadístiques opcionals ───────────────────────────────────────────────────
browsers  = safe_fetch("/stats/browsers")
systems   = safe_fetch("/stats/systems")
sizes     = safe_fetch("/stats/sizes")
locations = safe_fetch("/stats/locations")
refs      = safe_fetch("/stats/toprefs")

# ── Escriu el fitxer ──────────────────────────────────────────────────────────
analytics = {
    "generated":   datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "period":      {"start": start, "end": end},
    "total":       total,
    "total_unique": 0,
    "hits_by_day": hits_by_day,
    "hits":        hits_top,
    "by_section":  by_section,
    "by_lang":     {},
    "browsers":    browsers,
    "systems":     systems,
    "sizes":       sizes,
    "locations":   locations,
    "refs":        refs,
}

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w") as f:
    json.dump(analytics, f, indent=2)

print(f"analytics.json generat: {total} visites ({start} → {end})")
