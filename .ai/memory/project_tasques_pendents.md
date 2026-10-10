---
name: Tasques pendents — guiesbarcelona
description: Resum de tasques resoltes i deute tècnic pendent per al projecte guiesbarcelona.elglobusvermell.org (actualitzat 2026-10-10)
type: project
originSessionId: 646349da-9095-45b2-b4e0-119d25afa37d
## Resposta de Xavi (2026-10-09)

- ✅ **S1 — CMS «Publicacions» (pantalla negra)**: resolt. El camp `select multiple` amb 13 opcions obria el desplegable de tags (un `<dialog>` modal) que en alguns navegadors deixava la pantalla en negre. S'ha afegit `dropdown_threshold: 20` a `static/admin/cms/config.yml` (caselles de selecció, com a «Temes transversals») i s'ha pujat `CMS_CACHE_VERSION`. Verificat amb Chrome headless sobre la configuració real.
- 📄 Documentat el correu a `.ai/RESPOSTES-XAVI-2026-10-09.md` (font literal a `.ai/fonts-xavi/2026-10-09-xavi-resposta-revisio.md`).
- 🔴 **Prioritat**: validar S1 amb Xavi/Joan al navegador real i publicar-ho a staging.
- 🟠 **Temes nous**: S2 (sense faixa de color a les fitxes ni al títol), S3 («En paper» en dues columnes, textos desplegats).
- 🟠 **Portada i disseny**: S9 (redisseny P6: 3 blocs, mapa a sang, peu unificat), S10 (filtre de temes al mapa), S11 (carrusel), S12 (títols «En paper»), S15 (amplada + imatge), S24 (tipografia).
- 🟠 **Errors de traspàs**: S5–S8 (foto de portada a biblioteques, dades dins «projecte», adreça atrapada, sense camp «projecte»). Cal diagnosi abans de tocar.
- 🟡 **Altres**: S13 (color de la «i»), S14 (color parcial B/N), S16 (veu), S17 (anys), S18–S20 (duplicats de migració), S21 (cognom arquitectes), S22 (pins multicolor), S25 (punts amagats clicables), S26 (intervencions), S27 (nom d'arxiu).
- ⏳ **Pendent resposta Xavi**: tipografia (S24), paleta (S23), manual vs automàtic a «projecte» (S6), dubte vinculació arquitectes (S21), tall del domini i usuaris GitHub.

---

## Resoltes (sessió 2026-10-01)

- ✅ **Skill de control horari** versionat al repo + instal·lador `scripts/instal·la-gestor-hores.sh` (global a `~/.agents` i `~/.claude`)
- ✅ **C2 — Contacte i pàgines legals editables al CMS** (Contacte, Accessibilitat, Avís legal, Cookies, Privacitat) + guia de l'editor
- ✅ **Autoria d'arxiu de fotos** — `download="elglobusvermell-<slug>-<n>.<ext>"`
- ✅ **Arquitectes òrfens** — Viaplana i Toyo Ito resolts; 274/274 pàgines amb elements
- ✅ **F5 — Arquitectes + any en un camp**
- ✅ **SpeakableSpecification ampliat a `.fitxa-nomenclator`**
- ✅ **Resum de tasques i temps per a rendibilitat** — `scripts/resum-tasques.py`
- ✅ **GoatCounter** — verificat operatiu i documentat com a reutilitzable (`.ai/GOATCOUNTER-REUTILITZABLE.md`)
- ✅ **Còpia obsoleta del repo eliminada** (3,2 GB) preservant les 205 fotos originals a `originals/`
- ✅ **Pressupost corregit** — 3.900 € = webapp; app Flutter fora de l'abast
- ✅ **Duplicats de migració** — 3 preguntes afegides al tauler de revisió + diagnosi a `.ai/DUPLICATS-MIGRACIO.md`
- ✅ **M2 — mapa en grays** — provat i retirat; pàgina redirigida a `/mapa/`
- ⏳ **Correu MAPATGE-URLS adjunt** — esborrany a `docs/2026-10-01-mail-xavi-mapatge-urls-adjunt.md`; pendent d'enviar
- ⏳ **Tauler de revisió** — actualitzar-lo amb tot ben explicat al final (tasca `tauler-final`)

## Resoltes (sessions 2026-08-30 a 2026-09-04)

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
- 🟡 **Consistència xifres** portada/Presentació (debat obert)
- 🟡 **Separació 73 arquitectes combinats** — Xavi pendent de respondre
- 🟡 **PDFs guies** — francesos (8), castellà/anglès (barceloneta, marina)
- 🟡 **Paleta definitiva** — Xavi debat intern

## Pendent — petit, aplicable ara

- ⏳ **Revisió final post-tall** — pa11y real + PageSpeed Insights + GSC sobre domini producció
- ⏳ **Invitar comptes GitHub** — confirmar noms d'usuari (Laia, etc.) i convidar (rol Write)

## Pendent — contingut (espera Jorge/Xavi)

- 🔴 **Confirmació migració contra WP en producció** — el dump és del 16/02; verificar que no hi ha canvis posteriors
- 🔴 **Imatge logo elglobusvermell.org** — espera servidor Jorge
- 🔴 **Fotos fitxes** — les que manquen (biblioteques sense foto, masies, etc.)

## Why / How to apply

**Why:** El web està a GitHub Pages (staging). El 1/10 s'ha tancat el lot de tasques que no depenien de Xavi. El desbloqueig continua sent el tall del domini a Dinahosting. El **tauler de revisió és el canal únic** amb Xavi: allà hi ha les preguntes i les respostes; els correus només porten adjunts.

**How to apply:** Al proper contacte amb Xavi: confirmar data tall domini + noms d'usuari GitHub + resposta arquitectes combinats. Tota la feina tècnica del tall és una sessió de 2-3h (GSC, Bing, headers, OAuth Fase 1).
