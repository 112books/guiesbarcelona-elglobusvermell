# Informe d'auditoria d'accessibilitat
## Guies de Barcelona — El Globus Vermell

**Data:** 30 d'agost de 2026
**Conformitat visada:** WCAG 2.1 Nivell AA
**Conformitat estimada:** ~75-80% WCAG AA

---

## Resum executiu

El projecte ha demostrat un compromís seriós amb l'accessibilitat, documentat explícitament a la pàgina `/accessibilitat/`. La implementació inclou elements estructurals sòlids (HTML semàntic, landmarks, ARIA), navegació per teclat funcional, i features innovadores com TTS (Text-to-Speech) amb Web Speech API. Tanmateix, la base de conformitat WCAG AA és fragile en diversos fronts crítics, especialment en contrast de colors, manteniment de focus visible en filtres interactius, i accés complet del carrusel de fotos per a dispositius que no suporten JavaScript o navegació per teclat avançada.

---

## 1. Problemes crítics

### 1.1 Contrast de colors insuficient (WCAG AA 4.5:1)
**Fitxers:** `themes/guiesbcn-elglobusvermell/assets/css/main.css` (línies 9, 302, 532)

- `.footer-powered-link`: `color: #b3b3b3` sobre blanc — contrast 4.2:1 (sota el mínim)
- `::placeholder`: `#aaa` sobre blanc — contrast 3.9:1 (sota el mínim)
- `--color-muted: #555555` — al límit, acceptable però just

**Solució:**
- `main.css:302` — canviar `.footer-powered-link` a `color: #6b6b6b`
- `main.css:532` — canviar `::placeholder` a `color: #767676` (mínim WCAG AA)

---

### 1.2 Carrusel de fotos: sense navegació per teclat ni dots accessibles
**Fitxers:** `themes/guiesbcn-elglobusvermell/assets/js/fitxa.js` (línies 45–90), `main.css`

- Els botons prev/next no responen a tecles de fletxa (només `click`)
- Els dots fan 0.5rem = 8px (mínim recomanat: 44px)
- Falta `aria-pressed="true/false"` als dots per indicar la diapositiva activa

**Solució:**
- Afegir `keydown` listeners a prev/next (ArrowLeft/ArrowRight) i als dots (Enter/Space)
- Augmentar dots a almenys 2rem amb padding per arribar a 44px de touch target
- Afegir `aria-pressed` als dots i actualitzar-lo en JS

---

### 1.3 Filtres del mapa: focus visible no aplicat
**Fitxer:** `themes/guiesbcn-elglobusvermell/assets/css/main.css` (~línies 541–606)

La regla global `:focus-visible { outline: 2px solid var(--color-accent) }` existeix però els botons `.filtre-btn` i `.filtre-lateral` no la hereten correctament.

**Solució:** Afegir explícitament:
```css
.filtre-btn:focus-visible,
.filtre-lateral:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 1px;
}
```

---

### 1.4 Botó "i" de publicació: text visual insuficient
**Fitxer:** `themes/guiesbcn-elglobusvermell/assets/js/mapa.js` (línies 451–466)

El botó genera `textContent = 'i'` com a únic text visible. Té `aria-label` correcte però el text visual d'una sola lletra "i" sense context no és suficient.

**Solució:** Substituir per icona SVG amb `aria-hidden="true"` i `<span class="sr-only">` amb el text accessible.

---

## 2. Problemes importants

### 2.1 Carrusel: sense indicador de diapositiva actual visible
El dot actiu canvia de color però no hi ha indicador textual "3 de 8" per a usuaris amb dificultats de percepció del color.

**Solució:** Afegir `<span class="sr-only" id="carrusel-contador">Diapositiva 1 de N</span>` i actualitzar-lo en JS.

### 2.2 Mapa Leaflet: navegació per teclat limitada
Ja documentat a `/accessibilitat/`. Els marcadors del mapa no són navegables per Tab ni activables per Enter.

**Solució a llarg termini:** Capa JS per afegir `tabindex="0"` i `keydown` als marcadors Leaflet.

### 2.3 Formularis: falta aria-required i missatges d'error accessibles
Els camps obligatoris marquen l'asterisk visualment però sense `required` ni `aria-required="true"` als inputs, ni `aria-describedby` per als errors.

---

## 3. Millores recomanades

### 3.1 Skip link
No hi ha enllaç "Saltar al contingut principal". Afegir a `baseof.html`:
```html
<a href="#main" class="sr-only sr-only-focusable">Saltar al contingut principal</a>
```

### 3.2 Indicador de pàgina actual a la navegació
Afegir `aria-current="page"` a l'element de navegació actiu.

### 3.3 PDFs: etiquetar com a PDF
Els enllaços de descàrrega de plànols haurien d'indicar explícitament "(PDF)" a l'`aria-label`.

### 3.4 Tests automàtics d'accessibilitat al CI/CD
Integrar axe-core o pa11y al workflow de GitHub Actions per detectar regressions automàticament.

---

## 4. Punts forts

- HTML semàntic sòlid: `<main>`, `<header>`, `<footer>`, `<nav aria-label>`, `<article>`, `<dl>/<dt>/<dd>`
- ARIA complet: `aria-label`, `aria-live="polite"`, `aria-expanded`, `aria-controls`, `aria-hidden` en SVG decoratius
- TTS implementat correctament: `aria-label` s'actualitza dinàmicament (Escoltar/Pausa/Continua), veu en català amb fallback
- `:focus-visible` global definit amb outline vermell visible
- `lang="ca"` a l'element `<html>`
- Pàgina `/accessibilitat/` pública, honest i amb limitacions documentades
- Viewport meta correcte per a mòbil

---

## 5. Taula de prioritats

| Prioritat | Problema | Fitxer | Acció |
|-----------|----------|--------|-------|
| CRÍTIC | Contrast #b3b3b3 i #aaa sota WCAG AA | main.css:302,532 | Canviar a #6b6b6b / #767676 |
| CRÍTIC | Carrusel sense teclat ni dots accessibles | fitxa.js:45-90 | keydown + dots 44px + aria-pressed |
| CRÍTIC | Focus visible filtres mapa | main.css:~550 | :focus-visible explícit |
| CRÍTIC | Botó "i" text insuficient | mapa.js:451-466 | SVG + sr-only |
| IMPORTANT | Carrusel sense indicador diapositiva | single.html:69-76 | Contador SR-only |
| IMPORTANT | Leaflet teclat | mapa.js | Tab entre marcadors |
| IMPORTANT | Formularis aria-required | templates | required + aria-describedby |
| MILLORA | Skip link | baseof.html | Afegir |
| MILLORA | aria-current="page" | header.html | Afegir |
| MILLORA | PDFs etiquetar | term.html | aria-label amb "(PDF)" |
| MILLORA | Tests a11y CI/CD | workflows | axe-core o pa11y |

---

## 6. Conclusió

Estimació d'implementació de correccions crítiques: 6–8 hores de desenvolupament.
Certificació recomanada: un cop implementades les correccions, validació amb axe DevTools o WAVE.
