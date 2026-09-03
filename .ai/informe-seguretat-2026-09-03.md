# Informe de seguretat — Guies Barcelona
Data: 2026-09-03
Nivell anterior (30/08/2026): MODERAT-BAIX

---

## Nivell actual: MODERAT

La implementació de les correccions prioritàries de codi (SRI, whitelist ?tema=, unsafe=false, document.write) ha eliminat les vulnerabilitats directament corregibles sense canvi de servidor. El nivell puja de MODERAT-BAIX a MODERAT. Els elements que mantenen el risc en MODERAT (i no en ALT) són les vulnerabilitats estructurals que depenen de Dinahosting: absència de headers HTTP, CMS sense OAuth, analytics.json públic.

---

## Resum de canvis

| Vulnerabilitat | Informe 30/8 | Estat 3/9 | Verificat |
|---|---|---|---|
| SRI GoatCounter (count.js) | Sense SRI | Corregit — sha384 a head.html:54 | head.html linia 54 |
| SRI Chart.js (cdn.jsdelivr.net) | Sense SRI | Corregit — sha384 a admin/stats/index.html:12 | stats/index.html linia 12 |
| document.write() als fitxers admin | Present (6 fitxers) | Eliminat — substituït per getElementById a tots els fitxers | Grep confirma 0 coincidències document.write |
| ?tema= sense whitelist | Directe a classList.add | Corregit — whitelist ['a','b','c'] a mapa.js:49 | mapa.js linia 49 |
| unsafe=true Goldmark | unsafe = true | Corregit — unsafe = false a config/_default/hugo.toml:87 | hugo.toml linia 87 |
| robots.txt de producció | Sense Sitemap | Corregit — Sitemap + Disallow:/admin/ + bots IA permesos | layouts/robots.txt |
| llms.txt | No existia | Creat — context per a motors d'IA | static/llms.txt |
| CMS sense autenticació OAuth | CRÍTIC | Pendent — espera Dinahosting | TASKS.md Fase 1 |
| analytics.json públic | CRÍTIC | Pendent — espera Dinahosting | TASKS.md |
| Headers HTTP absents (CSP, HSTS...) | IMPORTANT | Pendent — limitació GitHub Pages | Estructural |
| envia.php no auditat | IMPORTANT | Pendent — dia del tall | Herència WP |
| DMARC/SPF/DKIM | MILLORA | Pendent — espera Dinahosting | Estructural |

---

## Anàlisi per categoria

### Codi client (JavaScript/HTML)

**SRI a dependències externes — RESOLT**

GoatCounter (`gc.zgo.at/count.js`) ara inclou:
```html
integrity="sha384-2UjvVpptg4JlEVgJI2PdscrjOjPcil/4F1ZvIMJ81CShQnEDSlPI+l4PfogvTLYi"
crossorigin="anonymous"
```
El script és condicionat a `not hugo.IsServer` (no carrega en local) i a `site.Params.gc_url` (no carrega a staging si el paràmetre no és definit).

Chart.js (`cdn.jsdelivr.net/npm/chart.js@4.4.0`) a `static/admin/stats/index.html` ara inclou:
```html
integrity="sha384-e6nUZLBkQ86NJ6TVVKAeSaK8jWa3NhkYWZFomE39AvDbQWeie9PlQqM3pmYW5d1g"
crossorigin="anonymous"
```

**Nota:** `static/admin/stats/index.html` continua sent accessible públicament (accés directe a `/admin/stats/`). L'SRI protegeix la integritat de Chart.js però no restringeix l'accés al dashboard.

**Whitelist ?tema= — RESOLT**

El codi a `mapa.js:49` ara és:
```javascript
var tema = ['a', 'b', 'c'].indexOf(temaBrut) !== -1 ? temaBrut : 'a';
```
Qualsevol valor aliè cau a `'a'` sense afectar `classList.add`. Anteriorment un valor com `?tema=malicious-class` podia afegir classes arbitràries al contenidor.

**document.write() — RESOLT**

Els 8 fitxers HTML de `/static/admin/` (index, guia, guia-admin, guia-usuaris, instal-la-al-mobil, galeria) fan servir ara `document.getElementById('year').textContent = new Date().getFullYear()`. Els fitxers `cms/index.html` i `cms-admin/index.html` usen concatenació de string (`'© ' + new Date().getFullYear()`) dins un context de generació dinàmica de HTML, que és acceptable.

**SRI per a assets propis — MANTINGUT**

Hugo genera `integrity="{{ $css.Data.Integrity }}"` per al CSS propi. El JS del mapa i altres assets locals es serveixen des del mateix origen (sense dependència de CDN).

**Leaflet — LOCAL, sense CDN**

Leaflet 1.9.4 es serveix des de `static/vendor/leaflet/` (sense CDN extern, sense SRI necessari). Sense canvis.

### Configuració Hugo

**unsafe=false Goldmark — RESOLT**

`config/_default/hugo.toml` (línia 87): `unsafe = false`. L'únic HTML en cru que hi havia al contingut (badges d'accessibilitat) s'ha mogut al shortcode `badges-accesibilitat`. Build complet verificat (1.645 pàgines) sense regressions.

**Impacte:** Cap editor del CMS, ni en cas d'accés no autoritzat, pot injectar HTML arbitrari via Markdown.

**enableGitInfo — activat**

El build de producció genera `lastmod` a les 964 URLs del sitemap a partir de l'historial git. No té impacte de seguretat directe però reflecteix bona pràctica de gestió.

### Infraestructura (GitHub Pages — staging)

**Headers HTTP de seguretat — ABSENT (limitació estructural)**

GitHub Pages no permet configurar headers personalitzats. En conseqüència falten:

- `Content-Security-Policy` — sense CSP, un XSS potencial és més fàcil d'explotar
- `X-Frame-Options` — la pàgina pot ser incrustada en iframes (clickjacking)
- `X-Content-Type-Options: nosniff` — sense protecció MIME-sniffing
- `Strict-Transport-Security` — HTTPS forçat per GitHub Pages però sense HSTS explícit
- `Referrer-Policy` — sense control dels referrers enviats a tercers

Aquesta limitació és una de les raons principals per migrar a un hosting que permeti headers (Dinahosting, Vercel, Netlify o Cloudflare frontal).

**robots.txt — CORREGIT**

L'entorn de producció (`env != staging`) ara inclou:
- `Disallow: /admin/` — les interfícies d'administració no s'indexen
- `Sitemap:` amb URL absoluta
- 13 bots d'IA i cercadors generatius explícitament permesos (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot, OAI-SearchBot, Perplexity-User, Claude-Web, anthropic-ai, Applebot-Extended, cohere-ai, Meta-ExternalAgent, ChatGPT-User)

L'entorn de staging (`env = staging`) manté `Disallow: /` per a tots els agents.

**llms.txt — NOU**

Creat a `static/llms.txt`: context estructurat per a motors d'IA amb descripció del projecte, navegació principal, llistat de les 13 publicacions i notes de llicència (CC BY-SA 4.0). Coherent amb la política de robots.txt de producció (bots IA benvinguts).

### CMS (Sveltia CMS)

**Autenticació — PENDENT (espera Dinahosting)**

Les interfícies `/admin/` i `/admin/cms/` continuen sent accessibles públicament sense autenticació de servidor. L'autenticació actual és un Personal Access Token (PAT) de GitHub introduït manualment. La Fase 1 (OAuth via GitHub App) està bloquejada fins que Dinahosting estigui configurat.

Risc actual: qualsevol persona pot accedir a les interfícies del CMS. Si un PAT és filtrat o reutilitzat, pot modificar el contingut del repositori.

**analytics.json — PENDENT (espera Dinahosting)**

`/admin/stats/analytics.json` continua sent accessible sense autenticació. Conté estadístiques de visita: pàgines, navegadors, sistemes operatius, ubicacions i referrers. L'accés no requereix cap credencial.

**Guies del CMS — actualitzades**

Les guies a `/admin/guia/` reflecteixen l'adreça real (github.io + domini futur) i el token clàssic (no fine-grained). No és un canvi de seguretat sinó de precisió documental.

### Pendent fins al canvi de servidor

Aquests punts no es poden resoldre mentre el projecte estigui a GitHub Pages:

1. **OAuth proxy** — `oauth/index.php` amb validació CSRF (state param), GitHub OAuth App, secrets a Dinahosting fora del webroot. Quan estigui llest: actualitzar `config.yml` amb `base_url`.
2. **analytics.json** — moure a ruta protegida o substituir per càrrega directa des de la GoatCounter API amb token protegit server-side.
3. **Headers HTTP** — CSP, X-Frame-Options, X-Content-Type-Options, HSTS, Referrer-Policy. Configurables via `.htaccess` a Dinahosting o via CDN Cloudflare frontal.
4. **DMARC/SPF/DKIM** — si s'envien emails des de `@elglobusvermell.org`, configurar els registres DNS corresponents.
5. **envia.php** — el formulari de contacte envia a un PHP que no és al repositori Hugo. Cal auditar (validació CSRF, sanitització, anti-spam) o substituir per una alternativa serverless. Es fa el dia del tall.
6. **SMTP formulari** — l'opció `mailto:` és el substitut actual fins que el servidor estigui definit.

---

## Riscos acceptats i raó

| Risc | Raó d'acceptació |
|---|---|
| CMS accessible sense OAuth | Bloquejat per Dinahosting; PAT requereix acció activa de l'usuari per filtrar-lo |
| analytics.json públic | Dades de GoatCounter, sense dades personals identificables; risc de privacitat baix |
| Absència de headers HTTP | Limitació de GitHub Pages; irresoluble sense canvi de hosting |
| envia.php no auditat | No és al repo Hugo; es tractarà el dia del tall |
| Google Fonts sense SRI | Carregat des de `stats/index.html` (pàgina admin, no pública); risc molt baix |

---

## Limitacions de la revisió

- Els headers HTTP reals del staging (`112books.github.io`) no s'han pogut verificar per fetch directe en aquesta sessió. El comportament de GitHub Pages (absència de CSP/HSTS/X-Frame-Options) és documentat i confirmat per l'auditoria anterior i per la documentació oficial de GitHub Pages.
- El codi de `envia.php` no és accessible al repositori Hugo i no ha pogut ser auditat.
- No s'han analitzat les dependències Python dels scripts de manteniment (`scripts/`); recomanació: `pip audit` periòdic.

---

## Pròxims passos

**Immediats (no depenen de servidor)**
- Cap — totes les correccions aplicables sense Dinahosting estan fetes.

**Quan Dinahosting estigui llest (Fase 1)**
1. Crear GitHub OAuth App (callbacks per a dev i prod)
2. Desplegar `oauth/index.php` amb validació CSRF
3. Configurar secrets a Dinahosting fora del webroot
4. Actualitzar `static/admin/cms/config.yml` i `cms-admin/config.yml` amb `base_url`
5. Provar flux OAuth complet
6. Configurar headers HTTP: CSP, X-Frame-Options, X-Content-Type-Options, HSTS, Referrer-Policy
7. Revisar analytics.json: moure o substituir per càrrega directa GoatCounter API
8. Configurar DMARC/SPF/DKIM si s'activa correu SMTP

**Dia del tall**
- Auditar o substituir `envia.php`
- Activar formulari de contacte per SMTP

**Recomanació post-migració**
- Implementar CSP estricta tal com s'esbossa a l'informe del 30/08/2026 (§3.1)
- Activar branch protection a GitHub (`main`, revisió PR obligatòria)
- `pip audit` als scripts Python de manteniment
