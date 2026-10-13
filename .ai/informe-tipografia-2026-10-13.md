# Proposta de tipografia — Guies Barcelona (13/10/2026)

**Origen:** pregunta d'en Xavi (correu 9/10, ref. GR3 · C10): «Sobre la
tipografia, en podem escollir una altra? Qualsevol? D'unes concretes? És fàcil
fer el canvi?»

**Estat actual:** el web fa servir la **pila de tipus del sistema**
(`-apple-system, Segoe UI, Roboto…`). No carrega cap fitxer de lletra extern:
zero cost i zero dependències, però el resultat canvia segons el dispositiu.

## Condicions

- **Llicència oberta** (OFL o equivalent) → es pot instal·lar lliurement.
- **Autoallotjada** al nostre servidor (sense CDN de Google ni de tercers),
  coherent amb el criteri del projecte de no dependre de Google.
- Canvi fàcil: es defineix una variable i uns `@font-face`; s'aplica a tot el web.

## Tres opcions

### Opció 1 — Instrument Sans (recomanada)
- **Autor:** Instrument (Rodrigo Fuenzalida i Jordan Egstad). **Llicència:** SIL OFL 1.1.
- **Caràcter:** sans neutra, moderna i lleugerament estreta; molt llegible en
  pantalla i amb un punt tècnic i actual.
- **Enllaç de mostra:** https://fonts.google.com/specimen/Instrument+Sans
- **Codi font:** https://github.com/Instrument/instrument-sans
- **Per què:** és la que millor encaixa amb un projecte d'arquitectura i
  urbanisme: discreta, contemporània i sense estridències.

### Opció 2 — Public Sans
- **Autor:** US Web Design System (General Services Administration). **Llicència:** SIL OFL 1.1.
- **Caràcter:** institucional, cívica i molt llegible; tons neutres.
- **Enllaç de mostra:** https://public-sans.design/
- **Codi font:** https://github.com/uswds/public-sans
- **Per què:** dona un to de servei públic i rigorós, adient per a guies de
  patrimoni i espai públic.

### Opció 3 — Space Grotesk (títols) + cos neutre
- **Autor:** Florian Karsten. **Llicència:** SIL OFL 1.1.
- **Caràcter:** geomètrica amb caràcter, to tècnic (recorda els rètols de
  plànol). Els títols guanyen personalitat; el cos es quedaria amb una sans
  neutra (Instrument o Public Sans) per no cansar la lectura.
- **Enllaç de mostra:** https://fonts.floriankarsten.com/space-grotesk
- **Codi font:** https://github.com/floriankarsten/space-grotesk

## Recomanació

**Instrument Sans** per a tot el web. Si es vol més personalitat als títols,
l'opció 3 (Space Grotesk als títols) és la més distintiva.

## Com s'aplicaria

1. Descarregar els fitxers `.woff2` de la família triada i desar-los a
   `static/fonts/`.
2. Afegir els `@font-face` i canviar la variable `--font-sans` a `main.css`.
3. Verificar la càrrega (pes, `font-display: swap`) i el contrast WCAG.

*Cap dels tres casos afegeix cap dependència externa.*

---
*Document intern LinuxBCN. Font canònica en Markdown; cap PDF derivat.*
