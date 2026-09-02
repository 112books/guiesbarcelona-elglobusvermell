# Kit del tall del domini — guiesbarcelona.elglobusvermell.org

**Què és:** el pas a pas operatiu per moure el domini del WordPress antic (Hetzner `195.201.2.76`) al web Hugo (GitHub Pages). Derivat de `.ai/informe-seo-geo-aeo-2026-09-01.md` (pas a pas) i verificat amb build de producció en local el 2 de setembre de 2026.

**Regla de Joan (1 set): el tall és la DARRERA cosa** — es fa quan la migració estigui confirmada contra el WordPress en viu (font bona) i amb el server decisiu. Fins llavors: GitHub Pages amb l'entorn `staging` (noindex).

---

## Pre-vols ja verificats (2 set 2026, `hugo --environment production`)

- [x] Canonicals, `og:url` i sitemap apunten al domini final (963 URLs, totes amb `lastmod`)
- [x] 672 aliases generats: 671 URLs del WP antic + `/elements/` (duplicat del mapa eliminat)
- [x] `robots.txt` de producció: `Sitemap:`, `Disallow: /admin/` i 13 bots d'IA permesos
- [x] `llms.txt`, `404.html` (amb cerca al llistat), `img/og-default.jpg` 1200×630
- [x] Meta robots indexable a producció; noindex NOMÉS a staging
- [x] JSON-LD vàlid (safeJS): WebSite, LandmarksOrHistoricalBuildings, Person/Organization amb sameAs, speakable

## Pas 1 — Custom domain a GitHub Pages (112books)

- Repo → Settings → Pages → Custom domain: `guiesbarcelona.elglobusvermell.org` (+ afegir `www.guiesbarcelona.elglobusvermell.org`). Es crea el fitxer CNAME al repo.
- Un cop el DNS resolgui (pas 2): activar **Enforce HTTPS** (el Let's Encrypt triga 15 min – 24 h).

## Pas 2 — DNS (el gestiona en Jorge)

Al panell DNS d'`elglobusvermell.org` (avui `guiesbarcelona` apunta a `195.201.2.76`):

```
CNAME  guiesbarcelona  →  112books.github.io
CNAME  www.guiesbarcelona  →  112books.github.io
```

(És subdomini: el CNAME és vàlid.) Coordinar amb Jorge; verificar la propagació amb `dig guiesbarcelona.elglobusvermell.org`.

## Pas 3 — Build de producció al workflow

`.github/workflows/deploy-prod.yml`, línia 40:

```diff
-        run: hugo --minify --environment staging
+        run: hugo --minify --environment production
```

**NOMÉS quan el DNS ja resolgui** al GitHub Pages — sinó canonicals, OG i sitemap apuntarien a un domini no resoluble. El build de producció està verificat en local (pre-vols de dalt). Esborrar el CNAME del repo si el pas 1 el va crear amb contingut equivocat (ha de ser exactament el subdomini).

## Pas 4 — Redireccions del WordPress ✅ JA FET (1–2 set)

671 URLs del WP via `aliases` al front matter (`scripts/aliases-wordpress.py`, idempotent). Hugo genera meta-refresh + canonical que Google tracta com a redireccions. Excepcions conegudes i gestionades: `biblioteca-fort-pienc` (→ `illa-dequipaments-fort-pienc`), `mercat-de-la-barceloneta-2` (fitxa única al Hugo) i `placa-i-mercat-de-la-marina` (duplicat al WP). El 2 set s'hi afegí `/elements/` → `/mapa/`.

## Pas 5 — Post-tall

- [ ] **Google Search Console:** verificar el domini (TXT al DNS), enviar `sitemap.xml`, demanar indexació de la portada
- [ ] **Bing Webmaster Tools** + **IndexNow** (indexació ràpida)
- [ ] Monitoratge de 404 d'URLs antics del WP a GSC durant uns dies
- [ ] **Retirar el WordPress del Hetzner** quan el DNS ja no hi apunti (coordinar amb Jorge; abans: confirmació final de la migració contra el WP en viu — font bona)
- [ ] `envia.php` i `analytics.json`: auditar/restringir el mateix dia (pendents de seguretat)
- [ ] `hreflang`: preparar quan s'activin EN/ES

## Rollback

Si algo va malament amb el domini: tornar el DNS al Hetzner (el WP segueix viu fins al pas 5) i revertir la línia 40 del workflow a `staging`. No es perd res: el contingut Hugo és al repo.

## Nota mòbil

La portada fa `location.replace()` al `/mapa/` en pantalles ≤ 48rem (decisió d'Xavi 28/8, en debat amb la Mar — el consens de l'equip hi pot canviar el plantejament). Amb el tall, Googlebot smartphone veurà sempre el mapa com a destí de la portada: coherent amb el disseny actual, però convé revisar-ho si l'equip convergeix pc/mòbil.
