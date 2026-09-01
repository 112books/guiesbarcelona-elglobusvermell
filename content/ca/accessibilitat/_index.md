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
- **Navegació per teclat**: navegació principal, mapa i filtres operables sense ratolí
- **Contrast de color**: paleta dissenyada per complir la ràtio mínima de contrast 4.5:1 en text (dos elements concrets encara pendents d'ajust; vegeu limitacions)
- **Responsive**: disseny adaptable a mòbil, tauleta i escriptori
- **Idioma declarat**: l'atribut `lang` del document coincideix amb l'idioma del contingut
- **Lectura en veu alta de les fitxes d'edifici**: text a veu (TTS) mitjançant la Web Speech API del navegador; boto a cada fitxa per escoltar el contingut (títol, adreça, any, arquitectes i descripció)

## Limitacions conegudes

- El mapa interactiu (Leaflet) té suport parcial de teclat heretat de la llibreria; s'està revisant
- El carrusel de fotografies de les fitxes encara no es pot fer servir amb el teclat; pendent de millora
- Els filtres del mapa no sempre mostren l'indicador de focus en navegar amb teclat; pendent de millora
- Dos elements tenen el contrast per sota del recomanat (l'enllaç de la banda del peu i el text de mostra del camp de cerca); pendent d'ajust
- Manca un enllaç de salt directe al contingut principal per a la navegació amb teclat; pendent

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
