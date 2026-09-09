# CLAUDE.md — El Globus Vermell · Guies de Barcelona

Guia operativa per a Claude Code en aquest projecte.

## El projecte

**Webapp de guies de Barcelona per El Globus Vermell.** Plataforma interactiva de patrimoni arquitectònic amb mapes (OpenStreetMap/Leaflet) i rutes (OpenRouteService). Migrat de WordPress a Hugo. Sense dependències de Google: mapes propis, analítica privada.

- **Producció:** `https://guiesbarcelona.elglobusvermell.org/`
- **Staging:** `https://112books.github.io/guiesbarcelona-elglobusvermell/`
- **Repositori:** GitHub `112books/guiesbarcelona-elglobusvermell`
- **Contacte client:** LinuxBCN — hola@linuxbcn.com

---

## Stack tècnic

| Capa | Tecnologia |
|------|-----------|
| SSG | Hugo 0.159 extended |
| Tema | Custom `guiesbcn-elglobusvermell` |
| Mapes | OpenStreetMap + Leaflet + OpenRouteService |
| Analítica | GoatCounter (privada) |
| Accessibilitat | pa11y-ci (WCAG 2.1 AA) |
| CI/CD | GitHub Actions (deploy, pa11y, stats, verificació) |
| Deploy prod | rsync SSH → servidor LinuxBCN (manual post-validació) |
| Deploy staging | GitHub Actions → GitHub Pages (automàtic) |
| Utilitats | Python 3 (scraping imatges), Bash (scripts editors) |

---

## Entorns

| Entorn | URL | Config |
|--------|-----|--------|
| Local | `http://localhost:1313/` | `config/development/` |
| Staging | `https://112books.github.io/guiesbarcelona-elglobusvermell/` | `config/staging/` |
| Producció | `https://guiesbarcelona.elglobusvermell.org/` | `config/production/` |

---

## Comandos habituals

```bash
# Local
hugo server -D

# Build staging
hugo --minify --environment staging

# Build producció
hugo --minify --environment production

# Publicar (script per a editors, abstrau Git)
./publica-canvis

# Accessibilitat
pa11y-ci --config .pa11yci.json

# Imatges (migració WordPress)
python3 download_images.py
python3 cleanup_logos.py
```

---

## Estructura principal

```
elglobusvermell.org/
├── content/ca/            # Contingut: elements, arquitectes, publicacions
├── config/{entorn}/       # Config Hugo per entorn (baseURL, robots.txt, params)
├── themes/guiesbcn-*/     # Tema Hugo personalitzat
├── static/
│   ├── img/elements/      # Fotos patrimoni (880 MB, excloses de git)
│   ├── pdf/               # Publicacions i guies
│   └── vendor/            # GoatCounter, Chart.js
├── .ai/                   # Documentació interna (arquitectura, decisions)
├── publica-canvis         # Script deploy per a editors
└── .github/workflows/     # deploy-prod, accessibilitat, stats, verifica-numeros
```

⚠️ Excloses de git: `docs/`, `guia-globus-vermell/`, `static/img/elements/Fotos-web-app/`

---

## Convencions

**Commits:** `<type>: <descripció>` (ex: `feat: SpeakableSpec`, `fix(a11y): contrast`)

**Autoria commits:** reescrits a `LinuxBCN <hola@linuxbcn.com>`

**Idioma:** Català (principal) · Anglès i Castellà disponibles però desactivats

**Branca:** `main` (única, protegida) — staging i producció comparteixen branca

---

## Regles operatives

- **pa11y-ci** s'executa a cada commit — PRs no es mergegen si falla WCAG 2.1 AA
- **Deploy producció és manual** (post-validació staging) — staging és automàtic
- `./publica-canvis` és el punt d'entrada per als editors (abstrau tot el Git)
- **SRI** per a GoatCounter i Chart.js — no canviar versions sense actualitzar hashes
- `robots.txt` dinàmic: blocat en dev, públic en staging/producció
- **Schema.org:** JSON-LD a cada element (Organization, Article, Place, BreadcrumbList)

---

## Control horari

Skill actiu: `gestor-hores` — registra automàticament el temps de treball per sessió.

- Logs a `.taques/elglobusvermell.org/YYYY-MM-DD.md` (creat automàticament)
- Comandes: `/time-log [tasca] [hores]`, `/time-report [periode]`, `/time-config [hores] [tarifa]`
- No modificar manualment els fitxers `.taques/` — són append-only
