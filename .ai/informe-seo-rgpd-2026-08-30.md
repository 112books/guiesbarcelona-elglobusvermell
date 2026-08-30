# Informe d'auditoria SEO i RGPD
## Guies de Barcelona — El Globus Vermell

**Data:** 30 d'agost de 2026
**Conformitat RGPD estimada:** Alta (GoatCounter, sense cookies)
**Nivell SEO tècnic:** Moderat (bon fonament, mancances d'OG i Schema)

---

## Resum executiu

El projecte té una base SEO sòlida: URLs netes, canonical correcte, `robots.txt` per entorn, HTML semàntic, `lang="ca"`. Les mancances principals eren l'absència d'Open Graph / Twitter Cards, de dades estructurades Schema.org, i tres pàgines legals buides ("Pendent de redactar"). Pel que fa a RGPD, el projecte és exemplar: GoatCounter sense cookies, sense Google Fonts, sense CDN externs, sense bàner de consentiment necessari.

**Implementacions fetes el 30/08/2026:**
- Open Graph + Twitter Cards a `head.html` (condicionals per entorn)
- Schema.org JSON-LD: WebSite (inici) + LandmarksOrHistoricalBuildings (fitxes)
- Política de privacitat completa (`/legal/privacitat/`)
- Política de galetes completa (`/legal/cookies/`)
- Avís legal complet (`/legal/avis-legal/`)

---

## 1. Problemes crítics (resolt)

### 1.1 Absència d'Open Graph i Twitter Cards
**Fitxer:** `themes/guiesbcn-elglobusvermell/layouts/partials/head.html`

Sense metadades OG, les fitxes compartides a xarxes socials apareixien sense previsualització (sense imatge, sense títol formatat, sense descripció). Impacte directe en difusió orgànica.

**Solució implementada:** Meta tags `og:*` i `twitter:*` condicionats a l'entorn de producció. La imatge OG s'extreu de `.Params.foto` si existeix.

---

### 1.2 Absència de dades estructurades (Schema.org)
**Fitxer:** nou `partials/schema.html`

Sense Schema.org, Google no pot mostrar rich results per als edificis (Knowledge Panel, resultats enriquits amb ubicació i arquitecte).

**Solució implementada:**
- Pàgina d'inici: tipus `WebSite` amb publisher `Organization`
- Fitxes d'edifici: tipus `LandmarksOrHistoricalBuildings` amb adreça, coordenades, arquitectes i any

---

### 1.3 Pàgines legals buides
**Fitxers:** `content/ca/legal/privacitat.md`, `cookies.md`, `avis-legal.md`

Les tres pàgines contenien únicament "Pendent de redactar". Això genera desconfiança i pot ser problemàtic per al compliment del RGPD.

**Solució implementada:** Contingut complet redactat per a les tres pàgines (veure fitxers).

---

## 2. Problemes importants

### 2.1 Meta descriptions absents en la majoria de pàgines
Les fitxes d'edifici no tenen camp `description` als seus front matters. Sense description, Google genera automàticament el snippet a partir del contingut visible, que pot no ser representatiu.

**Solució parcial:** El camp `description` de la configuració del site s'aplica com a fallback. A llarg termini: afegir `description` als front matters de les fitxes més importants, o usar `.Params.descripcio` com a descripció automàtica.

**Millora recomanada:** Afegir al template `head.html`:
```
{{ with .Params.descripcio }}{{ $desc = . | truncate 155 }}{{ end }}
```

### 2.2 Sitemap.xml: verificar contingut en producció
L'entorn staging genera el sitemap amb la base URL de GitHub Pages. Cal verificar que el sitemap de producció (guiesbarcelona.elglobusvermell.org) és correcte i conté totes les fitxes.

### 2.3 `hreflang` no configurat
El site té contingut en català (actiu), castellà i anglès (desactivats). Quan s'activin els altres idiomes caldrà afegir `<link rel="alternate" hreflang="...">` per evitar problemes de contingut duplicat internacional.

---

## 3. RGPD — Conformitat

### Punts forts (sense acció necessària)

| Aspecte | Estat | Detall |
|---------|-------|--------|
| Galetes | Conforme | Cap galeta de seguiment ni publicitat |
| Analytics | Conforme | GoatCounter: sense cookies, sense IP completa, Do Not Track |
| Google Fonts | Conforme | No s'usen; tipografia de sistema |
| CDN externs | Conforme | Leaflet és local; CartoDB només per a teseles de mapa (sense tracking) |
| Bàner de consentiment | No requerit | La configuració actual no necessita consentiment explícit |
| Drets ARCO | Documentat | Inclòs a la política de privacitat |
| Transferència fora UE | Cap | GitHub Pages / GoatCounter: servidors UE |

### Aspectes a revisar

| Aspecte | Risc | Recomanació |
|---------|------|-------------|
| `envia.php` | Mig | El formulari envia a un PHP extern no auditat. Verificar validació CSRF, sanitització i política de conservació de dades. |
| analytics.json | Baix | Conté dades agregades sense IP. Considerar restringir l'accés o eliminar el fitxer estàtic públic. |

---

## 4. SEO tècnic — Estat general

| Element | Estat | Notes |
|---------|-------|-------|
| URLs netes | Bé | `/elements/nom-edifici/` sense paràmetres |
| Canonical | Bé | `<link rel="canonical">` a totes les pàgines |
| robots.txt | Bé | Diferent per entorn (staging bloqueja) |
| Sitemap | Parcialment | Generat; verificar a producció |
| `lang="ca"` | Bé | Declarat a `<html>` |
| Títols `<title>` | Bé | Format: Nom — Guies de Barcelona |
| Meta description | Parcial | Fallback global; manquen descriptions individuals |
| Open Graph | Implementat | Fet el 30/08/2026 |
| Twitter Cards | Implementat | Fet el 30/08/2026 |
| Schema.org | Implementat | Fet el 30/08/2026 |
| Pàgines legals | Implementat | Fet el 30/08/2026 |
| HTTPS | Bé | GitHub Pages força HTTPS |
| Velocitat | Mig | Bloquejat per imatges (veure informe-rendiment) |

---

## 5. Pròxims passos recomanats

1. **Descriptions per a fitxes** — Afegir `.Params.descripcio` com a fallback de `meta description` individual a `head.html`
2. **Verificar sitemap de producció** — Un cop fet deploy a guiesbarcelona.elglobusvermell.org
3. **Auditoria `envia.php`** — Revisar el PHP del formulari de contacte per a RGPD i seguretat
4. **Google Search Console** — Activar un cop el domini de producció estigui llest
5. **hreflang** — Preparar quan s'activin els idiomes EN/ES
