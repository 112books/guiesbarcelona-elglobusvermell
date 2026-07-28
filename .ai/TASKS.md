# TASKS.md — Llista de tasques

Llegenda: ✅ Fet | 🔄 En curs | ⏳ Pendent | 🔴 Bloquejat (espera info externa)

---

## Web guies (guiesbarcelona.elglobusvermell.org)

### Infraestructura
- ✅ Repositori GitHub + deploy automàtic a GitHub Pages
- ✅ Dominis: funcionant a https://112books.github.io/guiesbarcelona-elglobusvermell/
- ⏳ Configurar domini propi guiesbarcelona.elglobusvermell.org a GitHub Pages (espera control del domini)

### Contingut
- ✅ Importació de 66 edificis des del dump SQL (7 publicacions)
- ✅ Pàgina Presentació
- ✅ Pàgina En paper (13 publicacions)
- ✅ Pàgina Crèdits (amb LinuxBCN)
- 🔴 Importació de les 564 entrades del WordPress real (espera accés servidor Jorge)
- 🔴 Imatges dels edificis (espera accés servidor Jorge)
- ⏳ Geocodificació automàtica dels edificis sense coordenades
- ✅ Detecció i llistat de punts desubicats (vegeu `.ai/PUNTS-DESUBICATS.md`)

### Mapa
- ✅ Mapa Leaflet + OpenStreetMap
- ✅ Marcadors amb color per publicació
- ✅ Filtres per publicació (llista plana, activables independentment)
- ✅ Nou comportament del filtre: tots els punts atenuats al iniciar, ressaltar al marcar una publicació
- ✅ Punts en múltiples publicacions: dibuixats amb dos o més cercles de colors
- ⏳ Filtre URL (?pub=gatcpac) per arribar al mapa pre-filtrat des de les fitxes

### Fitxes d'edifici
- ✅ Template single.html amb dades, navegació
- ✅ Enllaços a publicació i arquitecte des de la fitxa (corregit bug d'URL amb subpath)
- ✅ Fitxes sense foto: no es mostra placeholder
- ⏳ **Color de la publicació com a identitat visual de la fitxa** (capçalera o banda lateral del color de la publicació a la qual pertany l'edifici)
- ⏳ Mapa individual a la fitxa (JS carregant, revisar bug de quotes al FITXA_PUNT)
- 🔴 Imatge de l'edifici a la fitxa (espera servidor)
- ⏳ Imatge del plànol-guia a la fitxa

### Arquitectes
- ✅ Taxonomia d'arquitectes activa a Hugo (`config/_default/hugo.toml`)
- ✅ Layouts per a pàgina de llistat i pàgina d'arquitecte individual (amb mapa i llistat d'edificis)
- ✅ Enllaços a arquitectes des de la fitxa d'edifici
- ⏳ Separar noms d'arquitectes combinats (73 casos detectats, vegeu `.ai/ARQUITECTES-A-SEPARAR.md`)
- ⏳ Normalitzar variants duplicades d'arquitectes (esborrany a `.ai/ARQUITECTES-NORMALITZACIO.yaml`)

### Disseny
- ✅ Logo guiesbarcelona al header
- ✅ Sistema de colors per publicació
- ⏳ Decisió paleta definitiva (espera Xavi)
- 🔴 Logo elglobusvermell.org principal (espera servidor Jorge)
- ⏳ Disseny mòbil (revisar responsiu)
- ⏳ Revisar secció "En paper": miniatures per idioma + botons de PDF descarregable
- ✅ Pàgina de cada guia: secció de descàrregues PDF per idioma preparada (es mostra quan hi ha PDFs a `static/pdf/`)

### CMS Editorial (Sveltia CMS) — vegeu `.ai/CMS-PLAN.md`

#### Fase 0 — sense servidor (implementable ara)
- ✅ Script migració TOML→YAML (`scripts/toml-to-yaml.py`)
- ✅ Migrats 70 fitxers d'elements a YAML + build Hugo verificat
- ✅ Crear `static/admin/index.html` + `config.yml` (master: tot)
- ✅ Crear `static/admin-editor/` (editors: només fitxes d'edificis)
- ⏳ Verificar CMS a GitHub Pages amb PAT de prova
- ⏳ Invitar compte GitHub Globus Vermell al repo (rol: Write)
- ⏳ Guia ràpida per a editors: crear PAT i accedir al CMS

#### Fase 1 — OAuth proxy (quan Dinahosting estigui llest)
- 🔴 Crear GitHub OAuth App per a dev (callback → GitHub Pages)
- 🔴 Crear GitHub OAuth App per a prod (callback → Dinahosting)
- 🔴 Crear `oauth/index.php` amb validació CSRF (state param)
- 🔴 Configurar secrets a Dinahosting fora del webroot
- 🔴 Actualitzar `config.yml` amb `base_url` del proxy
- 🔴 Provar flux OAuth complet (dev + prod)

#### Fase 2 — Editorial workflow (quan Sveltia CMS v1.0 — tardor 2026)
- ⏳ Activar `publish_mode: editorial_workflow`
- ⏳ Configurar branca `drafts` per a editors
- ⏳ Revisar rols si Sveltia v1.0 ja els implementa

---

## App mòbil Flutter

- ⏳ Eliminar Firebase del codi Flutter
- 🔴 Nova Google Maps API Key — URGENT, termini setembre 2026 (acció: Xavi crea compte Google Cloud)
- ⏳ Compilar app buida iOS + Android
- ⏳ Decidir arquitectura BD (PostgreSQL / SQLite / altra)
- ⏳ Decidir futur backoffice Node.js
- ⏳ Migrar compte admin Xavi
- ⏳ Llistat d'edificis amb filtres per publicació
- ⏳ Fitxa d'edifici amb mapa
- ⏳ Mapa general amb punts
- ⏳ Clarificar "filtrar per publicacions" al mapa (preguntar Xavi)

### GoatCounter Dashboard — vegeu `.ai/GOATCOUNTER-HUGO-PLAN.md`

- ⏳ Adaptar `goatcounter-dashboard/admin/index.html` → layout Hugo `layouts/stats/list.html`
  (substituir CFG hardcoded per valors del frontmatter del `.md` de configuració)
- ⏳ Adaptar `scripts/fetch_goatcounter_analytics.py` → `scripts/fetch-goatcounter.py`
  (llegir config des del frontmatter, output a `static/data/analytics.json`)
- ⏳ Crear `.github/workflows/goatcounter.yml` (fetch horari + commit automàtic)
- ⏳ Crear `content/ca/estadistiques/_index.md` (fitxer de config del projecte)
- ⏳ Afegir tracking script a `head.html` (condicionat: no en local)
- ⏳ Afegir `GC_API_TOKEN` com a GitHub Secret al repo guiesbarcelona
- ⏳ Decidir path: `/ca/estadistiques/` vs `/admin/stats/`
- ⏳ Documentar procés per reutilitzar en altres projectes Hugo (15 min/projecte)

---

## Infraestructura servidor

- 🔴 Rebre dades de Jorge (host, usuari, ruta, clau SSH)
- ⏳ Còpia del WordPress actual (wp-content + BD)
- ⏳ Pressupostar migració WordPress → Dinahosting
- ⏳ Decidir correu: IMAP propi / Etik / seguir amb Gmail informal
- ⏳ Configurar clau SSH LinuxBCN al servidor de Jorge
- ✅ Clau SSH LinuxBCN generada (~/.ssh/linuxbcn) i pujada a GitHub

---

## Pendents client (preguntes per Xavi / Jorge)

Vegeu `.ai/QUESTIONS-CLIENT.md` per la llista completa.

- 🔴 Jorge: dades d'accés al servidor actual
- ⏳ Xavi: confirmar pressupost 3.900€
- ⏳ Xavi: 50% de bestreta per iniciar Flutter
- ⏳ Xavi: accés a guiesbarcelona.elglobusvermell.org (Xavi diu que ha demanat)
- ✅ Xavi: clarificació "filtrar per publicacions" al mapa (resolt: tots atenuats al iniciar, ressaltar al marcar)
- ⏳ Xavi: decisió de disseny (colors publicació vs nou rebrand)
- ⏳ Xavi: confirmar esquema de "En paper" (portada + botó PDF)
- ⏳ Xavi: separar arquitectes combinats (o demanar que ho fem nosaltres)
- ⏳ Xavi: llicència del peu de pàgina (© o Creative Commons)
- ⏳ Xavi: confirmar contrasenya admin backoffice
