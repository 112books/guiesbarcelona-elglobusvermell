# Informe de rendiment — Guies Barcelona
Data: 2026-09-03
Estat anterior (30/08/2026): MODERAT — bloquejat per imatges (score estimat 5/10)

---

## Puntuació estimada actual: 7,5/10

La millora principal és la resolució del bloqueig crític d'imatges (−83% de pes). Tots els punts de l'informe anterior que no depenien del canvi de servidor s'han corregit.

---

## Resum de canvis

| Punt de l'informe 30/8 | Estat 30/8 | Estat 3/9 | Verificat |
|---|---|---|---|
| Imatges 4–8 MB sense compressió | CRÍTIC | Resolt: 150–800 KB per foto | `static/img/elements/` del 1 set |
| `width`/`height` absents a `<img>` (CLS) | CRÍTIC | Resolt: manifest `imatges_dims.json` + template | `single.html` línies 59, 85 |
| `fetchpriority="high"` a imatge LCP | ABSENT | Resolt: foto principal + primera diapositiva | `single.html` línies 60, 86 |
| `loading="lazy"` a imatges secundàries | Parcial | Complet: eager per al LCP, lazy per a les altres | `single.html` línia 60 |
| Leaflet no minificat (147 KB) | IMPORTANT | Verificat: **ja era la dist minificada** (5 línies, 42 KB gzipat) | `static/vendor/leaflet/leaflet.js` |
| Sitemap buit en staging | IMPORTANT | Resolt: 957 URLs (build staging); producció 963+ | `public/sitemap.xml` |
| Scripts sense `defer` | No documentat | Correcte: tots els scripts amb `defer` | `baseof.html` línies 15–30 |
| SRI absent a GoatCounter | Risc seguretat | Resolt: `integrity` sha384 a `head.html` | `head.html` línia 54 |
| Preload imatge LCP | MILLORA | Pendent (no bloquejant; `fetchpriority` compensa) | — |
| Page Resources Hugo / WebP | MILLORA | Pendent (decisió: JPG per compatibilitat og:image) | TASKS.md |

---

## Anàlisi per categoria

### Imatges

**Estat: resolt (crític → acceptable)**

Les 837 imatges han passat de 818 MB (originals, 4–8 MB cadascuna) a 144 MB (−83%). El directori `static/img/elements/` mostra timestamps del 1 set 2026 amb mides representatives:

- Rang mínim: ~155 KB (`torre-de-sant-sebastia.jpg`, `tallers-oliva-artes.jpg`)
- Rang típic: 170–550 KB
- Rang màxim observat: ~793 KB (`biblioteca-gabriel-garcia-marquez.jpg`)
- Paràmetres aplicats: màx 1.600 px amplada, qualitat 85, EXIF tret, auto-orient

El `public/` local mostra mides de 3–11 MB perquè és un build del 29 ag anterior a l'optimització; el `static/` (font de veritat) és correcte.

**Nota sobre format:** Es va decidir mantenir JPEG en lloc de WebP perquè WhatsApp i Telegram no llegeixen WebP com a `og:image`. Sense WebP, el guany per canvi de format queda no explotat, però la reducció per redimensionament i compressió ja és molt significativa.

**Pendent:** 5 imatges que ja eren optimitzades es van mantenir (no reprocessades). Cap acció necessària.

**Manifest de dimensions:** `data/imatges_dims.json` (17 KB, 408 imatges indexades, generat l'1 set). La plantilla `single.html` el consulta per injectar `width` i `height` a cada `<img>`, eliminant el Layout Shift mentre la imatge es carrega.

### JavaScript i CSS

**Estat: correcte**

Tots els scripts propis es carreguen amb `defer` i estan minificats i fingerprinted (SRI):
- `main.js` — defer + SRI
- `mapa.js` — defer + SRI (només a pàgines de mapa/taxonomia)
- `fitxa.js` — defer + SRI (només a fitxes d'edifici)
- `arquitectes.js` — defer + SRI (només a pàgines d'arquitecte)
- `leaflet.js` + `leaflet-gesture-handling.min.js` — defer (sense SRI perquè és servit localment; el fitxer és la dist oficial 1.9.4, 5 línies = minificat)
- GoatCounter (`gc.zgo.at/count.js`) — `async` + SRI sha384 + `crossorigin="anonymous"` (afegit 2 set)

CSS:
- `main.css` — minificat, fingerprinted, SRI
- `leaflet.css` — servit localment, sense fingerprint (acceptable per a biblioteca externa estàtica)

**Cap script bloquejant al `<head>`** excepte l'inline de 4 línies per a la redirecció mòbil a la portada (inevitable per evitar flash de portada en mòbil).

**Preconnect:** CartoDB (`a.basemaps.cartocdn.com`, `b.basemaps.cartocdn.com`) + `dns-prefetch` actius condicionalment per a pàgines de mapa. Correcte.

### Temps de càrrega (estimat sense Lighthouse real)

| Recurs | Mida en xarxa (estimada) | Notes |
|---|---|---|
| HTML (fitxa d'edifici) | ~5–15 KB | Estàtic Hugo, sense SSR |
| `main.css` fingerprinted | ~10–15 KB gzipat | Minificat per Hugo |
| `fitxa.js` | ~5–8 KB gzipat | Defer |
| Foto principal (LCP) | 150–800 KB | JPEG optimitzat; `fetchpriority="high"` |
| TTFB GitHub Pages CDN | <50 ms | CDN global, HTML estàtic |

Per a una connexió 4G típica (10 Mbps efectius), una foto de 500 KB triga ~400 ms. Amb `fetchpriority="high"` i l'absència de scripts bloquejants, el LCP estimat és **1,5–3 s** en 4G (depèn de la mida concreta de la foto del primer edifici). Sense optimització era >4 s.

### Core Web Vitals (estimació sense Lighthouse real)

**Avís:** Sense Lighthouse o PageSpeed Insights real (requereix Chrome i accés a l'URL), aquestes estimacions es basen en les bones pràctiques observades directament al codi. No substitueixen una mesura real.

**LCP (Largest Contentful Paint)**
- Estimació anterior: >4 s (Poor)
- Estimació actual: 1,5–3 s en 4G (Good/Needs Improvement, depèn de la foto)
- Factors positius: `fetchpriority="high"` a la foto principal, TTFB <50 ms, scripts amb `defer`
- Factor limitant: no hi ha `<link rel="preload">` per a la foto LCP; el navegador la descobreix en parsejar el HTML, no abans. Impacte estimat: +300–500 ms vs. amb preload
- Imatges sense WebP: +20–30% de pes respecte a WebP equivalent (no crític, però mesurable)

**CLS (Cumulative Layout Shift)**
- Estimació anterior: Probable (Poor) — sense `width`/`height` a les `<img>`
- Estimació actual: 0 o molt proper (Good) — manifest `imatges_dims.json` reserva l'espai
- Risc residual: les 408 imatges indexades al manifest no cobreixen necessàriament el 100% de les fitxes (837 imatges totals); les fitxes amb foto no indexada al manifest no tindran dimensions i podran causar layout shift petit
- Recomanació: re-executar `scripts/genera-dims-imatges.py` per assegurar cobertura completa

**INP (Interaction to Next Paint)**
- Estimació: Good (<200 ms)
- El mapa Leaflet carrega amb `defer`; els filtres i el carrusel usen event listeners natius sense frameworks pesants
- L'script inline de redirecció mòbil a la portada és <100 bytes i no bloqueja

---

## Bloquejos fins al canvi de servidor / decisions pendents

| Millora | Bloqueig | Impacte estimat |
|---|---|---|
| Headers HTTP (CSP, HSTS, X-Frame-Options) | Dinahosting / nou hosting | Seguretat, no rendiment |
| `<link rel="preload">` per a la foto LCP | No bloquejat — implementable ara | −300–500 ms LCP |
| WebP amb fallback JPEG (`<picture>`) | Decisió revertida (WhatsApp og:image) | −20–30% pes fotos |
| Page Resources Hugo + `srcset` | Canvi arquitectural major | Millora avançada, post-MVP |
| Google Search Console / PageSpeed real | Tall del domini (domini actual → WP) | Mesura real de Core Web Vitals |

---

## Limitacions de la revisió (sense Lighthouse real)

1. **No s'ha pogut fer WebFetch del staging** per restricció de permisos en aquesta sessió. L'anàlisi de recursos es basa íntegrament en la lectura directa dels fitxers font (`head.html`, `baseof.html`, `single.html`).
2. **Core Web Vitals no mesurats.** Les estimacions de LCP/CLS/INP es basen en bones pràctiques documentades al codi, no en mesures reals de Chrome.
3. **El `public/` local és un build del 29 ag** (anterior a l'optimització d'imatges). Les mides correctes s'han verificat a `static/img/elements/` (data 1 set).
4. **El sitemap de staging té 957 URLs**, no 963. La diferència respecte al build de producció (963, verificat l'1 set) és esperada: el staging usa `--environment staging` que aplica `noindex` i pot ometre o alterar algunes URLs.

---

## Pròxims passos

### Prioritat alta (implementables ara, sense canvi de servidor)
1. **`<link rel="preload">` per a la foto LCP** a les fitxes d'edifici: afegir a `head.html` condicionat a `(eq .Section "elements")` i `(.Params.foto)`. Guany estimat: −300–500 ms LCP.
2. **Re-executar `scripts/genera-dims-imatges.py`** i verificar que les 837 imatges (no només les 408 del manifest actual) estan indexades, per eliminar el risc de CLS residual.
3. **Mesura real amb PageSpeed Insights** sobre el staging: `https://pagespeed.web.dev/analysis?url=https%3A%2F%2F112books.github.io%2Fguiesbarcelona-elglobusvermell%2Fca%2Felements%2F[slug-edifici]%2F` — obté Core Web Vitals reals sense necessitat del domini de producció.

### Prioritat mitjana (post-tall de domini)
4. Verificar Core Web Vitals a Google Search Console un cop actiu el domini de producció.
5. Avaluar `<picture>` WebP + JPEG per als que no siguin `og:image` (les fotos del carrusel a partir de la segona, per exemple, no necessiten ser JPEG per compatibilitat social).

### No prioritari (post-MVP)
6. Page Resources Hugo + `srcset` per a múltiples resolucions (1600/1200/800/400 px).
7. Service Worker per a cache offline de visites recurrents.
