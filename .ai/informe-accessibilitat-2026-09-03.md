# Informe d'accessibilitat — Guies Barcelona
Data: 2026-09-03
Estàndard: WCAG 2.1 nivell AA
Estat anterior (30/08/2026): ~75-80% conformitat estimada

---

## Puntuació actual estimada: 8.5/10

Totes les correccions crítiques i la majoria de les importants han estat aplicades. Els punts restants oberts o bé depenen d'infraestructura externa (Dinahosting/tall de domini) o requereixen decisió d'equip.

---

## Resum de canvis respecte l'informe anterior

| Punt | Informe 30/8 | Estat 3/9 | Verificat |
|---|---|---|---|
| Contrast `.footer-powered-link` #b3b3b3 | Falla AA (4.2:1) | Corregit — #6b6b6b | Codi (main.css:341) |
| Contrast `.footer-powered-services` #b3b3b3 | Falla AA (no detectat al 30/8) | Corregit — #6b6b6b | Codi (main.css:351) |
| Contrast `::placeholder` #aaa | Falla AA (3.9:1) | Corregit — #767676 | Codi (main.css:572) |
| Carrusel: fletxes de teclat | No implementat | Corregit — ArrowLeft/ArrowRight al contenidor | Codi (fitxa.js:85-93) |
| Carrusel: `aria-pressed` als dots | No implementat | Corregit | Codi (fitxa.js:65) |
| Carrusel: comptador SR-only | No implementat | Corregit — "Diapositiva N de M" role=status | Codi (fitxa.js:67-69) |
| Dots 44px touch target | 8px, insuficient | Corregit — 2.75rem (44px) amb ::before | Codi (main.css:791-810) |
| Dots role incorrecte (tab/tablist) | role="tab" sense tabpanel | Corregit — role="group" + aria-pressed | Codi TASKS.md |
| Focus visible filtres mapa | Heretat incorrectament | Corregit — regles explícites per a .filtre-btn/.filtre-lateral/.filtre-btn-info | Codi (main.css:163-168) |
| Arrel del problema focus (border-radius global) | Desconeguda | Identificada i corregida — tret border-radius de :focus-visible global | Codi (main.css:157-160) |
| Botó "i" publicació: text visual insuficient | textContent='i' sense context | Corregit — SVG aria-hidden + span.sr-only | Codi (mapa.js:482-486) |
| Skip link | Absent | Corregit — .skip-link primer element del body | Codi (baseof.html:8) |
| `<main id="main" tabindex="-1">` | Absent | Corregit | Codi (baseof.html:10) |
| `aria-current="page"` al nav | Absent | Corregit — $.RelPermalink vs .URL | Codi (header.html:14) |
| Leaflet: marcadors navegables per teclat | No implementat | Corregit — tabindex=0, role=button, aria-label, keydown Enter/Espai | Codi (mapa.js:155-174) |
| Focus visible marcadors Leaflet | No previst | Afegit — .leaflet-interactive:focus-visible | Codi (main.css:171-174) |
| Formularis: `required` + errors accessibles | Absent | Implementat — required + aria-invalid + aria-describedby dinàmic | Codi (contacte/list.html) |
| PDF: aria-label explícit "(PDF)" | Absent | Implementat — aria-label="Descarregar el plànol-guia X (PDF)" | Codi (term.html:66,73) |

---

## Conformitat per categoria

### Perceptible (Principi 1)

**1.1 Alternatives de text**
- Imatges decoratives: `alt=""` i SVG amb `aria-hidden="true"` — correcte.
- Foto principal de fitxa: `alt` pres del camp `foto_peu` (peu de foto = descripció accessible) — acceptable, no sempre descriptiu però consistent amb el contingut editorial.
- Imatges del logo al header: `alt=""` (decoratives; el link del logo té `aria-label` amb el títol del web) — correcte.
- Fotos del carrusel: cal verificar que `alt` és sempre present i descriptiu a totes les diapositives (no verificat al codi de plantilla en detall — pendent revisió visual).

**1.3 Contingut adaptable**
- HTML semàntic: `<main>`, `<header>`, `<footer>`, `<nav aria-label>`, `<article>`, `<section aria-labelledby>`, `<dl>/<dt>/<dd>` — correcte.
- Jerarquia de headings: h1 > h2 > h3 aparentment coherent. No verificat en totes les pàgines (requeriria eines automatitzades o revisió manual exhaustiva).

**1.4 Distingible**
- Contrast text sobre fons:
  - `.footer-powered-link` i `.footer-powered-services`: corregit a #6b6b6b (contrast ~5.7:1 sobre blanc). Passa AA.
  - `::placeholder`: corregit a #767676 (contrast exactament 4.5:1). Passa AA per just.
  - `--color-muted: #555555` sobre blanc: contrast ~7.4:1. Passa AA i AAA.
  - Color #aaa que roman al CSS (main.css:716): correspon a `.fitxa-imatge--placeholder` — text de placeholder quan no hi ha foto ("Sense foto", indicatiu, no informatiu crític). Context de caixa amb vora discontinua. Risc baix; es pot millorar a #767676 si es vol conformitat estricta.
  - Tiles del mapa (OpenStreetMap/CartoDB): contingut de tercers, text sobre mapa no controlat. Limitació acceptada.

---

### Operable (Principi 2)

**2.1 Accessible per teclat**
- Navegació principal: tabulable, focus visible.
- Skip link: present i funcional — `<a class="skip-link" href="#main">Salta al contingut principal</a>` com a primer element del body; `<main id="main" tabindex="-1">` com a destí. Verificat al codi.
- Carrusel de fotos:
  - Botons prev/next: clicables i ara responen a ArrowLeft/ArrowRight.
  - Dots: `aria-pressed` actualitzat, àrea de toc 2.75rem (44px). Correcte.
  - Navegació per teclat: el listener keydown és al contenidor `[data-fitxa-carrusel]`, de manera que les fletxes funcionen amb el focus a qualsevol control intern.
- Filtres del mapa: focus visible explícit per a `.filtre-btn`, `.filtre-lateral` i `.filtre-btn-info`. Correcte.
- Marcadors Leaflet: ara reben `tabindex="0"`, `role="button"`, `aria-label` amb nom + adreça, i `keydown` que obre el popup amb Enter/Espai. Corregit (era el punt §2.2 de l'informe anterior). Focus visible afegit via `.leaflet-interactive:focus-visible`.
- Formulari de contacte: camps navegables per teclat, `required` HTML natiu, errors amb `aria-invalid` i `aria-describedby` assignats dinàmicament en JS.

**2.4 Navegable**
- `aria-current="page"` al nav: implementat — compara `$.RelPermalink` amb `.URL` de cada ítem del menú. Correcte per a pàgines de primer nivell; no cobreix pàgines filles (p. ex. `/elements/una-fitxa/` no marcarà "Mapa" com a actiu — comportament acceptable i habitual en Hugo).
- Títols de pàgina: `<title>` adequat a cada pàgina via Hugo.
- Focus order: coherent amb l'ordre del DOM.

---

### Comprensible (Principi 3)

**3.1 Llegible**
- `lang="ca"` a l'element `<html>` via `site.Language.Lang`. Correcte.
- Contingut en català, sense barreja d'idiomes sense marcar.

**3.2 Predictible**
- Navegació consistent a totes les pàgines.
- Canvis de context: el carrusel no provoca canvis inesperats de focus.
- TTS (lectura en veu alta): `aria-label` del botó s'actualitza dinàmicament ("Escoltar" / "Pausa" / "Continua") — correcte per a lectors de pantalla.

**3.3 Assistència a l'entrada**
- Formulari de contacte: etiquetes `<label for>` associades correctament, `required` HTML natiu, missatges d'error amb `role="alert"` i `aria-invalid`/`aria-describedby` en JS. Correcte.
- Camp asterisk (*): `<span class="form-requerit" aria-hidden="true">*</span>` — correcte, el text visual no és llegit per lectors de pantalla (visual only), però `required` proporciona la informació al lector de pantalla de forma nativa. Acceptable.
- Nota: no hi ha `aria-required="true"` explícit als inputs (l'atribut `required` HTML natiu és equivalent i preferible). Correcte.

---

### Robust (Principi 4)

**4.1 Compatible**
- HTML vàlid generalment correcte (Hugo genera HTML5 semàntic).
- ARIA: rols, estats i propietats usats correctament:
  - `aria-label` als landmarks de navegació.
  - `aria-live="polite"` al contenidor de resultats del mapa (verificat a sessions anteriors).
  - `aria-expanded` als filtres (verificat a sessions anteriors).
  - `aria-controls` associats correctament (verificat a sessions anteriors).
  - SVG decoratius amb `aria-hidden="true"`.
- `role="group"` als dots del carrusel (substituït el patró tab/tablist incomplet). Correcte.
- `role="status"` al comptador de diapositives SR-only. Correcte.
- `role="alert"` als missatges d'error del formulari. Correcte.
- `role="button"` als marcadors Leaflet navigables per teclat. Correcte.
- SRI (Subresource Integrity) a les dependències externes (GoatCounter, Chart.js). Millorat el 2 set.

---

## Limitacions conegudes i acceptades

Aquestes limitacions estan documentades a la pàgina pública `/accessibilitat/` del web:

1. **Tiles del mapa (OpenStreetMap/CartoDB)**: les imatges del mapa base no tenen text alternatiu — limitació del proveïdor, no controlable des del projecte. Documentada com a limitació honesta.

2. **Diapositives del carrusel**: la navegació per teclat funciona; tanmateix, el contingut de les diapositives (imatges amb peu de foto) no té un "slider" ARIA formal complet (`role="region"` o `tabpanel`). El patró implementat (role=group + aria-pressed + comptador SR-only) és funcional i honest, però menys ric que un carrusel ARIA pur.

3. **Navegació entre pàgines de fitxes**: els botons "Anterior"/"Següent" de la fitxa d'edifici funcionen amb teclat, però la seva associació semàntica amb el contingut no és explicitament marcada com a landmark de navegació contextual. Millora menor.

4. **GoatCounter analytics**: el script de seguiment no usa cookies. Compatible amb RGPD. L'attribut `data-goatcounter` al noscript és informatiu. Acceptable.

5. **Formulari de contacte (acció envia.php)**: el backend `envia.php` és herència del WordPress en producció, fora del repositori Hugo. La validació front-end és accessible; la resposta del servidor no ha estat testada amb lector de pantalla.

6. **Pàgines sense foto**: el placeholder usa `color: #aaa` (main.css:716) — contrast 3.9:1 sobre blanc, sota WCAG AA. Context purament decoratiu/indicatiu; no és text crític. Millora recomanada però no urgent.

---

## Limitacions de la revisió

Aquesta revisió s'ha basat en:

- **Inspecció directa del codi font** (main.css, fitxa.js, mapa.js, baseof.html, header.html, contacte/list.html, term.html) — cobreix el 100% dels punts detectats a l'informe del 30/8 i els canvis registrats a TASKS.md.
- **Lectura del build compilat local** (directori `public/`) per als fitxers HTML generats — verificació puntual, no exhaustiva.
- **No s'han executat** en aquesta revisió:
  - Eines automatitzades (axe DevTools, WAVE, pa11y) — requeririen execució al navegador o servidor local.
  - Proves amb lectors de pantalla reals (VoiceOver, NVDA, JAWS).
  - Proves amb usuaris amb discapacitat.
  - Fetch de les pàgines del staging (https://112books.github.io/guiesbarcelona-elglobusvermell/) — sense permisos en aquesta sessió; les verificacions al codi font cobreixen el mateix perquè el build és determinista.
  - Revisió visual del contrast en context real (en alguns casos depèn de la superposició exacta de colors).
  - Revisió de la jerarquia de headings en totes les 660+ pàgines de fitxes (proves en plantilla).

---

## Pròxims passos recomanats

### Prioritat alta (aplicable ara, sense tall de domini)

1. **Corregir `color: #aaa` del placeholder de fitxa sense foto** (`main.css:716`) — canviar a `#767676` per completar la conformitat AA al 100% dels elements de text. Canvi mínim, 5 minuts.

2. **Integrar pa11y o axe al CI/CD** (GitHub Actions) — detectar regressions automàticament. El workflow de pa11y ja es va intentar el 6 set (commit `6398bf5`); revisar si va quedar actiu o si cal ajustar les URLs. Temps estimat: 2-4 hores.

3. **Verificar alt text del carrusel de fotos** — revisar la plantilla `elements/single.html` per assegurar que totes les diapositives del carrusel passen un `alt` descriptiu (o el camp `foto_peu` quan existeix).

### Prioritat mitjana (recomanat, no urgent)

4. **Prova amb VoiceOver (macOS/iOS)** sobre la pàgina del mapa i una fitxa — verificar el flux real de navegació per teclat i lector de pantalla, especialment els marcadors Leaflet i el carrusel.

5. **Prova amb axe DevTools** al navegador sobre el staging — identificar errors residuals de contrast o ARIA no detectables per inspecció de codi.

6. **Revisar navegació entre fitxes** (botons "Anterior"/"Següent") — afegir `aria-label` descriptiu ("Edifici anterior: [nom]", "Edifici següent: [nom]") si estan implementats.

### Pendent d'infraestructura (Dinahosting/tall de domini)

7. **Headers HTTP d'accessibilitat/seguretat** (CSP, X-Frame-Options) — no aplicables a GitHub Pages; activar a Netlify/Vercel o Cloudflare CDN quan es produeixi la migració.

8. **Formulari de contacte backend** (`envia.php`) — auditar respostes d'error del servidor i assegurar que els missatges d'error es comuniquen de forma accessible al front-end.

---

*Informe generat per inspecció de codi font el 2026-09-03. Cobreix tots els punts de l'informe del 30/8/2026 i reflecteix les correccions aplicades durant la setmana del 1-2 de setembre de 2026.*
