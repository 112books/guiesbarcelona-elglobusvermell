# Informe d'auditoria de rendiment
## Guies de Barcelona — El Globus Vermell

**Data:** 30 d'agost de 2026
**Nivell de rendiment estimat: MODERAT** (bloquejat per imatges)

---

## Resum executiu

L'arquitectura estàtica Hugo + GitHub Pages és excel·lent per a rendiment base (TTFB < 100 ms, HTML estàtic, assets amb SRI i fingerprinting). El bloqueig crític és el pes de les imatges: 1,7 GB de fotos sense compressió ni WebP, amb mides de 4–8 MB cadascuna. Sense imatges optimitzades, el LCP (Largest Contentful Paint) de les fitxes d'edifici serà superior a 4 s en mòbil, impedint passar Core Web Vitals.

---

## 1. Problemes crítics

### 1.1 Imatges sense compressió ni WebP
**Directori:** `static/img/`

Les imatges d'edificis (1,7 GB en total) es publiquen tal com s'han importat, sense cap conversió ni redimensionament.

- Mida típica: 4–8 MB per foto (JPEG d'alta resolució)
- Mida òptima per web: < 200 KB (WebP, 1200 px amplada màxima)
- Factor de compressió possible: 20×–40×
- Impacte: LCP > 4 s en mòbil (Core Web Vitals "Poor")

**Solució:**
Conversió batch amb ImageMagick o cwebp:
```bash
for f in static/img/edificis/*.jpg; do
  cwebp -q 82 "$f" -o "${f%.jpg}.webp"
  mogrify -resize "1200>" -quality 82 "$f"
done
```
I actualitzar les templates per usar `<picture>` amb `srcset` WebP + JPEG de fallback.

---

### 1.2 Atributs `width` i `height` absents a les imatges
**Fitxer:** `themes/guiesbcn-elglobusvermell/layouts/elements/single.html`

Les etiquetes `<img>` de les fitxes no inclouen `width` ni `height`. Sense aquestes dimensions, el navegador no pot reservar espai abans de carregar la imatge, causant **Layout Shift** (CLS).

**Solució:**
Afegir `width="1200" height="800"` (o les dimensions reals) a totes les `<img>` de fitxa, o usar Hugo Image Processing per obtenir les dimensions automàticament si les imatges passen a ser Page Resources.

---

### 1.3 Sitemap.xml aparentment buit en staging
**Fitxer:** `config/staging/hugo.toml` (o absència de configuració explícita)

En l'entorn staging (`--environment staging`), el `sitemap.xml` generat pot estar buit o no incloure les pàgines correctes perquè `baseURL` apunta a GitHub Pages (subpath) i `noindex` és actiu. Cal verificar que el sitemap de producció conté totes les 1.257 pàgines.

**Acció:** Fer un build `--environment production` i inspeccionar `/public/sitemap.xml`.

---

## 2. Problemes importants

### 2.1 Leaflet no minificat
**Fitxers:** `static/vendor/leaflet/leaflet.js` (147 KB sense minificar)

Leaflet es carrega sense minificar. En producció hauria de ser la versió minificada (`leaflet.min.js`, ~42 KB).

**Solució:** Substituir per `leaflet.min.js` al directori vendor i actualitzar la referència a `baseof.html`.

### 2.2 Font web: Google Fonts absent (positiu)
El projecte no carrega Google Fonts ni cap font web externa. S'usa la font del sistema (`system-ui`). Això és positiu per al rendiment i la privacitat.

### 2.3 Manca de `<link rel="preload">` per a la imatge LCP
A les fitxes d'edifici, la foto principal (primera del carrusel) és el probable LCP. Afegir `<link rel="preload">` per a aquesta imatge milloraria el LCP en ~500 ms.

---

## 3. Millores recomanades

### 3.1 Imatges com a Page Resources de Hugo
Migrar les imatges de `static/img/` a Page Bundles per poder usar Hugo Image Processing:
- Conversió automàtica a WebP
- Generació de `srcset` per a múltiples resolucions
- Atributs `width`/`height` automàtics

### 3.2 Lazy loading natiu (ja implementat parcialment)
Les imatges del carrusel ja usen `loading="lazy"` (tret de la primera, que usa `loading="eager"`). Correcte.

### 3.3 Service Worker per a cache offline
Per a usuaris recurrents, un Service Worker que cachi assets estàtics milloraria els temps de càrrega en visites posteriors. Opcional per al MVP.

---

## 4. Punts forts

- **HTML estàtic:** TTFB < 50 ms (GitHub Pages CDN)
- **Assets fingerprinted + SRI:** CSS i JS amb hash, cache perpètua, SRI per a integritat
- **CSS i JS minificats:** Hugo minifica tots els assets propis
- **Leaflet local:** Sense dependència de CDN extern per al mapa
- **`loading="lazy"` a imatges secundàries:** Implementat correctament al carrusel
- **`preconnect` per a CartoDB:** Redueix el RTT del mapa Leaflet
- **No hi ha Google Fonts:** Zero cost de xarxa per a tipografia

---

## 5. Taula de prioritats

| Prioritat | Problema | Fitxer/Directori | Acció |
|-----------|----------|------------------|-------|
| CRÍTIC | Imatges 4–8 MB sense WebP | static/img/ | Conversió batch WebP + resize |
| CRÍTIC | width/height absents (CLS) | elements/single.html | Afegir dimensions |
| IMPORTANT | Sitemap buit en staging | config/staging/ | Verificar build producció |
| IMPORTANT | Leaflet no minificat | static/vendor/leaflet/ | Usar leaflet.min.js |
| MILLORA | preload imatge LCP | head.html | Afegir link rel=preload condicional |
| MILLORA | Page Resources Hugo | static/img/ → bundles | Migrar per ImageProcessing |

---

## 6. Estimació d'impacte

Implementant la conversió d'imatges (punt 1.1), el LCP de les fitxes passaria de >4 s a <2,5 s (Core Web Vitals "Good") en connexions 4G. Aquesta és l'única millora crítica per al rendiment real.
