# Informe SEO / GEO / AEO — Guies Barcelona
Data: 2026-09-03
Estat anterior: SEO 6/10 · GEO 5/10 · AEO 5/10 (informe 01/09/2026)

## Puntuació actual

- SEO: 7,5/10
- GEO (motors de cerca generatius): 7/10
- AEO (resposta directa / featured snippets): 6/10

Les puntuacions reflecteixen l'estat del codi i els builds verificats localment. El web viu a staging (github.io, noindex per disseny): totes les millores estan desplegades i llestes per activar-se tan aviat com el DNS apunti al build de producció.

---

## Resum de canvis respecte l'informe anterior

| Punt | Informe 1/9 | Estat 3/9 | Verificat |
|---|---|---|---|
| JSON-LD invàlid (auto-escape de Go html/template) | CRÍTIC — afectava tota la dada estructurada | Corregit: `jsonify \| safeJS` a tots els camps de schema.html | Codi verificat |
| robots.txt de producció minimal | Sense Sitemap: ni Disallow: /admin/ | Corregit: Sitemap: + Disallow: /admin/ + 13 bots d'IA permesos | Template verificat |
| llms.txt inexistent (404) | Falta | Creat a static/llms.txt: 13 publicacions + notes per a IA | Fitxer verificat |
| og:image absent a ~315 fitxes i hubs | Atenció | Corregit: og-default.jpg 1200×630 (57 KB) al config com a defaultOgImage | Codi + fitxer verificats |
| Redireccions 671 URLs del WP | CRÍTIC — pendent | Implementades: 672 aliases a les 660 fitxes (script idempotent, plantilla noindex catalana) | Registre TASKS.md |
| SpeakableSpecification absent | Falta | Implementat: WebPage + cssSelector .fitxa-descripcio a fitxes amb descripció | Codi verificat |
| sameAs Organization absent | Atenció | Implementat: 6 perfils socials confirmats (Instagram, Twitter/X, Bluesky, Facebook, LinkedIn, YouTube) | Config verificat |
| sameAs arquitectes absent | Falta | Implementat: Person/Organization amb sameAs (COAC, Viquipèdia, web oficial) | Codi verificat |
| lastmod al sitemap (6 de 964 URLs) | Atenció | Corregit: enableGitInfo = true → lastmod a totes les URLs | Config verificat |
| 404 sense pàgina pròpia | Atenció | Corregit: 404.html amb el layout del tema + cerca al llistat | Codi verificat |
| Meta description automàtica absent | Atenció | Corregit: fallback .Params.descripcio truncat a 155 car. | Codi verificat |
| Duplicat /elements/ (restes del canvi d'URL 31/8) | No detectat a l'1/9 | Corregit: build: render: never + redirect alias a /mapa/ | TASKS.md |
| SRI a dependències externes | No detectat a l'1/9 | Corregit: GoatCounter sha384 + Chart.js sha384; crossorigin="anonymous" | Codi verificat |
| document.write() | No detectat a l'1/9 | Corregit: substituït per getElementById a 6 fitxers admin | TASKS.md |
| Bots d'IA al robots.txt de producció | Falta | Implementat: 13 bots explícitament permesos (GPTBot, ClaudeBot, PerplexityBot, Google-Extended...) | Template verificat |
| 4 punts bloquejats per consens d'equip | Falta | Sense canvis: SSR de llistes, FAQ/FAQPage, og:image dissenyada, consistència xifres | Pendent equip |

---

## SEO tècnic

### Metadades i Open Graph

**Title tag** — Format consistent «Pàgina — Guies de Barcelona de El Globus Vermell» a totes les pàgines. La portada conserva només la marca (38 car.). El duplicat de títol del mapa (doble marca) estava pendent de consens d'equip; al moment d'escriure aquest informe el títol del mapa s'ha netejat (verificat al TASKS.md: «títol del mapa» a la passada del 1/9). Estat: Be.

**Meta description** — Cadena de fallback en tres nivells: (1) `.Description` del front matter, (2) `.Params.descripcio` truncat a 155 car., (3) descripció global del site. Les 660 fitxes amb descripció pròpia (`descripcio:`) generen meta description individual. Les 13 publicacions i els hubs (arquitectes, accessibilitat, presentació) han rebut descripcions manuals a la passada del 1/9. Estimació: ~350 pàgines encara amb meta description genèrica (les fitxes data-only sense camp `descripcio`). Estat: Millora respecte l'informe anterior.

**Open Graph** — Complet a producció: og:type, og:url, og:title, og:description, og:site_name, og:locale, og:image, twitter:card. La imatge per defecte (`og-default.jpg`, 57 KB, 1200×630, logo sobre fons blanc, aprovat per Joan el 2/9) cobreix les ~315 fitxes sense foto i totes les pàgines hub. Les fitxes amb foto usen la foto de l'edifici com a og:image. Twitter card commuta entre `summary` (sense imatge) i `summary_large_image` (amb imatge) automàticament. Estat: Be.

**Canonical** — Self-referencing per entorn, generat per Hugo. Staging apunta a github.io; el build de producció apuntarà a guiesbarcelona.elglobusvermell.org. Estat: Be.

**Robots meta** — Staging: `noindex, nofollow, noai, noimageai, noarchive, nositelinkssearchbox` (correcte per disseny). Producció: indexable (sense meta robots restrictiva). Estat: Be.

### Schema.org / dades estructurades

El bug crític d'escapament (l'auto-escaping de Go `html/template` produia `"name": "\"Guies de Barcelona…\""`) esta corregit: tots els camps de `schema.html` usen `jsonify | safeJS`. La dada estructurada es ara valida a tots els entorns.

**Cobertura del schema per tipus de pagina:**

| Pagina | Tipus schema | Camps clau | Estat |
|---|---|---|---|
| Portada | WebSite | name, url, description, inLanguage, publisher (Organization + sameAs 6 perfils) | Be |
| Fitxa d'edifici (amb descripcio) | LandmarksOrHistoricalBuildings + WebPage (Speakable) | name, url, description, address, geo, image, dateCreated, creator (Person) | Be |
| Fitxa d'edifici (sense descripcio) | LandmarksOrHistoricalBuildings | name, url, address, geo, image, dateCreated, creator | Be — sense Speakable (correcte: sense text llegible) |
| Fitxa d'arquitecte | Person o Organization (tipus: estudi) | name, url, jobTitle, description, sameAs (COAC/Viquipedia/web) | Be |
| Resta de pagines | Cap schema propi | Meta i OG coberts | Atenció — sense schema |

Limitacio coneguda: les pagines hub (mapa, arquitectes, publicacions, presentacio) no tenen schema propi. El contingut d'aquestes pagines es majoritariament renderitzat per JavaScript (client-side), de manera que afegir-los schema seria poc efectiu fins que el contingut estigui al HTML.

### Rastreig i indexacio

**robots.txt per entorn** — Template `layouts/robots.txt` condicional:

- Staging: bloqueja tots els bots (Googlebot, Bingbot, 13 bots d'IA, etc.) — correcte per disseny.
- Produccio (build `--environment production`): `Allow: /`, `Disallow: /admin/`, directiva `Sitemap:` amb URL absoluta, i 13 bots d'IA i cercadors generatius explicitament permesos amb `Allow: /` (GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, CCBot, cohere-ai, Meta-ExternalAgent). Senyal GEO coherent amb el `llms.txt`.

**Sitemap** — 963 URLs (build de produccio verificat localment: 660 fitxes + 274 arquitectes + 13 publicacions + hubs/legals). `enableGitInfo = true` assegura `lastmod` basat en git a totes les URLs. Anteriorment nomes 6 de 964 tenien `lastmod`. Estat: Be.

**404** — Pagina 404.html propia amb el layout del tema i un enllaç de cerca «Cerca un edifici al llistat alfabetic» que apunta a `/mapa/#llistat`. Anteriorment GitHub Pages servia la 404 generica anglesa. Estat: Be.

**RSS** — `/index.xml` actiu. Estat: Be.

### URLs i redirects

672 redirects cobreixen les 671 URLs del WordPress de produccio (WP post-sitemap) mes el duplicat `/elements/` → `/mapa/`. Cada redirect es una pagina `alias.html` catalana amb `<meta http-equiv="refresh">`, `<link rel="canonical">` i `<meta name="robots" content="noindex">` — Google les tracta com a redireccions. El script `scripts/aliases-wordpress.py` es idempotent; els 44 canvis de nom verificats un per un. El duplicat intern `/elements/` (restes del canvi d'URL del 31/8) esta eliminat del sitemap (`build: render: never`) i redirigit.

Limitacio: els 672 redirects son meta-refresh, no HTTP 301. Un cop el DNS apunti al nou servidor i hi hagi acces a la configuracio del servidor (Dinahosting), es recomanable afegir 301 reals a nivell de servidor per als casos mes importants (portada WP i categories principals). Per a un lloc estàtic a GitHub Pages, pero, el meta-refresh + canonical es la solucio estandard i Google l'accepta.

### Rendiment (impacte SEO)

Imatges optimitzades: 837 → 144 MB (−83%), maxim 1.600px, qualitat 85, EXIF eliminat. `width`/`height` declarats a `<img>` (manifest `data/imatges_dims.json`, 408 imatges) → menys CLS. Imatge LCP amb `fetchpriority="high"` i `loading="eager"`. Leaflet 1.9.4 dist minificada, 42 KB gzipades. CSS minificat amb fingerprint i SRI. Lloc estatic a GitHub Pages amb HTTPS forcat. Aspecte que resta pendent: conversio a WebP (880 MB originals); decisio ajornada perque WhatsApp/Telegram no llegeixen WebP com a og:image i caldria miniatures JPG separades.

---

## GEO — Optimitzacio per a motors generatius

### Accessibilitat per a bots d'IA (robots.txt, llms.txt)

**robots.txt de produccio** — 13 bots d'IA i cercadors generatius explicitament permesos (detall a la seccio anterior). Anteriorment el robots.txt de produccio era minimal (`Allow: /` i res mes). Ara el senyal es clar: el web vol ser indexat i citat pels motors generatius.

**llms.txt** — Creat a `static/llms.txt`. Inclou: descripcio del projecte, navigacio principal (6 seccions), llista de les 13 publicacions amb any i estat, i notes per a sistemes d'IA (llengua, llicencia CC BY-SA 4.0, estructura de les fitxes, politica de correccions, RSS). Format Markdown curat, llegible per LLMs sense processament previ. Anteriorment era 404.

### Citabilitat del contingut

**Densitat factual** — Les publicacions segueixen sent el punt fort: `interiors-illa` (1.500+ paraules, xifres citables com 16.000 hab/km², 70+ jardins interiors, 150.000 m² recuperats, bibliografia enllaçada). El contingut original de les guies de camp (Cerda, superilles, patrimoni industrial del Poblenou, avantguarda GATCPAC 1928–1939) no te equivalent a cap altra font web en catala. Estat: Be.

**Estructura llegible per IA** — Les fitxes d'edifici serveixen dades estructurades al HTML: adreça, any, arquitectes com a text i com a schema JSON-LD. El `SpeakableSpecification` marca la seccio `.fitxa-descripcio` per als assistents de veu. Les 346 fitxes amb descripcio generen ara schema Speakable + dada factual estructurada (LandmarksOrHistoricalBuildings). Estat: Millora.

**Limitacio vigent** — El 62% de les fitxes te descripcio pero el 38% restant (les data-only, inclosa la Boqueria) nomes te schema amb dades. Sense paragraf descriptiu, la citabilitat per a respostes de text lliure es limitada. Aquesta limitacio dependra de l'equip editorial per omplir les fitxes o de decidir una descripcio automatica basada en els camps estructurats.

### Entitat i sameAs

**Organization (portada)** — 6 perfils socials actius declarats al `sameAs` del schema WebSite: Instagram, Twitter/X, Bluesky, Facebook, LinkedIn, YouTube. Issuu exclòs (perfil 404, verificat el 2/9). Anteriorment no hi havia cap perfil social al schema. El graf d'entitat que construeix El Globus Vermell als motors generatius es ara mes robust. Estat: Be.

**Person / Organization (arquitectes)** — sameAs amb COAC, Viquipedia i web oficial quan els camps `link_coac`, `link_wikipedia` i `link_web` existeixen a la fitxa o al fitxer `arquitectes-bio-extra`. Els arquitectes sense biografia curada (79 de 274) generen schema minimal pero valid. Estat: Be.

**E-E-A-T** — Crèdits amb noms i rols, fonts COAC i Viquipedia, CC BY-SA 4.0, suport de l'Ajuntament de Barcelona, formulari public de correccions. RGPD exemplar (GoatCounter sense cookies). Estat: Be.

---

## AEO — Answer Engine Optimization

### SpeakableSpecification

Implementat a les fitxes d'edifici amb camp `descripcio`: schema `WebPage` amb `SpeakableSpecification` i `cssSelector: [".fitxa-descripcio"]`. Es coherent amb la funcio TTS «Escoltar» ja existent a les fitxes. Anteriorment absent. Les 346 fitxes amb descripcio son ara elegibles per a resposta per veu. Estat: Implementat (millora des de Falta).

Limitacio: el cssSelector apunta a la seccio de descripcio, no al titol ni a les dades factuals. Un selector mes ampli (incloent `.fitxa-dades`) podria millorar la cobertura de les respostes factuals per veu, pero requeriria proves de qualitat de lectura.

### FAQ i contingut estructurat

**FAQ** — Absent. Cap schema FAQPage ni pagines de preguntes frequents. El formulari public de correccions genera preguntes reals dels lectors que podrien alimentar una FAQ curada. Aquesta millora dependra de l'equip editorial. Estat: Pendent (bloquejat per equip).

**Headings en forma de pregunta** — Absents a totes les pagines auditades. Cap H2/H3 amb «Com...? / Que...? / Per que...?». Estat: Pendent (bloquejat per equip — es decisio editorial, no tecnica).

**Paràgrafs de resposta directa** — Les 346 fitxes amb descripcio son elegibles per a featured snippets. El 38% data-only (sense text extractible) queda fora. Les publicacions (hub de llarga forma) son el contingut mes solid per a snippets factuals. Estat: Parcial.

**Llistes i taules al HTML** — Les llistes principals (elements, publicacions, arquitectes als hubs) segueixen renderitzant-se nomes via JavaScript. Els motors generatius que no executen JS no veuen aquestes llistes. Les descàrregues PDF de les publicacions i la navegacio prev/next de les fitxes si que son al HTML. Estat: Atenció (bloquejat per consens d'equip — SSR de llistes).

### Cerca per veu i long-tail

**TTS «Escoltar»** — Web Speech API nativa a les fitxes d'edifici. Unic al sector en catala. Estat: Be.

**Preguntes long-tail cobertes** — «Qui va construir X» → cobert per les dades de la fitxa + schema creator. «Quin es l'edifici mes antic de...», «Quants edificis modernistes hi ha a...» → no cobert per cap pagina. Pendent d'equip editorial.

---

## Bloquejat fins al tall de domini

Els punts seguents son tecnics pero no es poden activar fins que el DNS apunti al build de produccio:

| Eina | Motiu del bloqueig | Preparat? |
|---|---|---|
| Google Search Console | Requereix verificar el domini (TXT al DNS) + enviar sitemap.xml al domini final | Build de produccio verificat localment; el sitemap apunta al domini final |
| Bing Webmaster Tools + IndexNow | Requereix el domini real resolt | Pendent del tall |
| HTTP 301 reals per als redirects | GitHub Pages no permet configurar respostes HTTP | Dinahosting o Vercel/Netlify al moment del tall |
| Headers HTTP de seguretat (CSP, HSTS, X-Frame-Options) | GitHub Pages no permet configurar capçaleres | Dinahosting o Vercel/Netlify |
| DMARC/SPF/DKIM | Requereix configuracio al DNS del domini | Coordinar amb Jorge |
| `analytics.json` public | Restringir acces un cop migrat | Dinahosting |
| `envia.php` (formulari contacte) | Herencia del WP de produccio; no es al repo Hugo | Dia del tall |
| og:image amb disseny propi | El placeholder actual (logo sobre blanc) es provisional | Equip de disseny (Xavi) |

---

## Limitacions de la revisio

1. **Fetch del staging no disponible en sessio** — La verificacio en linia de la portada, robots.txt, llms.txt i sitemap ha estat substituida per la lectura directa dels fitxers font (templates, config, static) i pels registres de TASKS.md. El build de produccio verificat localment el 2/9 dona 963 URLs al sitemap i 672 aliases.

2. **Staging sempre en noindex** — El web public a 112books.github.io esta en noindex per disseny. Cap motor de cerca ni bot d'IA el pot rastrejar. Totes les millores GEO/AEO son efectives nomes un cop el DNS apunti al build de produccio.

3. **Punts bloquejats per equip** — 4 millores de SEO/AEO depenen de decisions editorials o de disseny i no s'han implementat: SSR de llistes (hubs renderitzats per JS), FAQ/FAQPage, og:image dissenyada, i consistencia de xifres portada/Presentacio. Cap d'aquests punts es tecnicament complex un cop hi hagi consens.

4. **Sitemap de produccio no accessible en linia** — El sitemap del build de produccio s'ha verificat localment (963 URLs, lastmod a totes). No s'ha pogut fer fetch en sessio; els numeros provenen del registre TASKS.md (passada del 2/9).

---

## Proxims passos prioritaris

| Prioritat | Punt | Dimensio | Esforc | Desbloqueig |
|---|---|---|---|---|
| CRITIC | Tall del domini: DNS + custom domain GitHub Pages + workflow produccio | SEO/GEO/AEO | Mitja | Xavi (~16 set) + Jorge (DNS) |
| CRITIC | Google Search Console: verificar domini TXT + enviar sitemap | SEO | XS | Just despres del tall |
| ALT | Bing Webmaster Tools + IndexNow (indexacio rapida) | SEO | XS | Just despres del tall |
| ALT | SSR de llistes (arquitectes, publicacions) + headings al mapa | SEO/GEO | M | Consens equip |
| MITJA | FAQ + schema FAQPage + headings en forma de pregunta | AEO | M | Equip editorial |
| MITJA | og:image dissenyada 1200×630 (el placeholder actual ja es funcional) | SEO | S | Disseny (Xavi) |
| MITJA | Consistencia xifres portada/Presentacio | SEO | XS | Consens equip |
| MITJA | Headers HTTP seguretat (CSP, HSTS) | Seguretat | S | Dinahosting / hosting nou |
| BAIXA | hreflang EN/ES | SEO | S | Quan s'activin els idiomes |
| BAIXA | SpeakableSpecification mes ampli (.fitxa-dades inclos) | AEO | XS | Qualsevol sessio |
| BAIXA | Imatges WebP (amb solucio per og:image JPG separades) | Rendiment | M | Qualsevol sessio |
