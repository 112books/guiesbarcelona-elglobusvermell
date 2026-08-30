# Informe d'auditoria de seguretat
## Guies de Barcelona — El Globus Vermell

**Data:** 30 d'agost de 2026
**Nivell de risc general: MODERAT-BAIX**

---

## Resum executiu

El model estàtic Hugo proporciona avantatges inherents de seguretat: no hi ha backend dinàmic, cap injecció SQL ni API server-side, HTTPS obligatori via GitHub Pages, i tot el codi és auditable al repositori. Els riscos principals provenen de la secció d'administració accessible públicament, l'absència de headers HTTP de seguretat (limitació de GitHub Pages), i algunes dependències externes sense Subresource Integrity.

Amb les correccions prioritàries implementades el nivell passaria a **ALT**.

---

## 1. Problemes crítics

### 1.1 CMS accessible sense protecció de contrasenya
**Fitxers:** `/static/admin/cms/index.html`, `/static/admin/stats/`, `/static/admin/cms-admin/`

Les interfícies d'administració (editor CMS, dashboard d'estadístiques) són accessibles públicament. L'única autenticació és un Personal Access Token (PAT) de GitHub introduït manualment per l'editor. Qualsevol persona pot accedir a les interfícies.

**Impacte:** Superfície d'atac exposada; si s'obté el token, pot modificar contingut del repositori.

**Solució:** Implementar OAuth via GitHub App (ja previst al `config.yml` com a `base_url: /oauth/`). Alternativa temporal: HTTP Basic Auth si el hosting ho permet.

---

### 1.2 analytics.json accessible públicament
**Fitxer:** `/static/admin/stats/analytics.json`

El fitxer conté totes les estadístiques del site: hits diaris, pàgines més visitades, navegadors, sistemes operatius, ubicacions geogràfiques, referrers. Accessible sense autenticació.

**Impacte:** Privacitat dels visitants (ubicació geogràfica, comportament); exposició d'informació competitiva.

**Solució a curt termini:** Moure a una ruta no indexada o protegida. El dashboard ja requereix accés a `/admin/` — restringir el JSON al mateix nivell. Alternativa: el dashboard carrega directament de la GoatCounter API (amb token protegit) en lloc d'un JSON estàtic.

---

### 1.3 Paràmetres d'URL llegits sense whitelist estricta
**Fitxer:** `themes/guiesbcn-elglobusvermell/assets/js/mapa.js` (línies 46–49)

```javascript
var tema = (new URLSearchParams(window.location.search).get('tema') || 'a').toLowerCase();
if (contenidor) contenidor.classList.add('tema-' + tema);
```

El valor de `?tema=` s'aplica directament a `classList.add()` sense whitelist explícita. Risc de CSS injection.

**Solució:**
```javascript
var TEMES_VALIDS = ['a', 'b'];
var temaParam = (new URLSearchParams(window.location.search).get('tema') || 'a').toLowerCase();
var tema = TEMES_VALIDS.includes(temaParam) ? temaParam : 'a';
```

---

### 1.4 Markdown renderer amb unsafe = true
**Fitxer:** `config/_default/hugo.toml`

```toml
[markup.goldmark.renderer]
  unsafe = true
```

Permet injectar HTML arbitrari en fitxers Markdown. Si un editor no confiable accedeix al CMS, pot inserir scripts.

**Impacte:** XSS per editors amb accés al CMS.

**Solució:** Avaluar si cal `unsafe = true`. Si els casos d'ús es poden resoldre amb shortcodes d'Hugo, desactivar-lo.

---

## 2. Problemes importants

### 2.1 Absència de headers HTTP de seguretat
**Limitació de GitHub Pages** — no permet configurar headers personalitzats.

Falten: `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options: nosniff`, `Strict-Transport-Security`, `Referrer-Policy`.

**Impacte:** Sense CSP, XSS és més fàcil d'explotar. Sense `X-Frame-Options`, la pàgina pot ser incrustada en iframes maliciosos (clickjacking).

**Solució:** Migrar hosting a Vercel o Netlify (ambdós permeten headers personalitzats via `vercel.json` / `_headers`). Alternativa: Cloudflare com a CDN frontal per injectar headers.

---

### 2.2 Dependències externes sense Subresource Integrity (SRI)
**Fitxers:** `layouts/partials/head.html`, `/static/admin/stats/index.html`

- GoatCounter (`https://gc.zgo.at/count.js`) — sense SRI
- Chart.js (`https://cdn.jsdelivr.net/npm/chart.js@4.4.0/...`) — sense SRI

**Nota positiva:** Els assets generats per Hugo (CSS i JS propis) SÍ inclouen SRI via `integrity="{{ $css.Data.Integrity }}"`.

**Solució:** Calcular i afegir atribut `integrity="sha384-..."` a cada script extern:
```bash
curl -s https://gc.zgo.at/count.js | openssl dgst -sha384 -binary | openssl enc -base64
```

---

### 2.3 Formulari de contacte envia a envia.php extern
**Fitxer:** `themes/guiesbcn-elglobusvermell/layouts/contacte/list.html`

```html
<form action="{{ "contacte/envia.php" | relURL }}" method="post">
```

El fitxer `envia.php` no existeix al repositori (probablement en servidor extern). No s'ha pogut auditar.

**Impacte:** Si `envia.php` no valida servidor-side: CSRF, injecció, spam.

**Solució:** Auditar el codi de `envia.php`. Verificar: validació CSRF, sanitització d'inputs, maxlength, protecció anti-spam. Alternativa: substituir per formulari serverless (Formspree, etc.).

---

### 2.4 document.write() en pàgines administratives
**Fitxer:** `/static/admin/index.html` i similars

```html
<script>document.write(new Date().getFullYear())</script>
```

`document.write()` és obsolet, bloqueja el parsing del DOM i no funciona en documents ja carregats.

**Solució:** `document.getElementById('year').textContent = new Date().getFullYear();`

---

## 3. Millores recomanades

### 3.1 Content Security Policy
Un cop migrat a Vercel/Netlify, implementar CSP:
```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' https://gc.zgo.at https://cdn.jsdelivr.net;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  font-src https://fonts.gstatic.com;
  img-src 'self' data: https: blob:;
  connect-src 'self' https://gc.zgo.at https://guiesbarcelona.goatcounter.com https://api.github.com;
  frame-src 'none';
  upgrade-insecure-requests;
```

### 3.2 Política de privacitat actualitzada
Documentar a `/legal/privacitat/` que GoatCounter és privacy-friendly (sense cookies, RGPD conforme, no rastreia IP exacta, opció Do Not Track).

### 3.3 Revisar dependències Python regularment
```bash
pip show requests  # verificar versió, comprovar CVEs
```

### 3.4 Protecció de domini (DMARC/SPF/DKIM)
Si s'envien emails des del domini `elglobusvermell.org`, configurar registres SPF, DKIM i DMARC per evitar suplantació.

### 3.5 Branch protection i firma de commits
Activar a GitHub: branch protection a `main`, revisió de PR obligatòria, verificació de signatures GPG.

---

## 4. Punts forts

- **SRI per a assets propis:** Hugo genera `integrity` automàticament per a CSS i JS locals — correcte i segur
- **Secrets en GitHub Secrets:** `GC_TOKEN`, `GOATCOUNTER_SITE` no estan hardcodificats al codi
- **HTTPS obligatori:** GitHub Pages força HTTPS per a tot
- **Formularis:** Honeypot anti-spam, regex d'email, checkbox RGPD, `required` attributes, `method="post"`
- **safeURL i safeJS:** Ús correcte de les funcions Hugo per a URLs i JS en templates
- **Leaflet local:** Leaflet es serveix localment (no CDN extern), reduint superfície d'atac
- **Arquitectura estàtica:** Sense base de dades, sense backend dinàmic — la majoria d'atacs web no apliquen
- **Validació ?pub=:** Usa `hasOwnProperty()` per validar valors (tot i que es pot millorar amb whitelist explícita)
- **robots.txt:** L'entorn staging bloqueja indexació; producció és selectiu
- **GitHub Actions permissions:** Workflows amb permisos limitats (`contents: write` o `read`)

---

## 5. Taula de prioritats

| Prioritat | Problema | Fitxer | Acció |
|-----------|----------|--------|-------|
| CRÍTIC | CMS accessible sense auth | /static/admin/ | Implementar OAuth GitHub App |
| CRÍTIC | analytics.json públic | /static/admin/stats/ | Restringir accés o eliminar |
| CRÍTIC | ?tema= sense whitelist | mapa.js:46 | Afegir array de valors vàlids |
| CRÍTIC | unsafe=true Markdown | hugo.toml | Avaluar i desactivar si possible |
| IMPORTANT | Sense headers HTTP | GitHub Pages | Migrar a Vercel/Netlify |
| IMPORTANT | GoatCounter sense SRI | head.html:21 | Afegir integrity hash |
| IMPORTANT | Chart.js sense SRI | admin/stats/ | Afegir integrity hash |
| IMPORTANT | envia.php no auditat | contacte/list.html | Auditar o substituir |
| IMPORTANT | document.write() | /static/admin/ | Refactoritzar |
| MILLORA | CSP estricta | headers config | Implementar post-migració |
| MILLORA | Política de privacitat | /legal/privacitat/ | Documentar GoatCounter |
| MILLORA | Branch protection | GitHub settings | Activar |

---

## 6. Conclusió

**Nivell de risc actual: MODERAT-BAIX.** L'arquitectura estàtica elimina la majoria de riscos web habituals. Els problemes crítics identificats (CMS públic, analytics.json exposat, headers absents) són adreçables amb canvis concrets. El projecte és adequat per a desplegament en producció amb les correccions de la setmana 1–2 implementades.
