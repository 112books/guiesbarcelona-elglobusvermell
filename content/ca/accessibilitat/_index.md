---
title: "Accessibilitat"
---

## Declaració d'accessibilitat

Guies de Barcelona d'El Globus Vermell treballa per fer aquest lloc web accessible, seguint com a referència les **Pautes d'Accessibilitat pel Contingut Web (WCAG) 2.1, nivell AA**, l'estàndard de referència a la Unió Europea (Directiva (UE) 2016/2102) i a l'Estat espanyol (Reial Decret 1112/2018).

Aquesta és una declaració de compromís i mesures aplicades, no una certificació d'auditoria externa formal.

## Mesures aplicades

- **Estructura semàntica**: capçaleres jeràrquiques (H1-H2), regions marcades amb `role` i `aria-label` (mapa, navegació, seccions de contingut)
- **Text alternatiu**: imatges amb atribut `alt` descriptiu
- **Navegació per teclat**: enllaços i controls interactius (mapa, filtres, botons) operables sense ratolí
- **Contrast de color**: paleta pensada per complir la ràtio mínima de contrast 4.5:1 en text
- **Responsive**: disseny adaptable a mòbil, tauleta i escriptori
- **Idioma declarat**: l'atribut `lang` del document coincideix amb l'idioma del contingut

## Limitacions conegudes

- El mapa interactiu (Leaflet) té suport parcial de teclat heretat de la llibreria; s'està revisant

## Estàndards que complim

<div class="accessibilitat-badges">
  <a href="https://www.w3.org/TR/WCAG21/" target="_blank" rel="noopener noreferrer" class="accessibilitat-badge">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
    <span>WCAG 2.1<br>Nivell AA</span>
  </a>
  <a href="https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf" target="_blank" rel="noopener noreferrer" class="accessibilitat-badge">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
    <span>EN 301 549</span>
  </a>
  <a href="https://www.boe.es/eli/es/rd/2018/09/07/1112" target="_blank" rel="noopener noreferrer" class="accessibilitat-badge">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
    <span>RD 1112/2018</span>
  </a>
</div>

## Tecnologia utilitzada

Aquest lloc s'ha construït amb:

- **Hugo** — generador de lloc estàtic (Go)
- **HTML5 / CSS3 / JavaScript** — maquetació i interactivitat (mapa, filtres, llistats)
- **Leaflet + OpenStreetMap** — mapa interactiu
- **Python** — scripts de migració i importació de contingut
- **PHP** — proxy d'autenticació per a l'editor de contingut (Sveltia CMS), previst a Dinahosting
- **GitHub Pages** — allotjament actual (Dinahosting previst en migrar)
- **GoatCounter** — estadístiques de visites respectuoses amb la privacitat

## Contacte

Si detectes cap problema d'accessibilitat en aquest lloc, escriu-nos a [info@elglobusvermell.org](mailto:info@elglobusvermell.org).
