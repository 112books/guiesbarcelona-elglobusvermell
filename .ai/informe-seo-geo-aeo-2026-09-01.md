# Informe d'auditoria SEO / GEO / AEO — guiesbarcelona.elglobusvermell.org

**Data:** 1 de setembre de 2026 · **Tipus:** auditoria completa
**Entorn auditat:** staging publicat (112books.github.io) + build de producció verificat en local + repositori + WordPress mare de producció

> **Nota (2 set):** els punts CRÍTIC/ALT d'aquest informe ja estan aplicats l'1 de setembre
> (JSON-LD amb `safeJS`, schema Person dels arquitectes amb `sameAs`, redireccions de les 671
> URLs del WP via `aliases`, robots.txt de producció amb `Sitemap:` i `Disallow: /admin/`,
> llms.txt, 404 pròpia, meta descriptions, og:image per defecte i lastmod al sitemap) — vegeu
> l'estat actual a `.ai/TASKS.md`. Aquest document conserva l'estat del web **tal com era al
> moment de l'auditoria**.

| Dimensió | Puntuació | Estat | Conclusió clau |
|---|---|---|---|
| SEO | 6/10 | On Track | Base tècnica correcta però bloquejada pel tall del domini; JSON-LD invàlid a tot el web |
| GEO | 5/10 | Needs Work | Contingut citable excel·lent però invisible als bots d'IA i amb dada estructurada trencada |
| AEO | 5/10 | Needs Work | Sense FAQ, sense paràgrafs de resposta directa ni schema FAQPage; el TTS és un punt únic |
| **Combinat** | **16/30** | | **El tall del domini és el desbloquejador únic: tota la resta ja té base per sobre de la mitjana** |

## Resum executiu

El web Hugo de Guies de Barcelona té una base tècnica sana — entorns separats amb noindex a
staging, canonicals, Open Graph i sitemap correctes al build de producció (verificat en local),
URLs netes i un contingut únic — però avui és completament invisible a Google i als motors
d'IA: el domini de producció encara serveix el WordPress antic i el Hugo viu, per disseny,
noindex a github.io. A sobre, tres problemes travessen tot el web: la dada estructurada (JSON-LD)
és invàlida per un bug d'escapament de cometes, el robots.txt de producció és minimal (sense
directiva Sitemap ni protecció d'/admin/), i les pàgines centrals (mapa, arquitectes, llistats
de publicacions) es renderitzen només amb JavaScript, sense headings ni enllaços al HTML servit.
L'oportunitat és clara: amb el tall del domini ben fet — build de producció, DNS i redireccions
de les 671 URLs del WordPress — i tres correccions de baix cost, el contingut de les guies de
camp té tot el potencial de posicionar-se a Google i de ser citat pels motors generatius.

## Pàgines auditades

| URL | Tipus | Observacions |
|---|---|---|
| `/` | Portada | Stats noves (659/13/274/1928–2026); seccions destacades buides al HTML cru (JS) |
| `/mapa/` | Hub principal | Cap heading al HTML servit; títol redundant amb doble marca; destí del redirect mòbil |
| `/presentacio/` | Sobre el projecte | Text propi; xifres inconsistents amb la portada (11 Mapes / 660 Punts / 98 anys) |
| `/en-paper/` | Índex publicacions | Llistat de plànols-guia; estat de cadascun |
| `/credits/` | Crèdits | E-E-A-T sòlid: noms, rols, CC BY-SA 4.0, fonts COAC/Viquipèdia, suport Ajuntament |
| `/contacte/` | Contacte | Email + formulari públic de correccions (trust + participació) |
| `/arquitectes/` | Hub arquitectes | Llistes només via JS; dades encastades com `window.MAPA_PUNTS` / `TOTS_ELEMENTS` |
| `/arquitectes/marino-canosa/` | Fitxa arquitecte | Quasi buida (nom + «Arquitecte»); mateix patró a les 79 pàgines de terme sense fitxa curada |
| `/publicacions/interiors-illa/` | Publicació | Forta: 1.500+ paraules, densitat factual, bibliografia enllaçada, PDFs en 4 idiomes |
| `/elements/mercat-de-la-boqueria/` | Fitxa element | Data-only, sense descripció (38% de les fitxes igual) |
| `/elements/casa-roca-barallat/` | Fitxa element | Amb foto (og:image present al build de producció) |
| `/elements/flors-de-la-rambla/` | Fitxa element | Publicada el 31/8 (mercat no-alimentari); verificada en línia |
| `/admin/` | Hub intern | HTTP 200 públic però amb meta noindex,nofollow; analytics.json crawleable |
| `/legal/*` | Legal (3 pàg.) | RGPD exemplar: analytics sense cookies (GoatCounter) |
| `/accessibilitat/`, `/llicencia/` | Meta | Declaracions d'accessibilitat i llicència |
| `robots.txt` | Crawl | Staging bloqueja tots els bots (incl. IA); producció: `Allow: /` i res més |
| `sitemap.xml` | Índex | 964 URLs (661 elements + 277 arquitectes + 14 publicacions); lastmod a 6 |
| `/index.xml` | RSS | Actiu i correcte |
| `/llms.txt` | GEO | 404 — no existeix |
| WP mare (producció) | Referència | 671 URLs al post-sitemap — abast de les redireccions del tall |
| Builds locals | Verificació | staging + producció + sense minify: OG/canonical/robots/sitemap per entorn |

## Anàlisi SEO — 6/10

Base tècnica per sobre de la mitjana i coherent entre entorns; els punts febles són la dada
estructurada trencada, les pàgines renderitzades només amb JS i la manca de senyals de frescor.

### Tècnic on-page

| Senyal | Troballa | Estat |
|---|---|---|
| Title tag | Format consistent «Pàgina — Guies de Barcelona de El Globus Vermell»; la portada només porta la marca (38 car.) i el mapa en repeteix dues («Guies Barcelona — El Globus Vermell — Guies de Barcelona…»). | Atenció |
| Meta description | Present a totes les pàgines via fallback global (155 car.), però genèrica a les pàgines hub; només 346 de 660 fitxes tenen descripció pròpia. | Atenció |
| Jerarquia de headings | H1 únic a fitxes i publicacions; el `/mapa/` — la pàgina on aterren els mòbils — no té cap heading al HTML servit (tot JS). | Atenció |
| URLs | Netes i semàntiques (`/elements/slug/`); algun artefacte aïllat («mariano-romano-rius-» amb guió final). | Bé |
| Canonical | Self-referencing per entorn, verificat als builds de staging i producció. | Bé |
| Robots meta | Staging 100% noindex (correcte per disseny); producció indexable. | Bé |
| Viewport | Present i correcte. | Bé |
| Alt d'imatges | Carrussel amb alt descriptiu («Mercat de la Boqueria (1/3)») i peu amb crèdit CC BY-SA. | Bé |
| Enllaços interns | Graf fluix: hubs (arquitectes, publicacions) no enllacen les fitxes al HTML servit — les llistes són JS; les fitxes sí enllacen arquitectes i veïns (prev/next). | Atenció |
| Open Graph / Twitter | Completa al build de producció (og:type/url/title/description/site_name/locale + twitter:card), però `defaultOgImage` és buit: sense og:image a ~315 fitxes sense foto i a totes les pàgines hub. | Atenció |

### Qualitat del contingut

| Senyal | Troballa | Estat |
|---|---|---|
| Volum | Publicacions de plànol-guia excel·lents (interiors-illa: 1.500+ paraules); fitxes desiguals — 62% amb text, 38% data-only (la Boqueria no té descripció). | Atenció |
| Senyals de frescor | lastmod només a 6 de 964 URLs del sitemap (2026-07-09); cap data visible a les pàgines. | Atenció |
| Llegibilitat | Text amb H2 per seccions, paràgrafs curts i llistes; estructura de fitxa clara i repetible. | Bé |
| Coherència de dades | Portada: 659 edificis / 13 guies; Presentació: 660 Punts / 11 Mapes / 98 anys — inconsistència ja en debat d'equip. | Atenció |

### Dada estructurada i índex

| Senyal | Troballa | Estat |
|---|---|---|
| JSON-LD (WebSite + LandmarksOrHistoricalBuildings) | **INVÀLID a tot el web i als dos entorns**: la sortida de `jsonify` s'escapa dins el context JS del template (`"name": "\"Guies de Barcelona…\""`) — reproduït sense minify, donc és l'auto-escaping de Go html/template, no el minificador. Fix: `\| safeJS` a tots els jsonify de `schema.html` (~30 min). Rich results perduts mentre no es corregeixi. | Falta |
| Sitemap | 964 URLs correctes per entorn; fitxer únic; sense lastmod generalitzat i sense prioritats. | Atenció |
| robots.txt | Correctament separat per entorns; el de producció és minimal: cap directiva `Sitemap:` i cap `Disallow: /admin/` (l'hub i analytics.json són crawleables, tot i el noindex meta). | Atenció |
| 404 | Retorna HTTP 404 correcte, però sense pàgina pròpia — GitHub Pages serveix la genèrica anglesa. | Atenció |
| RSS | `/index.xml` actiu, amb el mateix títol i descripció per entrada. | Bé |

## Anàlisi GEO — 5/10

GEO és optimitzar per als motors generatius (Perplexity, ChatGPT Search, AI Overviews de
Google): les IA trien i citen fonts clares, factuals i amb autoritat. El contingut és el punt
fort del web; l'accés dels crawlers d'IA és el punt feble.

### E-E-A-T

| Senyal | Troballa | Estat |
|---|---|---|
| Autoria i organització | Crèdits amb noms i rols (Jorge Vitoria — edició 2006, Joan Martínez/LinuxBCN — redisseny, La Correccional — revisió, Vicenç Benéitez — revisió històrica), suport de l'Ajuntament de Barcelona i CC BY-SA 4.0. | Bé |
| Contacte | Email actiu + formulari públic de correccions — senyal de confiança i de manteniment viu. | Bé |
| Confiança / privacitat | RGPD exemplar: analytics sense cookies (GoatCounter), política clara; no hi ha telèfon ni adreça física (acceptable per a un projecte editorial). | Bé |
| Equip editorial | «Edició: El Globus Vermell» com a col·lectiu; els noms de l'equip actual no hi són (la fitxa d'arquitecte no enllaça fonts pròpies — ex. Marino Canosa sense COAC/Viquipèdia, tot i que altres en tenen). | Atenció |

### Contingut per a la síntesi d'IA

| Senyal | Troballa | Estat |
|---|---|---|
| Densitat factual | Les pàgines de publicació són plenes de dades citables: «16.000 hab/km²», «6 m² de verd per habitant», «70+ jardins interiors», «150.000 m² recuperats» — material ideal perquè una IA citi la font. | Bé |
| Fonts externes | Bibliografia enllaçada (aladi.diba.cat), referències COAC i Viquipèdia a crèdits i fitxes amb enllaços. | Bé |
| Claredat d'entitat | Marca consistent (El Globus Vermell + guiesbarcelona.elglobusvermell.org) i publisher declarat al schema — un cop corregit el JSON-LD. | Bé |
| Originalitat / POV | Guies de camp pròpies amb veu editorial (Cerdà, superilles, patrimoni obrer) — contingut que cap altre web té. | Bé |
| Completitud | 79 de les 274 pàgines d'arquitecte sense contingut propi (les altres 195 tenen biografia i enllaços) i llistes renderitzades només client-side: les IA poden llegir les dades encastades (`window.MAPA_PUNTS`) però no el contingut estructurat final. | Falta |

### Accés dels crawlers d'IA

Staging bloqueja explícitament GPTBot, ClaudeBot, PerplexityBot, CCBot, Google-Extended i
companyia (correcte mentre no hi hagi tall); el robots.txt de producció encara no defineix
política per a bots d'IA. — **Falta**

### GEO tècnic

| Senyal | Troballa | Estat |
|---|---|---|
| HTTPS / rendiment | Lloc estàtic ràpid i segur; pendent: convertir les imatges (880 MB de PNG) a WebP (ja detectat a l'informe de rendiment del 30/8). | Bé |
| Profunditat de schema | JSON-LD invàlid (mateix bug arreu); sense Person per als arquitectes ni Author per a publicacions. | Falta |
| llms.txt | No existeix (404). Un resum curat del web en Markdown per a LLMs seria un actiu barat i diferenciador. | Falta |
| Graf d'entitat | Cap enllaç a perfils socials de l'entitat des del web (enfortiria el reconeixement d'entitat dels motors generatius). | Atenció |

## Anàlisi AEO — 5/10

AEO és optimitzar per als motors de resposta: featured snippets, People Also Ask i cerca per
veu. La regla d'or: la resposta a la pregunta de l'usuari, en un paràgraf de 40–60 paraules,
sota un heading en forma de pregunta.

### Elegibilitat per a featured snippets

| Senyal | Troballa | Estat |
|---|---|---|
| Paràgrafs de resposta directa | Les 346 fitxes amb descripció poden generar snippet; el 38% restant (la Boqueria inclosa) són data-only: responen «qui va construir X i quan» amb dades però sense paràgraf extractible. | Atenció |
| Patrons de definició | Definicions implícites a les publicacions (Cerdà, l'Eixample, les superilles), però no sistemàtiques ni al principi de pàgina. | Atenció |
| Llistes i taules | Les llistes principals (elements, publicacions, arquitectes) no existeixen al HTML servit (JS); les descàrregues PDF de les publicacions sí que són enllaços SSR. | Atenció |

### Formats de resposta estructurats

| Senyal | Troballa | Estat |
|---|---|---|
| FAQ | Cap pàgina de FAQ ni schema FAQPage al web. El formulari públic de correccions ja genera preguntes reals dels lectors que podrien alimentar una FAQ curada. | Falta |
| Headings en forma de pregunta | Cap H2/H3 amb «Com…? / Què…? / Per què…?» a cap pàgina auditada. | Falta |
| Speakable | Sense SpeakableSpecification; el TTS «Escoltar» ja marca les seccions llegibles — seria directe mapar-ho a schema. | Falta |

### Preparació per a cerca per veu

| Senyal | Troballa | Estat |
|---|---|---|
| Llenguatge conversacional + TTS | Texts en català natural i funció «Escoltar» (text-to-speech) a les fitxes — una raresa absoluta al sector, alineada amb la decisió 7a de l'enquesta interna. | Bé |
| Preguntes long-tail | «Qui va construir X» queda cobert per les dades de la fitxa; preguntes com «quin és l'edifici més antic de…» no les cobreix cap pàgina. | Atenció |
| Senyals locals (NAP) | Projecte editorial, no negoci local: no hi ha NAP que preservar; l'email i el formulari fan el paper. | N/A |

## El tall del domini — pas a pas

**Prerequisit:** validació de l'equip (Xavi torna cap al 16 de setembre) — la data la decideix
l'equip. Avui el domini de producció serveix el WordPress antic a Hetzner (195.201.2.76) i el
Hugo viu, noindex per disseny, a 112books.github.io. Ordre recomanat, tot en una mateixa
finestra de treball:

1. **Domini personalitzat al GitHub Pages.** Al repo: Settings → Pages → Custom domain:
   `guiesbarcelona.elglobusvermell.org` (+ `www.guiesbarcelona.elglobusvermell.org`). Això crea
   el fitxer CNAME al repo. Un cop el DNS resolgui, activar «Enforce HTTPS» (el certificat
   Let's Encrypt triga entre 15 minuts i 24 h).
2. **DNS al registre d'elglobusvermell.org.** Ara el subdomini apunta al Hetzner del WP. Cal:
   `CNAME guiesbarcelona → 112books.github.io` i `CNAME www.guiesbarcelona →
   112books.github.io` (és subdomini, el CNAME és vàlid). Verificar qui gestiona el DNS del
   domini arrel (Jorge) i coordinar-ho amb ell.
3. **Build de producció.** Canviar al workflow `.github/workflows/deploy-prod.yml` la línia
   `hugo --minify --environment staging` → `--environment production`. **Només quan el domini
   ja resolgui** — sinó canonicals, OG i sitemap apuntarien a un domini no resoluble. El build
   de producció ja està verificat en local: OG/Twitter complets, meta robots indexable,
   canonicals i sitemap al domini final.
4. **Redireccions del WordPress (671 URLs).** El post-sitemap del WP té 671 URLs en 11
   categories i els slugs coincideixen majoritàriament amb els del Hugo → mapa mecànic amb
   `aliases` de Hugo al front matter de cada fitxa (ex.: `/mercats/mercat-de-la-boqueria/` →
   alias a `/elements/mercat-de-la-boqueria/`). Hugo genera pàgines meta-refresh + canonical
   que Google tracta com a redireccions. Excepcions detectades: `biblioteca-fort-pienc` (al
   Hugo és `illa-dequipaments-fort-pienc`), `mercat-de-la-barceloneta-2` (el Hugo en té una de
   sola) i `placa-i-mercat-de-la-marina` (duplicat al WP).
5. **Post-tall.** Google Search Console (verificar el domini per TXT al DNS i enviar el
   sitemap.xml), Bing Webmaster Tools + IndexNow per a la indexació ràpida, i uns dies de
   monitoratge dels 404 d'antics URLs del WP a GSC. El WordPress del Hetzner es pot retirar
   quan el DNS ja no hi apunti (coordinar amb Jorge).

**Nota sobre el mòbil:** la portada fa `location.replace()` al `/mapa/` en pantalles ≤ 48rem
(decisió d'Xavi, en debat amb la Mar). Amb el tall, Googlebot smartphone veurà sempre el mapa
com a destí de la portada: és coherent amb el disseny actual, però convé saber-ho i revisar-ho
si l'equip convergeix cap al mateix plantejament pc/mòbil.

## Prioritats de treball

| Prioritat | Qüestió | Dimensió | Esforç | Impacte |
|---|---|---|---|---|
| 🔴 CRÍTIC | Tall del domini: DNS + custom domain + workflow a producció | SEO/GEO/AEO | Mitjà | Desbloqueja tot |
| 🔴 CRÍTIC | Corregir el JSON-LD: `\| safeJS` a tots els jsonify de schema.html | SEO/GEO | XS (30 min) | Alt |
| 🔴 CRÍTIC | Redireccions de les 671 URLs del WP (aliases de Hugo) | SEO | Mitjà | Alt |
| 🟠 ALT | robots.txt de producció: directiva `Sitemap:` + `Disallow: /admin/` | SEO | XS | Alt |
| 🟠 ALT | default og:image (1200×630) per a pàgines sense foto | SEO | S | Mitjà |
| 🟠 ALT | Renderitzar al servidor les llistes (arquitectes, publicacions) + headings al mapa | SEO/GEO | M | Alt |
| 🟡 MITJÀ | 404.html propi amb cerca d'elements | SEO | S | Mitjà |
| 🟡 MITJÀ | lastmod al sitemap (enableGitInfo) i dates visibles | SEO | S | Mitjà |
| 🟡 MITJÀ | llms.txt + política de bots d'IA al robots.txt de producció | GEO | S | Mitjà |
| 🟢 QUICK WIN | Títol redundant del mapa + consistència de xifres portada/Presentació | SEO | XS | Baix |

## Què funciona bé

| Fortalesa | Evidència del crawling |
|---|---|
| Entorns separats amb cura | Staging 100% noindex per disseny; producció verificada en local amb canonicals, OG i sitemap apuntant al domini final |
| Contingut de publicacions | interiors-illa: 1.500+ paraules, dades factuals citables (16.000 hab/km², 70+ jardins) i bibliografia enllaçada — or per a GEO i snippets |
| E-E-A-T | Crèdits amb noms i rols, fonts COAC/Viquipèdia, CC BY-SA 4.0 i suport de l'Ajuntament de Barcelona |
| RGPD exemplar | GoatCounter sense cookies: zero banners, política neta — confiança per a lectors, cercadors i IA |
| Formulari públic de correccions | Senyal de manteniment viu i participació dels lectors |
| Fitxes semàntiques | Adreça per coordenades, alt a les imatges amb crèdit, navegació prev/next i TTS «Escoltar» (únic al sector) |
| Base tècnica sana | RSS actiu, URLs netes, lloc estàtic ràpid, HTML semàntic a fitxes i publicacions |

## Glossari

- **SEO** — Search Engine Optimization: optimització per als cercadors clàssics (Google, Bing): crawling, indexació i ranquing de pàgines web.
- **GEO** — Generative Engine Optimization: optimització per als motors generatius (Perplexity, ChatGPT Search, AI Overviews de Google): aconseguir que les IA triïn el web com a font i el citin a les respostes.
- **AEO** — Answer Engine Optimization: optimització per als motors de resposta (featured snippets, People Also Ask, cerca per veu): respondre preguntes concretes de forma directa i extractible.
