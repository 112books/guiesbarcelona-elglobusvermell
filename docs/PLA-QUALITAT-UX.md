# Pla de qualitat: accessibilitat, seguretat i UX mòbil

**Projecte:** guiesbarcelona.elglobusvermell.org  
**Data:** 2026-07-18  
**Basat en:** auditoria automàtica de codi + cas d'ús real (guia de camp en telèfon)

## Context i cas d'ús prioritari

El web s'usa principalment en telèfons intel·ligents a peu de carrer: l'usuari busca un edifici, veu on és al mapa, obre la fitxa i llegeix les dades. La connexió pot ser dolenta (3G), el sol fa difícil veure la pantalla, i s'usa amb una mà. Totes les decisions de disseny han de prioritzar aquest context.

Segon cas d'ús: desktop en context editorial (preparació de visita, consulta de dades).

---

## FASE 1 — Accessibilitat bàsica (WCAG 2.1 AA)
**Prioritat: alta. Requeriment legal i de qualitat.**

### 1.1 Focus visible per teclat i lectors de pantalla

**Problema:** Botons i links creats dinàmicament amb JS (acordions, filtres, marcadors) no tenen `:focus-visible` visible. Navegació per teclat invisible.

**Solució:**
```css
/* A main.css: afegir a la secció de reset */
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
  border-radius: 2px;
}
button:focus-visible,
a:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
}
```

**Fitxers afectats:** `themes/guiesbcn-elglobusvermell/assets/css/main.css`

### 1.2 aria-controls als acordeons

**Problema:** Botons d'acordió (`llistat-grup-capsalera`) tenen `aria-expanded` però no `aria-controls`.

**Solució a mapa.js:** Quan es crea el botó, afegir ID al contingut i vincular-lo:
```javascript
cos.id = 'grup-' + i;
btn.setAttribute('aria-controls', 'grup-' + i);
```

**Fitxers afectats:** `themes/guiesbcn-elglobusvermell/assets/js/mapa.js`

### 1.3 Alt text al logo del header

**Problema:** `alt=""` al logo del header dins un `<a>` sense `aria-label` → lectors de pantalla diuen "link" sense descripció.

**Solució:**
```html
<a href="{{ "/" | absURL }}" aria-label="El Globus Vermell — Inici">
  <img src="..." alt="" aria-hidden="true">
</a>
```

**Fitxers afectats:** `themes/guiesbcn-elglobusvermell/layouts/partials/header.html`

### 1.4 Contrast de borders

**Problema:** `--color-border: #e5e5e5` és quasi invisible sobre blanc (ratio 1.1:1).

**Solució:** Canviar a `#d0d0d0` (ratio 1.4:1 — acceptable per a borders decoratius no portadors d'informació). Els borders que sí porten informació (separadors de seccions) han d'arribar a 3:1.

---

## FASE 2 — UX mòbil (prioritat alta per cas d'ús)

### 2.1 Mida de zones tàctils (tap targets)

**Estàndard WCAG 2.5.5:** mínim 44×44px de zona tàctil.

**Problemes identificats:**
- Links de nav a fitxa (`← Anterior · Tots · Següent →`): text pur sense padding
- Botons d'acordió: ok en altura però potser estrets

**Solució:**
```css
/* Fitxa nav: botons tàctils adequats */
.fitxa-nav a {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 0.75rem;
}

/* Acordió: zona tàctil adequada */
.llistat-grup-capsalera {
  min-height: 48px;
}
```

### 2.2 Feedback tàctil visual

**Problema:** Links i botons no tenen feedback visual quan es premen (`:active`). En mòbil no hi ha hover, l'únic feedback és `:active`.

**Solució:**
```css
a:active,
button:active,
.llistat-grup-capsalera:active {
  opacity: 0.7;
  transition: opacity 0.05s;
}
```

### 2.3 Tipografia responsive

**Problema:** Títols de fitxa (`h1`) i textos principals es basen en `clamp()` però no s'ha provat en 320px (iPhone SE antic).

**Solució:** Verificar i ajustar clamp:
```css
/* Actual: clamp(2rem, 4vw, 3.5rem) — a 320px = 2rem = 32px (ok) */
/* Però cos de text: font-size base 1rem = 16px a tots els tamanyos — ok */
.fitxa-titol { font-size: clamp(1.5rem, 4vw, 2.5rem); }
```

### 2.4 Mapa en mòbil: navegació millorada

**Context:** En un mapa de camp, l'usuari vol:
1. Veure on és (geolocalització)
2. Buscar un edifici concret
3. Filtrar per publicació

**Millores:**
- Afegir botó "Centrar a la meva ubicació" (Leaflet `L.control.locate` o implementació simple)
- El popup del marcador ha de ser prou gran per ser llegit amb llum solar (font-size min 16px)
- Opció de fullscreen del mapa en mòbil

**Implementació:**
```javascript
// Botó geolocalització simple (sense plugin extern)
var btnGeo = L.control({ position: 'bottomright' });
btnGeo.onAdd = function() {
  var div = L.DomUtil.create('button', 'mapa-btn-geo');
  div.innerHTML = '📍';
  div.setAttribute('aria-label', 'Centrar al meu lloc');
  div.onclick = function() {
    map.locate({ setView: true, maxZoom: 17 });
  };
  return div;
};
btnGeo.addTo(map);
```

### 2.5 Popup del mapa: disseny per mòbil

**Problema actual:** Popup petit, difícil de llegir i clicar amb el sol.

**Solució CSS:**
```css
.leaflet-popup-content {
  font-size: 1rem;
  line-height: 1.4;
  min-width: 160px;
}
.leaflet-popup-content a {
  display: block;
  padding: 0.5rem 0;
  font-weight: 600;
  color: var(--pub-color, var(--color-accent));
}
```

### 2.6 Filtre de publicació accessible en mòbil

**Problema:** Els botons de filtre (publicacions) poden ser massa petits en mòbil i ocupen molt espai horitzontal.

**Solució proposada:** En mòbil (<48rem), convertir els filtres en un `<select>` natiu o una interfície de scroll horitzontal amb snap:
```css
@media (max-width: 48rem) {
  .filtres-pubs {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    gap: 0.5rem;
    padding-bottom: 0.5rem;
  }
  .filtres-pubs button {
    scroll-snap-align: start;
    flex-shrink: 0;
    white-space: nowrap;
  }
}
```

---

## FASE 3 — Rendiment mòbil

### 3.1 Imatges responsive (srcset)

**Problema:** `<img src="...">` sense `srcset`. Un mòbil descarrega la mateixa imatge que un monitor 4K.

**Solució a Hugo template:**
```html
{{ if .Params.foto }}
<div class="fitxa-imatge">
  <img src="{{ .Params.foto | absURL }}"
       srcset="{{ .Params.foto | absURL }} 800w,
               {{ .Params.foto | absURL }} 400w"
       sizes="(max-width: 48rem) 100vw, 64rem"
       alt="{{ .Title }}"
       loading="lazy"
       width="800" height="450">
</div>
{{ end }}
```

**Nota:** Requereix que les imatges estiguin disponibles en múltiples mides (pipeline d'imatges Hugo o CDN). A curt termini, afegir `width` i `height` per evitar layout shift (CLS).

### 3.2 Leaflet: carrega condicional

**Problema:** Leaflet (150KB JS + 30KB CSS) es carrega a totes les pàgines amb `Section = "elements"`.

**Solució a termini:** Usar `<script defer>` i carregar Leaflet només si el mapa és visible al DOM. A curt termini, afegir `defer`:

```html
<!-- baseof.html -->
<script src="{{ $leaflet.RelPermalink }}" defer></script>
```

### 3.3 Preconnect a CDNs

**Solució (head.html):**
```html
<link rel="preconnect" href="https://a.basemaps.cartocdn.com">
<link rel="preconnect" href="https://b.basemaps.cartocdn.com">
<link rel="dns-prefetch" href="https://a.basemaps.cartocdn.com">
```

---

## FASE 4 — Seguretat

### 4.1 innerHTML → textContent / createElement

**Problema:** `mapa.js:486-490` construeix HTML amb `innerHTML` usant `p.url` i `p.title` de Hugo data. Risc baix però no és best practice.

**Solució:**
```javascript
// En lloc de:
li.innerHTML = '<a href="' + p.url + '">' + p.title + '</a>';

// Usar:
var a = document.createElement('a');
a.href = p.url;
a.textContent = p.title;
li.appendChild(a);
```

Aplicar a tots els casos d'innerHTML amb dades externes.

### 4.2 Content Security Policy

**Problema:** Sense CSP, qualsevol script inline pot executar-se.

**Solució a `_headers` (per Netlify/Cloudflare) o al servidor:**
```
Content-Security-Policy: 
  default-src 'self';
  script-src 'self' 'nonce-{NONCE}' https://gc.zgo.at;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https://*.cartocdn.com https://*.openstreetmap.org;
  connect-src 'self' https://gc.zgo.at https://*.cartocdn.com;
  frame-ancestors 'none';
```

**Nota:** Staticrypt usa scripts inline → cal `'unsafe-inline'` o nonces. Cal investigar compatibilitat.

### 4.3 Headers de seguretat HTTP

Afegir a la configuració del servidor/CDN:
```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(self)
```

---

## FASE 5 — Correccions menors

### 5.1 Acordió: animation correcta

**Problema:** `max-height: 5000vh` amb transició CSS causa stutter.

**Solució:** Usar JS per calcular l'altura real i animar amb `max-height` precís:
```javascript
// Al click del botó:
cos.style.maxHeight = expanded ? '0' : cos.scrollHeight + 'px';
```

### 5.2 Index alfabètic sticky en mòbil

**Problema:** `.llistat-index` fa `position: sticky; top: var(--header-height)` però quan el header es fa petit, l'index no s'ajusta.

**Solució:** Usar CSS custom property actualitzada per JS quan el header canvia:
```javascript
document.addEventListener('scroll', function() {
  var h = header.offsetHeight;
  document.documentElement.style.setProperty('--header-actual-height', h + 'px');
});
```

### 5.3 Popup del mapa: Adreça visible

**Millora UX:** El popup del marcador hauria de mostrar l'adreça i un link directe a Google Maps, no només el títol.

```javascript
var popup = '<strong>' + p.title + '</strong>';
if (p.adreca) popup += '<br><small>' + p.adreca + '</small>';
popup += '<br><a href="' + p.url + '">Veure fitxa →</a>';
marker.bindPopup(popup);
```

---

## Ordre d'implementació recomanat

| Fase | Tasca | Impacte | Esforç | Fitxers |
|------|-------|---------|--------|---------|
| 1.1 | Focus visible | Alt | Baix | main.css |
| 1.3 | Alt logo header | Alt | Baix | header.html |
| 2.1 | Tap targets nav fitxa | Alt | Baix | main.css |
| 2.2 | Feedback tàctil `:active` | Mig | Baix | main.css |
| 2.5 | Popup mòbil millorat | Alt | Mig | main.css, mapa.js |
| 4.1 | innerHTML → createElement | Mig | Mig | mapa.js |
| 1.2 | aria-controls acordió | Mig | Baix | mapa.js |
| 2.4 | Botó geolocalització | Alt | Mig | mapa.js |
| 2.6 | Filtres scroll horitzontal mòbil | Mig | Mig | main.css |
| 3.3 | Preconnect CDNs | Baix | Baix | head.html |
| 3.2 | Leaflet defer | Mig | Baix | baseof.html |
| 3.1 | Imatges srcset | Alt | Alt | single.html + pipeline |
| 5.1 | Acordió animation | Baix | Mig | mapa.js, main.css |
| 4.2 | CSP headers | Mig | Alt | config servidor |

---

## Notes per a continuïtat

- **Testar a:** iPhone SE (320px), iPhone 14 (390px), iPad (768px), desktop (1440px)
- **Eines recomanades:** Chrome DevTools > Lighthouse, axe DevTools (accessibilitat), WebPageTest (rendiment)
- **Prioritat màxima mòbil:** La primera pantalla que veu l'usuari és el mapa. Ha de carregar en < 3s amb 3G.
- **Staticrypt:** Qualsevol canvi a CSP ha de verificar compatibilitat amb l'script inline de desencriptació.
