# GoatCounter — dashboard d'estadístiques reutilitzable

Estat: **en funcionament** (2026-10-01). Aquest document explica com està muntat
al projecte guiesbarcelona i com copiar-lo a qualsevol altre projecte Hugo.

## Què hi ha

| Peça | Fitxer | Funció |
|------|--------|--------|
| Dashboard | `static/admin/stats/index.html` | Pàgina privada (`noindex`) amb gràfics i llistats. Llegeix `analytics.json`. |
| Dades | `static/admin/stats/analytics.json` | Generat per l'acció; no és cap credencial. |
| Script | `scripts/build-stats.py` | Consulta l'API de GoatCounter i escriu `analytics.json`. |
| Workflow | `.github/workflows/goatcounter.yml` | Cada 6 hores executa l'script i comiteja el JSON. |
| Tracking | `partials/head.html` | Carrega `gc.zgo.at/count.js` quan `gc_url` està definit i no és local. |

L'espai públic `/estadistiques/` (layout `layouts/estadistiques/list.html`,
config `content/ca/estadistiques/_index.md`) queda **en esborrany** perquè les
estadístiques són privades; la versió que es fa servir és la de `/admin/stats/`.

## Secrets necessaris (GitHub)

A `Settings → Secrets and variables → Actions`:

- `GOATCOUNTER_TOKEN` — token d'API de GoatCounter (Read stats).
- `GOATCOUNTER_SITE` — nom del compte (sense `.goatcounter.com`).

El token **mai** entra al repositori.

## Com reutilitzar-ho en un altre projecte Hugo

1. Copia `scripts/build-stats.py` i `.github/workflows/goatcounter.yml`.
2. Copia `static/admin/stats/` (l'`index.html`; el JSON es regenerarà).
3. Afegeix `gc_url` als paràmetres del lloc i inclou el tag de `head.html`.
4. A `index.html`, edita el bloc de configuració:
   - `siteName` — nom mostrat.
   - `gcUrl` — `https://<compte>.goatcounter.com`.
   - `sectionNames` — noms llegibles per als paths principals.
5. Crea els dos secrets al repositori destí.
6. Executa el workflow manualment un cop per generar el primer `analytics.json`.

No cal tocar res més: el dashboard és autònom i llegeix el JSON del mateix
directori.

## Pendent / millores possibles

- Fer que la configuració es pugui omplir des d'un únic fitxer (en lloc
  d'editar l'HTML) per reduir el pas 4.
- Decidir si mai s'exposa una versió pública (ara és privada per decisió del client).
