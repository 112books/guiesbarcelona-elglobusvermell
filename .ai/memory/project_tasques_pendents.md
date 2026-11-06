---
name: Tasques pendents — guiesbarcelona
description: Resum de tasques resoltes i deute tècnic pendent per al projecte guiesbarcelona.elglobusvermell.org (actualitzat 2026-09-04)
type: project
originSessionId: 646349da-9095-45b2-b4e0-119d25afa37d
---

## Resoltes (sessions 2026-10-23 a 2026-10-26)

- ✅ **Fotos biblioteques aplicades** — 23 biblioteques actualitzades amb fotos de Xavi; 6 sense foto (pendents Xavi)
- ✅ **106 fitxes arquitectes corregides** — script `corregeix-arquitectes-orfes.py`; noms obsolets resolts automàticament
- ✅ **Links Viquipèdia castellà→català** — 4 arquitectes corregits
- ✅ **Mapa fullscreen gestures** — gestureHandling desactivat en fullscreen; pseudo-fullscreen CSS mòbil
- ✅ **fotos_addicionals migrades** — 4 fitxes de format string antic a objecte `{url, autoria, peu}`
- ✅ **autors intervencions: string→relation** — CMS + template backward compat
- ✅ **Dashboard GoatCounter amb filtres de període** — dia/setm./mes/trim./any/tot
- ✅ **Xifres presentació actualitzades** — 6→13 plànols-guia, +650 elements
- ✅ **Pàgina 404 amb cerca en viu** — auto-detecta URL, filtra 658 elements, accents normalitzats
- ✅ **Redireccions WP: privacitat + mapa** — 4 aliases afegits, cobertura 100%
- ✅ **Fix a11y 404 label** — contrast #777→#666 (4.48→5.75:1, WCAG AA)
- ✅ **Skill controlprojecte** — `~/.claude/skills/controlprojecte/` AI-agnòstic
- ✅ **Auditoria servidor** — `.ai/auditoria-servidor.md` complet
- ✅ **Pressupost administració servidor** — 3 opcions, `docs/2026-10-26-pressupost-administracio-servidor.md`

## Resoltes (sessions 2026-08-30 a 2026-09-14)

- ✅ **Informes d'auditoria** — generats (30/8) i actualitzats post-correccions (3/9): accessibilitat 8.5/10, seguretat MODERAT, rendiment 7.5/10, SEO/GEO/AEO 7.5/7/6
- ✅ **PDF informe global** — .ai/informe-global-2026-09-03.pdf amb avís revisió final pendent al domini
- ✅ **Totes les correccions accessibilitat aplicables sense tall de domini** — contrast, carrusel, skip link, aria-current, focus filtres, marcadors Leaflet teclat, formulari accessible, PDFs etiquetats
- ✅ **Contrast placeholder fitxa sense foto** — #aaa → #767676 (WCAG AA, 4.5:1)
- ✅ **Preload imatge LCP** — `<link rel="preload">` a fitxes d'edifici amb foto
- ✅ **genera-dims-imatges.py amb Pillow** — sense dependència ImageMagick; 408 imatges indexades
- ✅ **MAPATGE-URLS.md** — 666 URLs WordPress documentades amb equivalent Hugo; base per a redirects 301 al tall
- ✅ **Mail a Xavi mapatge URLs** — enviat 3/9; explica verificació prèvia al tall + redirects SEO
- ✅ **Mail a Xavi resum setmana** — enviat 4/9; auditories + millores + pendents que depenen d'ell
- ✅ **SRI GoatCounter + Chart.js** — sha384, crossorigin="anonymous"
- ✅ **document.write eliminat** — 6 fitxers admin, substituït per getElementById
- ✅ **Whitelist ?tema=** — mapa.js, valors a/b/c, fallback a 'a'
- ✅ **unsafe=false Goldmark** — HTML en cru mogut a shortcode
- ✅ **robots.txt producció** — Sitemap, Disallow:/admin/, 13 bots IA permesos
- ✅ **llms.txt** — context per a motors d'IA
- ✅ **Schema.org JSON-LD** — corregit safeJS, Person/Organization arquitectes, sameAs social, SpeakableSpecification
- ✅ **SpeakableSpecification ampliat** — inclou .fitxa-dades (dades factuals), condició relaxada (no cal descripció)
- ✅ **hreflang preparat** — .AllTranslations + x-default a head.html; s'activa sol quan EN/ES estiguin al hugo.toml
- ✅ **Captures guia CMS** — imatges oficials GitHub Docs + Sveltia CMS integrades a GUIA-EDITORS.md
- ✅ **WebP fotos carrusel** — fotos_addicionals boqueria convertides (−34/35%); frontmatter actualitzat
- ✅ **og:image 1200×630** — og-default.jpg aprovat per Joan
- ✅ **672 aliases WordPress** — redireccions de les 671 URLs del WP antic
- ✅ **Imatges optimitzades** — 837→144 MB (−83%), màx 1.600px, qualitat 85
- ✅ **width/height <img>** — manifest imatges_dims.json (408 imatges), CLS eliminat
- ✅ **fetchpriority="high" + loading="eager"** — imatge principal LCP
- ✅ **Scripts defer + SRI** — tots els scripts propis
- ✅ **CMS Sveltia** — configurat, mails enviats, PAT clàssic documentat
- ✅ **Autoria git** — 179 commits reescrits a LinuxBCN (filter-branch)
- ✅ **pa11y CI/CD** — workflow actiu i operatiu (10/10 WCAG2AA); fix 10/9: el workflow tenia bug (hugo server sense --environment staging → URLs 404); fix + 4 correccions contrast CSS via color-mix()
- ✅ **Sync automàtic memòria Claude** — scripts/sync-memory.sh (import/export) + hooks SessionStart/Stop a .claude/settings.json; memòria sincronitzada via git per a ús multi-ordinador
- ✅ **Migració tiles CartoDB → Stadia Maps** (14/9) — CartoDB depreca servei raster gratuït; migrat a alidade_smooth/alidade_smooth_dark/outdoors; domain auth sense API key al codi; compte Stadia Maps creat per LinuxBCN

## Pendent — desbloqueig al tall del domini (Dinahosting, ~setembre 2026)

- 🔴 **Google Search Console** — verificar domini TXT + enviar sitemap (just després del tall)
- 🔴 **Bing Webmaster Tools + IndexNow** — indexació ràpida post-tall
- 🔴 **Headers HTTP** — CSP, X-Frame-Options, X-Content-Type-Options, HSTS, Referrer-Policy
- 🔴 **Redirects HTTP 301 reals** — ara meta-refresh Hugo; cal configurar al servidor
- 🔴 **OAuth CMS** — GitHub OAuth App + oauth/index.php (Fase 1)
- 🔴 **analytics.json** — restringir o substituir post-migració
- 🔴 **DMARC/SPF/DKIM** — si s'activa correu SMTP
- 🔴 **envia.php** — auditar o substituir (herència WP, dia del tall)

## Pendent — consens equip (Xavi)

- 🟡 **SSR de llistes** — arquitectes, publicacions, headings al mapa (GEO/SEO)
- 🟡 **FAQ + schema FAQPage** — contingut editorial
- 🟡 **og:image dissenyada** — el placeholder actual (logo sobre blanc) és provisional
- 🟡 **Consistència xifres** portada/Presentació — CONFIRMAT: portada i presentació han de ser idèntiques (feedback 30/9)
- 🟡 **Separació 73 arquitectes combinats** — RESOLT: ho faran manualment des del CMS (confirmació Xavi 30/9). Diccionari normalització també descartada l'automatització.
- ⏳ **Canvi nom "Casa xalet passatge Roserar" → "Casa Mercè Escolano"** — pendent confirmar si ho fan ells o ho apliquem nosaltres
- 🟡 **PDFs guies** — RESOLT: Barceloneta castellà ja existeix; francesos (8) + Marina EN/ES no existeixen (feedback 30/9)
- 🟡 **Paleta definitiva** — pendent que Xavi passi paleta per plànol (lligat a GR1)
- 🟡 **Llicència peu de pàgina** — RESOLT: Creative Commons BY-SA (feedback 30/9)
- 🟡 **Autoria fotos** — RESOLT: nota CC BY-NC a peu de pàgina + nom arxiu/meta amb "elglobusvermell" (feedback 30/9)
- 🟡 **Botó mapa exterior** — RESOLT: Google Maps, un sol botó (feedback 30/9)
- 🟡 **Data tall domini Dinahosting** — RESOLT (relatiu): quan la web estigui llesta, sense data fixa (feedback 30/9)

## Pendent — feedback Xavi 30/9/2026 (nou bloc, disseny i funcionalitat)

Detall complet: `.ai/FEEDBACK-XAVI-2026-09-30.md`

### Decisions prèvies necessàries (Joan ha de respondre a Xavi primer)
- 🔴 **F5** — arquitectes + any al mateix camp de taula: confirmar viabilitat tècnica
- 🔴 **A1** — ordenació arquitectes per cognom: avaluar implicacions (slugs, etc.)
- 🔴 **M3** — pins multicolor (mig/mig o pastís): necessiten paleta per plànol + decisió implementació
- 🔴 **GR3** — tipografia: explorar opcions i proposar a Xavi
- 🔴 **GR1** — colors pins/etiquetes: espera paleta definitiva per plànol de Xavi
- 🔴 **C2** — edició pàgina contacte al CMS: investigar per què no apareix

### Implementació — sense blocants externs
- ✅ **G2** — menú sempre text al desktop (T03, 30/9). Joan discrepa; documentat.
- ✅ **G3** — ordre menú: Presentació · Mapa · En paper · Arquitectes · Contacte (T02, 30/9)
- ✅ **M1** — zoom inicial mapa: padding fitBounds [30,30]→[10,10] (T04, 30/9)
- ✅ **M4** — difuminat eliminat en seleccionar plànol (T05, 30/9). Joan discrepa; documentat.
- ✅ **M6** — eliminar llistat elements + abecedari sota el mapa; mantenir només cercador (6/11)
- ✅ **P5** — eliminar: guia destacada, arquitecte destacat, recursos educatius de portada (ja era feta)
- ✅ **F7** — "edificis" → "elements" aplicat (30/9): 12 ocurrències en 4 fitxers UI. Doc: `.ai/canvis/T01-edificis-elements.md`
- ✅ **PR4** — eliminar bloc "Suggerir un canvi" de la presentació (ja era feta)
- ✅ **A2** — llistat elements arquitecte: eliminar etiqueta any + menys clics (6/11)

### Pendent contingut (espera text de Xavi/equip)
- 🟡 **M5** — informació temes transversals al mapa: contingut de la web antiga (Xavi ho passa)
- 🟡 **PR2** — secció presentació El Globus Vermell: contingut pendent d'ells
- 🟡 **C1** — text formulari contacte: contingut pendent d'ells
- 🟡 **EP4** — descripcions xips temàtics (Èpoques, Usos, Barris, Art): contingut pendent
- 🟡 **EP8** — reordenació plànols guia: decisió interna equip

### Redisseny major (aprofundiment i aprovació primer)
- 🟡 **G1** — layout dues modalitats (sang i dues columnes): mides de columna a determinar
- 🟡 **P1-P8** — redisseny pàgina principal
- 🟡 **F1-F4** — fitxes edificis: layout dues columnes + ordre informació
- 🟡 **EP1-EP7** — redisseny secció "En paper" (carrusel + xips + dues columnes)
- 🟡 **EPI1-EPI3** — redisseny pàgines individuals de cada plànol
- 🟡 **M7** — cercador mapa amb typeahead per arquitecte
- 🟡 **GR2** — vermell → negre/gris fosc (cal aprovació explícita disseny)
- 🟡 **P7** — splash logo mòbil (prototip per confirmar expectativa)

### Futur / documentació
- ⏳ **FU1** — documentar al CMS com crear nous plànols i noves fitxes

## Pendent — petit, aplicable ara

- ⏳ **Revisió final post-tall** — pa11y real + PageSpeed Insights + GSC sobre domini producció
- ⏳ **Invitar comptes GitHub** — confirmar noms d'usuari (Laia, etc.) i convidar (rol Write)
- ⏳ **SpeakableSpecification ampliat a .fitxa-nomenclator** — si es vol cobrir la secció de nomenclàtor dels jardins

## Resoltes (sessió 2026-10-28)

- ✅ **Resposta Jorge rebuda** — port SSH 21100, CPX11 (2vCPU/2GB/40GB+vol), DKIM actiu, credencials a `/root/` servidor
- ✅ **Auditoria servidor completada** — `.ai/auditoria-servidor.md` actualitzat amb totes les dades de Jorge
- ✅ **Pressupost servidor llest** — totes les caselles pendents resoltes; cost VPS ~9,38€/mes documentat
- ✅ **Resposta mail a Jorge redactada** — `.ai/MAILS/2026-10-28-resposta-jorge-servidor.md`

## Pendent — servidor i administració

- 🔴 **El Globus Vermell ha de crear compte Hetzner** — per assumir la propietat del servidor via transfer intern (Customer ID Jorge: K0628817718). Acció del client.
- 🔴 **Llegir credencials del servidor** — `/root/yunohost-elglobus-tech-admin.md` i `/root/2026-10-28-elglobus-users-info.txt` per completar versions programari i comptes correu exactes
- 🔴 **Presentar pressupost al client** — pressupost llest; pendent d'enviar a El Globus Vermell
- 🔴 **Confirmar si la IP canvia en el transfer Hetzner** — probable que sí; caldrà actualitzar registres A (elglobusvermell.org, guiesbarcelona, panel) + revisar MX/SPF al joker.com
- 🔴 **Credencials joker.com a mà** — Joan ha creat compte; cal tenir-les disponibles abans de planificar la finestra de migració
- 🔴 **Migració servidor en standby** — pla acordat (apagar → detach → transfer → reattach → engegar); s'executa quan El Globus Vermell tingui compte Hetzner i accés DNS confirmat

## Pendent — contingut (espera Jorge/Xavi)

- 🔴 **Fotos biblioteques que falten** — Bon Pastor, Canyelles, Les Roquetes, Vall d'Hebron, Vallcarca, Ateneu Barcelonès (mail enviat a Xavi 26/10)
- 🔴 **~50 arquitectes sense fitxa** — Xavi en revisa 80; n'ha creat ~30; els restants poden generar pàgines "fantasma"
- 🔴 **Imatge logo elglobusvermell.org** — espera servidor Jorge

## Why / How to apply

**Why:** El web està a GitHub Pages (staging). Totes les millores aplicables sense domini propi estan fetes (incloses accessibilitat + pa11y CI el 10/9). El desbloqueig és el tall del domini a Dinahosting (~16 set, tornada Xavi). Fins llavors, les úniques tasques pendents sense blocant extern són invitar els comptes GitHub i esperar resposta de Xavi als punts de consens.

**How to apply:** Al proper contacte amb Xavi: confirmar data tall domini + noms d'usuari GitHub + resposta arquitectes combinats. Tota la feina tècnica del tall és una sessió de 2-3h (GSC, Bing, headers, OAuth Fase 1).
