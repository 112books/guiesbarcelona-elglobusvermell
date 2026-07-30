# Pla: GoatCounter Dashboard com a component Hugo reutilitzable

Creat: 2026-07-16 | Estat: planificació

## Projectes de la família LinuxBCN Analytics

```
LinuxBCN Analytics for GoatCounter (marca paraigua)
├── goatcounter-wp          → Plugin WordPress (existent, publicat)
│   /Users/joan/Documents/Obsidian/goatcounter-wp/
│   Logo: Logotip-wordpress-modul/ (icon-128x128.png, icon-256x256.png)
│
├── goatcounter-dashboard   → Dashboard estàtic standalone (existent)
│   /Users/joan/Documents/Obsidian/goatcounter-dashboard/
│
└── hugo-goatcounter-dashboard  → Hugo Module (NOU — aquest document)
    github.com/112books/hugo-goatcounter-dashboard
    Projecte germà del plugin WordPress, mateixa marca i estètica
```

**Identitat visual:** Logo existent (`icon-128x128.png`, `icon-256x256.png`) reutilitzable per al mòdul Hugo. Estètica IBM Plex Mono + paper càlid + taronja `#d4600a` = identitat LinuxBCN Analytics.

Referència: `/Users/joan/Documents/Obsidian/goatcounter-dashboard/` (projecte base existent)

---

## Objectiu

Convertir el `goatcounter-dashboard` existent en un component Hugo instal·lable a qualsevol projecte amb **un sol fitxer de configuració `.md`**. El token d'API mai toca el repositori (GitHub Secret). El dashboard és idèntic visualment a la versió WordPress (`linuxbcn-analytics-for-goatcounter`).

---

## Arquitectura

```
Projecte Hugo (ex: guiesbarcelona)
│
├── content/ca/estadistiques/_index.md   ← ÚNIC fitxer a tocar per configurar
│     (frontmatter: gc_site, seccions, pw_hash)
│
├── themes/.../layouts/stats/list.html   ← Layout del dashboard (HTML+JS)
│     Adaptat de goatcounter-dashboard/admin/index.html
│     Llegeix CFG injectat per Hugo des del frontmatter
│
├── static/data/analytics.json           ← Generat per GitHub Action (gitignored)
│     Dades de GoatCounter pre-processades
│
└── .github/workflows/goatcounter.yml    ← Fetch diari/horari via GitHub Actions
      Usa GC_API_TOKEN (GitHub Secret, mai al repo)
      Reutilitza scripts/fetch_goatcounter_analytics.py del projecte base
```

### Flux de dades

```
GitHub Action (cada hora)
  → fetch_goatcounter_analytics.py
  → GoatCounter API (amb token secret)
  → static/data/analytics.json  (commit automàtic)
  → GitHub Pages rebuild
  → /ca/estadistiques/ mostra dades actualitzades
```

---

## Fitxer de configuració (l'únic que toca l'usuari)

`content/ca/estadistiques/_index.md`:

```yaml
---
title: Estadístiques
layout: stats

# ── GoatCounter ──────────────────────────────────────────────────────────────
gc_site: guiesbarcelona          # nom del compte (sense .goatcounter.com)
gc_url: https://guiesbarcelona.goatcounter.com

# ── Seccions importants per a aquest projecte ─────────────────────────────────
# Defineix noms llegibles per als paths del teu web
# Si no en poses, el dashboard mostra els paths crus
sections:
  /ca/elements/: "Fitxes d'edificis"
  /ca/: "Portada"
  /ca/en-paper/: "En paper"
  /ca/credits/: "Crèdits"

# ── Protecció per contrasenya ─────────────────────────────────────────────────
# Genera el hash: echo -n "la-teva-contrasenya" | shasum -a 256
# (La contrasenya real MAI al repo — només el hash SHA-256)
pw_hash: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# ── Pàgines destacades per a interpretació automàtica ────────────────────────
# El dashboard generarà insights específics per a aquestes pàgines
highlight_pages:
  - /ca/elements/
  - /ca/
---
```

**Per afegir a un nou projecte Hugo:** còpia aquest fitxer, edita `gc_site`, `gc_url`, `sections` i `pw_hash`. Res més.

---

## Token d'API — seguretat

El token de GoatCounter **mai entra al repositori**. S'afegeix com a GitHub Secret:

```
GitHub repo → Settings → Secrets → Actions → New secret
  Nom:   GC_API_TOKEN
  Valor: (token generat a GoatCounter → Settings → API tokens → Read stats)
```

El GitHub Action l'usa via `${{ secrets.GC_API_TOKEN }}`. El `analytics.json` resultant és dades públiques (estadístiques, no credencials) — és segur comitejar-lo.

---

## Implementació per fases

### Fase 1 — Layout Hugo (adaptar l'HTML existent)

**Fitxer:** `themes/guiesbcn-elglobusvermell/layouts/stats/list.html`

Adaptar `goatcounter-dashboard/admin/index.html`:
- Eliminar el bloc `<script> const CFG = { ... } </script>` hardcoded
- Substituir per valors injectats des del frontmatter Hugo:

```html
{{ define "main" }}
<script>
const CFG = {
  siteName:     {{ .Title | jsonify }},
  gcUrl:        {{ .Params.gc_url | jsonify }},
  pwHash:       {{ .Params.pw_hash | jsonify }},
  dataUrl:      {{ "data/analytics.json" | absURL | jsonify }},
  sectionNames: {{ .Params.sections | jsonify }},
};
</script>
<!-- Tot el CSS i JS de goatcounter-dashboard/admin/index.html aquí -->
{{ end }}
```

El CSS i JS (Chart.js, lògica de login, fetch de dades) s'agafen tal qual del projecte base. Zero reescriptura de lògica.

### Fase 2 — Script Python (adaptar fetch existent)

**Fitxer:** `scripts/fetch-goatcounter.py`

Adaptar `goatcounter-dashboard/scripts/fetch_goatcounter_analytics.py`:
- Llegir config des de `content/ca/estadistiques/_index.md` (frontmatter YAML)
  o des de variables d'entorn (per GitHub Actions)
- Output: `static/data/analytics.json`
- Mantenir el mateix format JSON que ja entén el dashboard HTML

Les dades que recull el script existent (i que cal mantenir):
- Pàgines vistes (per dia/setmana/mes)
- Top pàgines i seccions
- Referrers
- Països
- Navegadors i sistemes operatius
- Dispositius (mòbil/tauleta/escriptori)

Afegir per a guiesbarcelona específicament:
- Edificis més visitats (detectar paths `/ca/elements/*/`)
- Publicació amb més tràfic (agrupar per slug de publicació)

### Fase 3 — GitHub Action

**Fitxer:** `.github/workflows/goatcounter.yml`

```yaml
name: Actualitza estadístiques GoatCounter

on:
  schedule:
    - cron: '0 * * * *'   # cada hora
  workflow_dispatch:        # execució manual

jobs:
  fetch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configura Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Instal·la dependències
        run: pip install requests pyyaml python-frontmatter

      - name: Fetch GoatCounter
        env:
          GC_API_TOKEN: ${{ secrets.GC_API_TOKEN }}
          GC_SITE: guiesbarcelona      # o llegit del frontmatter .md
        run: python scripts/fetch-goatcounter.py

      - name: Commit analytics.json
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add static/data/analytics.json
          git diff --staged --quiet || git commit -m "chore: actualitza estadístiques GoatCounter"
          git push
```

### Fase 4 — Tracking script al web

Afegir a `themes/.../layouts/partials/head.html` (condicionat per entorn):

```html
{{- if not .Site.IsServer }}
<script data-goatcounter="{{ .Site.Params.gc_url }}/count"
        async src="//gc.zgo.at/count.js"></script>
{{- end }}
```

I a `hugo.toml`:
```toml
[params]
  gc_url = "https://guiesbarcelona.goatcounter.com"
```

Nota: `not .Site.IsServer` evita registrar visites locals durant el desenvolupament.

---

## Reusabilitat — com afegir a un altre projecte Hugo

1. Còpia `themes/guiesbcn-elglobusvermell/layouts/stats/list.html` al tema del nou projecte
2. Còpia `scripts/fetch-goatcounter.py` al nou projecte
3. Còpia `.github/workflows/goatcounter.yml` al nou projecte
4. Crea `content/{lang}/estadistiques/_index.md` amb la configuració del projecte
5. Afegeix el GitHub Secret `GC_API_TOKEN` al nou repo
6. Afegeix el tracking script al `head.html`

**Temps estimat per projecte nou: 15 minuts.**

---

## Arquitectura final: Hugo Module

En lloc de copiar fitxers projecte a projecte, el dashboard viu com un **Hugo Module** propi:

```
Repo: github.com/112books/hugo-goatcounter-dashboard
│
├── go.mod                          ← defineix el mòdul
├── layouts/
│   └── stats/
│       └── list.html               ← el dashboard complet (HTML+CSS+JS)
├── assets/
│   └── js/
│       └── goatcounter-map.js      ← tracking d'events del mapa (opcional)
└── README.md
```

### Com s'usa en qualsevol projecte Hugo

**`hugo.toml`:**
```toml
[module]
  [[module.imports]]
    path = "github.com/112books/hugo-goatcounter-dashboard"
```

**`content/ca/estadistiques/_index.md`:** (únic fitxer de config per projecte)
```yaml
---
title: Estadístiques
layout: stats
gc_site: guiesbarcelona
gc_url: https://guiesbarcelona.goatcounter.com
pw_hash: "sha256-de-la-contrasenya"
sections:
  /ca/elements/: "Fitxes d'edificis"
  /ca/: "Portada"
---
```

**Afegir a un nou projecte:** 3 línies a `hugo.toml` + 1 fitxer `.md`. Res més.

---

## Estètica: LinuxBCN Analytics for GoatCounter

El CSS del dashboard existent (`goatcounter-dashboard/admin/index.html`) és la referència definitiva. S'ha de portar tal qual al mòdul Hugo:

```css
:root {
  --bg:      #f5f4f0;   /* paper càlid */
  --ink:     #111110;
  --accent:  #d4600a;   /* taronja LinuxBCN */
  --surface: #eeede9;
}
font-family: 'IBM Plex Mono', monospace;
```

L'aspecte és intencional i diferenciador — **no adaptar al tema del projecte hoste**. El dashboard sempre té l'estètica LinuxBCN Analytics, igual que un plugin de tercers manté la seva identitat.

---

## Tracking d'interaccions del mapa

GoatCounter permet registrar **events personalitzats** (no només pàgines), usant `window.goatcounter.count()`. Per al mapa de guiesbarcelona:

### Events a capturar

```javascript
// Clic a un marcador d'edifici
goatcounter.count({
  path:  'mapa/edifici/' + edificiSlug,
  title: 'Mapa → ' + edificiTitol,
  event: true
});

// Activar/desactivar un filtre de publicació
goatcounter.count({
  path:  'mapa/filtre/' + pubSlug,
  title: 'Filtre → ' + pubTitol,
  event: true
});

// Canvi de proposta de disseny (tema A/B/C)
goatcounter.count({
  path:  'mapa/tema/' + tema,
  event: true
});
```

### Al dashboard, aquests events apareixerien com a secció pròpia:
- "Edificis més clicats al mapa" (top 10)
- "Filtres més usats" (quina publicació interessa més)
- "Proposta de disseny preferida" (A vs B vs C)

Això és informació valuosa per al client: saber quins edificis generen més interès **sense esperar que l'usuari cliqui a la fitxa completa**.

### Implementació al `mapa.js`

Afegir a cada event del mapa (ja existents al codi):
```javascript
// Exemple: dins m.on('click') al mapa.js
if (window.goatcounter && window.goatcounter.count) {
  window.goatcounter.count({
    path: 'mapa/edifici/' + p.url.split('/').filter(Boolean).pop(),
    event: true
  });
}
```

Condicionat a `window.goatcounter` per no trencar en local (on el script no es carrega).

---

## Pendent de decidir

- **Path del dashboard:** `/ca/estadistiques/` (accessible a editors) o `/estadistiques/` (fora de la navegació de l'idioma)?
- **`analytics.json` al repo:** dades públiques (no PII) → comitejar és la opció més simple. Alternativa: GitHub Releases artifact si el fitxer creix molt.
- **Freqüència:** cada hora via GitHub Action és suficient. Temps real exposa el token.
- **Nom del repo del mòdul:** `hugo-goatcounter-dashboard` o `hugo-linuxbcn-analytics`?

---

## Tasques (ordre d'implementació)

Vegeu `TASKS.md` secció **GoatCounter Dashboard** per al seguiment.

1. Crear repo `github.com/112books/hugo-goatcounter-dashboard` amb `go.mod`
2. Portar CSS+JS de `goatcounter-dashboard/admin/index.html` → `layouts/stats/list.html`
   substituint el bloc `CFG` hardcoded per valors Hugo des del frontmatter
3. Adaptar `scripts/fetch_goatcounter_analytics.py` → `scripts/fetch-goatcounter.py`
4. Afegir GitHub Action de fetch horari
5. Afegir events de mapa al `mapa.js` (condicionals a `window.goatcounter`)
6. Afegir tracking script a `head.html` del tema (condicionat: no en `hugo server`)
7. Provar el mòdul en local amb `replace` directive a `go.mod`
8. Publicar mòdul i afegir a guiesbarcelona com a dependència
