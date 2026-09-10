---
name: Tasques pendents — guiesbarcelona
description: Resum de tasques resoltes i deute tècnic pendent per al projecte guiesbarcelona.elglobusvermell.org (actualitzat 2026-09-04)
type: project
originSessionId: 646349da-9095-45b2-b4e0-119d25afa37d
---

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
- ⏳ **SpeakableSpecification ampliat a .fitxa-nomenclator** — si es vol cobrir la secció de nomenclàtor dels jardins

## Pendent — contingut (espera Jorge/Xavi)

- 🔴 **Confirmació migració contra WP en producció** — el dump és del 16/02; verificar que no hi ha canvis posteriors
- 🔴 **Imatge logo elglobusvermell.org** — espera servidor Jorge
- 🔴 **Fotos fitxes** — les que manquen (biblioteques sense foto, masies, etc.)

## Why / How to apply

**Why:** El web està a GitHub Pages (staging). Totes les millores aplicables sense domini propi estan fetes (incloses accessibilitat + pa11y CI el 10/9). El desbloqueig és el tall del domini a Dinahosting (~16 set, tornada Xavi). Fins llavors, les úniques tasques pendents sense blocant extern són invitar els comptes GitHub i esperar resposta de Xavi als punts de consens.

**How to apply:** Al proper contacte amb Xavi: confirmar data tall domini + noms d'usuari GitHub + resposta arquitectes combinats. Tota la feina tècnica del tall és una sessió de 2-3h (GSC, Bing, headers, OAuth Fase 1).
