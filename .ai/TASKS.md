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
- ✅ Detecció i llistat de punts desubicats (`.ai/PUNTS-DESUBICATS.md`) — confirmats per Xavi (18 ago): les 5 fitxes ja tenien la coordenada correcta a la base de dades actual, no calia tocar res. **Pendent: aplicar canvi de nom** "Casa xalet passatge Roserar" → "Casa Mercè Escolano" (confirmat per Xavi, encara no aplicat al frontmatter).

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
- ⏳ Separar noms d'arquitectes combinats (73 casos, `.ai/ARQUITECTES-A-SEPARAR.md`) — format de resposta enviat a Xavi (18 ago): `Nom combinat → Nom 1, Nom 2`, una línia per cas. Pendent que Xavi ompli la llista.
- ✅ Normalitzar variants duplicades d'arquitectes: diccionari revisat i corregit segons esmenes de Xavi (18 ago) — `.ai/ARQUITECTES-NORMALITZACIO.yaml`, YAML validat, 14 entrades netes. **Pendent: passada automàtica** per aplicar-lo a `content/ca/elements/*.md` (protocol ja definit a la nota del fitxer).

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

## Accessibilitat i millores d'experiència

- ⏳ **Text a veu (TTS) per a fitxes d'edifici** — permetre escoltar el contingut de la fitxa (prototip Web Speech API ja implementat, pendent decisió Xavi sobre qualitat de veu)
  - Avaluar solucions de programari lliure (Web Speech API nativa del navegador, o eSpeak/Piper si es vol veu pròpia al servidor)
  - Decidir veu: Web Speech API és gratuïta i funciona sense servidor (veus del sistema, pot sonar robòtic); Piper TTS és lliure i permet veu neutra de qualitat
  - Icona de reproducció discreta a la fitxa (play/pause)
  - Valorar quins camps llegir: títol, adreça, any, arquitecte/s, descripció
  - Estimar temps i cost: Web Speech API = 1-2 dies (zero cost); Piper al servidor = 3-5 dies (cost infraestructura)
- ⏳ **Crèdits → Tecnologia**: afegir entrada de la tecnologia TTS un cop confirmada l'opció (Web Speech API o Piper TTS)
- ⏳ **Accessibilitat → Mesures aplicades**: afegir "Lectura en veu alta de les fitxes d'edifici (text a veu)" i "Peu de foto amb text descriptiu (alt text)" un cop confirmada la implementació definitiva
- ⏳ **Accessibilitat → Tecnologia**: afegir la tecnologia TTS usada (Web Speech API del navegador o Piper TTS)
- ⏳ **Fotografies**: confirmar amb Xavi si el símbol © és correcte o si cal una altra forma de crèdit (CC, sense reserva, etc.) — afecta totes les fitxes d'edifici

---

## Infraestructura servidor

- 🔴 Rebre dades de Jorge (host, usuari, ruta, clau SSH)
- ⏳ Còpia del WordPress actual (wp-content + BD)
- ⏳ Pressupostar migració WordPress → Dinahosting
- ⏳ Decidir correu: IMAP propi / Etik / seguir amb Gmail informal
- ⏳ Configurar clau SSH LinuxBCN al servidor de Jorge
- ✅ Clau SSH LinuxBCN generada (~/.ssh/linuxbcn) i pujada a GitHub

---

## Decisions — respostes Xavi (2026-08-17)

Respostes arxivades a `.ai/RESPOSTES-XAVI-2026-08-17.md`

- ✅ Preparar mail de decisions amb totes les preguntes pendents (9 punts en 4 blocs)
- ✅ Enviat a xavirg@elglobusvermell.org el 2026-08-11
- ✅ Respostes rebudes el 2026-08-17 — arxivades a `.ai/RESPOSTES-XAVI-2026-08-17.md`
- ✅ GitHub Xavi: invitació admin a `xavirg` **cancel·lada (2026-08-18)** — resulta ser un compte GitHub alié ("Javi Rodriguez", coincidència de nom d'usuari amb l'email `xavirg@elglobusvermell.org`). Xavi ja tenia accés real amb un altre compte (`xaviglobus`, rol editor/push). Provat pujar `xaviglobus` a admin: no ha estat possible (limitació de GitHub) — **conclusió: no cal rol admin per a les tasques d'edició de continguts de Xavi**, l'accés d'editor ja és suficient.
- ✅ Correu de Xavi (18 ago, 12:26) amb correccions del diccionari d'arquitectes + confirmació punts desubicats — revisat, aplicat i respost (`docs/esborrany-mail-confirmacio-arquitectes-punts-18ago.md`, enviat)
- ✅ Correu de Xavi (18 ago, 12:46) amb dubtes d'accés al CMS ("Javi Rodríguez", login penjat) — respost explicant l'error de compte, ús del PAT i contingut del hub `/admin/` (`docs/esborrany-mail-acces-cms-18ago.md`, enviat)

### Confirmats per Xavi ✅
- ✅ Signatura LinuxBCN al peu del web públic — aprovada per Xavi
- ✅ Citar COAC i Viquipèdia a pàgina de Crèdits — implementat a `content/ca/credits/_index.md` (secció "Fonts de dades")
- ✅ © + CC BY-SA 4.0 simultàniament al peu
- ✅ Nova portada (hero + guia i arquitecte aleatoris)
- ✅ Arquitectes al menú principal
- ✅ Peu de pàgina reorganitzat (Crèdits al peu, Contacte al menú)
- ✅ Formulari de contacte (rep correu)
- ⏳ Configurar enviament formulari per SMTP — Google Workspace o servidor de producció (Dinahosting). Fer al final del projecte, quan el servidor estigui definit. Afegir opció mailto: visible a la pàgina /contacte/ com a alternativa directa.
- ✅ New Babylon/Tàpies: sense punts al mapa, presència a "en paper"/portada
- ✅ Fotos: penjar directament al nou web (sense WordPress)
- ✅ PWA — instal·lar al mòbil: pàgina `static/admin/instal-la-al-mobil/` creada i targeta afegida al hub `/admin/`
- ⏳ Estudiar si exposar les instruccions d'instal·lació al web públic (ara només a /admin/). Podria ser útil per als visitants. Cal decidir on: peu de pàgina, /ajuda/, banner discret... Pendent de decisió.

### Pendents de consens ⏳
- ⏳ Xifres portada: quines xifres concretes (treure anys d'arq. i 2a línia) — Xavi consensuarà amb l'equip
- ⏳ Camp "Projecte" a fitxes: Xavi diu que és redundant, cal confirmació explícita per eliminar-lo
- ⏳ Xavi: revisió llista arquitectes (73 combinats + normalització) — havia dit "aquesta setmana"
- ⏳ Xavi: disseny/colors — consulta amb l'equip
- ⏳ Xavi: criteris arquitectes vs estudis (Eugeni Bach, Soldevila...)
- ⏳ Arxiu Històric BCN: explorar col·laboració per fotos — iniciativa de Xavi, no urgent

---

## Pendents client (preguntes per Xavi / Jorge)

- 🔴 Jorge: dades d'accés al servidor actual
- ⏳ Xavi: confirmar pressupost 3.900€
- ⏳ Xavi: 50% de bestreta per iniciar Flutter
- ✅ Xavi: accés a guiesbarcelona.elglobusvermell.org — ja té accés (rol editor, compte `xaviglobus`); invitació admin errònia cancel·lada, no calia
- ✅ Xavi: clarificació "filtrar per publicacions" al mapa
- ⏳ Xavi: decisió de disseny (colors publicació vs nou rebrand) — consulta amb l'equip
- ⏳ Xavi: confirmar esquema de "En paper" (portada + botó PDF)
- ⏳ Xavi: llicència del peu de pàgina — resolt: © + CC BY-SA 4.0
- ~~⏳ Xavi: confirmar contrasenya admin backoffice~~ — obsolet, ja no hi ha protecció per contrasenya al GitHub Pages de proves (comprovat 18 ago)
