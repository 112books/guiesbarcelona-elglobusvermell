---
title: "Accessibilitat"
description: "Declaració d'accessibilitat del web Guies de Barcelona: WCAG 2.1 nivell AA, navegació per teclat, text alternatiu i lectura en veu alta de les fitxes."
---

## Declaració d'accessibilitat

Guies de Barcelona d'El Globus Vermell treballa per fer aquest lloc web accessible, seguint com a referència les **Pautes d'Accessibilitat pel Contingut Web (WCAG) 2.1, nivell AA**, l'estàndard de referència a la Unió Europea (Directiva (UE) 2016/2102) i a l'Estat espanyol (Reial Decret 1112/2018).

Aquesta és una declaració de compromís i mesures aplicades, no una certificació d'auditoria externa formal.

## Mesures aplicades

- **Estructura semàntica**: capçaleres jeràrquiques (H1-H2), regions marcades amb `role` i `aria-label` (mapa, navegació, seccions de contingut)
- **Text alternatiu**: imatges de contingut amb atribut `alt` descriptiu (el peu de foto de cada fitxa fa de text alternatiu); elements decoratius amb `alt` buit, com recomana la norma
- **Navegació per teclat**: enllaç de salt directe al contingut principal com a primera parada del tabulador; navegació principal, mapa i filtres operables sense ratolí
- **Carrusel de fotografies operable amb teclat**: fletxes esquerra/dreta per passar d'imatge, selectors amb etiqueta i estat («premat») per a lectors de pantalla, indicador de posició «Diapositiva X de Y» i àrea de toc de 44 px
- **Focus visible**: contorn destacat al rebre el focus per teclat a tots els elements interactius (filtres del mapa, carrusel, navegació)
- **Contrast de color**: paleta revisada per complir la ràtio mínima de 4.5:1 en text; l'enllaç del peu de pàgina i el text de mostra del camp de cerca es van ajustar el setembre de 2026
- **Pàgina actual indicada**: la navegació principal marca la secció on ets (`aria-current`)
- **Icones amb etiqueta accessible**: el botó d'informació de cada publicació del mapa té icona i text per a lectors de pantalla
- **Responsive**: disseny adaptable a mòbil, tauleta i escriptori
- **Idioma declarat**: l'atribut `lang` del document coincideix amb l'idioma del contingut
- **Lectura en veu alta de les fitxes d'edifici**: text a veu (TTS) mitjançant la Web Speech API del navegador; botó a cada fitxa per escoltar el contingut (títol, adreça, any, arquitectes i descripció)

## Limitacions conegudes

- El mapa interactiu (Leaflet) té suport parcial de teclat heretat de la llibreria; s'està revisant
- Els formularis (contacte i avís de correcció) encara no anuncien els camps obligatoris ni els errors als lectors de pantalla; pendent de millora

## Estàndards que complim

{{< badges-accesibilitat >}}

## Tecnologia utilitzada

Aquest lloc s'ha construït amb:

- **Hugo** — generador de lloc estàtic (Go)
- **HTML5 / CSS3 / JavaScript** — maquetació i interactivitat (mapa, filtres, llistats)
- **Leaflet + OpenStreetMap** — mapa interactiu
- **Web Speech API** — text a veu natiu del navegador per a la lectura de les fitxes d'edifici
- **Python** — scripts de migració i importació de contingut
- **PHP** — proxy d'autenticació per a l'editor de contingut (Sveltia CMS), previst a LinuxBCN
- **GitHub Pages** — allotjament actual del web (migració al servidor de producció, pendent)
- **GoatCounter** — estadístiques de visites respectuoses amb la privacitat

## Contacte

Si detectes cap problema d'accessibilitat en aquest lloc, escriu-nos a [info@elglobusvermell.org](mailto:info@elglobusvermell.org).
