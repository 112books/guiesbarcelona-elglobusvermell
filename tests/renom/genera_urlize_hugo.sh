#!/bin/bash
# Regenera tests/renom/fixtures/urlize_hugo.json: títol d'arquitecte -> carpeta de terme que dona Hugo
# (la ruta real del terme, `Page.RelPermalink`; NO és el mateix que la funció de plantilla `urlize`:
# p. ex. «Arriola & Fiol Arquitectes» -> arriola--fiol-arquitectes, amb %-encoding desfet).
# Ús: bash tests/renom/genera_urlize_hugo.sh [ruta-a-hugo-0.159]   (no s'executa en CI)
# Treballa només en una carpeta temporal: no escriu a content/ del repo.
set -euo pipefail
HUGO="${1:-hugo}"
ARREL="$(cd "$(dirname "$0")/../.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/content" "$TMP/layouts/_default" "$TMP/data"

cat > "$TMP/hugo.toml" <<'T'
baseURL = "https://example.org/"
titleCaseStyle = "none"
disableKinds = ["RSS", "sitemap", "robotsTXT", "404"]
[taxonomies]
  arquitecte = "arquitectes"
T

# Títols dels _index.md reals (llegits amb PyYAML si hi és; si no, amb regex simple).
"${PYTHON:-python3}" - "$ARREL" "$TMP" <<'P'
import glob, json, re, sys
arrel, tmp = sys.argv[1], sys.argv[2]
sys.path.insert(0, arrel + "/scripts")
import renom
titols = []
for f in sorted(glob.glob(arrel + "/content/ca/arquitectes/*/_index.md")):
    titols.append(renom.llegeix_titol(open(f, encoding="utf-8").read()))
# Sondes: caràcters que ara no surten als títols reals però que Sveltia pot deixar escriure.
SONDES = ["Sonda #hash", "Sonda: dos punts", "Sonda d'Apòstrof", "Sonda d\u2019Apòstrof", "Sonda_guio_baix",
          "Sonda! Admira?", "Sonda @ arroba", "Sonda \u2013 guió llarg", "Sonda \u00abangulars\u00bb",
          "Sonda ~ titlla", "Sonda  dos espais", "Sonda - guió", "Sonda 50%", "Sonda [claudàtors]", "Sonda a|b",
          "Sonda a*b;c$d^e", "Sonda =igual", "Sonda \"cometes\"", "SONDA MAJÚSCULES", "Sonda Núñez Ångström",
          "Sonda ends -", "Sonda (parèntesi)", "Sonda 1.2.3", "Sonda\u00a0nbsp", "Sonda ñ ç ü ï l\u00b7l"]
titols.extend(SONDES)
json.dump(titols, open(tmp + "/data/titols.json", "w", encoding="utf-8"), ensure_ascii=False)
# una sola pàgina que cita tots els arquitectes: Hugo en genera els termes
fm = "---\ntitle: Prova\narquitectes: " + json.dumps(titols, ensure_ascii=False) + "\n---\n"
open(tmp + "/content/p.md", "w", encoding="utf-8").write(fm)
P

cat > "$TMP/layouts/index.html" <<'T'
{{ range $k, $tp := site.Taxonomies.arquitectes }}{{ printf "%s\t%s\n" $tp.Page.Title $tp.Page.RelPermalink | safeHTML }}{{ end }}
T
echo '{{ .Title }}' > "$TMP/layouts/_default/single.html"
echo '{{ .Title }}' > "$TMP/layouts/_default/list.html"
echo '{{ .Title }}' > "$TMP/layouts/_default/taxonomy.html"
echo '{{ .Title }}' > "$TMP/layouts/_default/term.html"

"$HUGO" --quiet --source "$TMP" --destination "$TMP/public" >/dev/null

"${PYTHON:-python3}" - "$TMP" "$ARREL" <<'P'
import json, os, sys
from urllib.parse import unquote
tmp, arrel = sys.argv[1], sys.argv[2]
taula = {}
for linia in open(tmp + "/public/index.html", encoding="utf-8").read().splitlines():
    if "\t" in linia:
        t, u = linia.split("\t", 1)
        # RelPermalink és /arquitectes/<carpeta>/ amb %-encoding
        taula[t] = unquote(u).strip("/").split("/")[-1]
carpetes = set(unquote(c) for c in os.listdir(tmp + "/public/arquitectes"))
carpetes.discard("index.html")
# Comprovació creuada: les carpetes de termes que ha generat Hugo són exactament les de la taula
assert carpetes == set(taula.values()), sorted(carpetes ^ set(taula.values()))[:10]
out = arrel + "/tests/renom/fixtures/urlize_hugo.json"
json.dump(taula, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
print(f"{len(taula)} títols -> {out}")
P
