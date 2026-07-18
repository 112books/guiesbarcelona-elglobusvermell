# Revisió de contingut — canvis respecte al web original

Aquest document registra **tots els canvis editorials** fets als continguts del web nou respecte al web original (WordPress). El client ha de revisar cada entrada i confirmar si el canvi és correcte o cal revertir-lo.

---

## Com llegir aquest document

Cada entrada té:
- **Pàgina afectada**: URL de la pàgina al web nou (staging)
- **Tipus de canvi**: `Estructura` / `Text` / `URL` / `Contingut eliminat` / `Contingut afegit`
- **Original**: el que hi havia al web de WordPress
- **Nou**: el que hi ha ara al web Hugo
- **Motiu**: per què s'ha fet el canvi
- **Estat**: `Pendent de revisió` / `Confirmat` / `A revertir`

---

## Publicació: GATCPAC

**Pàgina:** `/publicacions/gatcpac/`
**Data edició:** 2026-07-19

---

### 1. Títol introductori en majúscules → minúscules

| Camp | Contingut |
|------|-----------|
| **Original** | `UNA IMMERSIÓ EN L'ARQUITECTURA DE SERT I ELS ARQUITECTES DEL GATCPAC` (text pla, tot en majúscules) |
| **Nou** | `Una immersió en l'arquitectura de Sert i els arquitectes del GATCPAC` (paràgraf normal) |
| **Motiu** | El text en majúscules era un estil del web WP que no té equivalència semàntica en HTML/Markdown. S'ha convertit a text normal. |
| **Estat** | Pendent de revisió |

---

### 2. Secció "El GATCPAC" sense heading → h2

| Camp | Contingut |
|------|-----------|
| **Original** | `El GATCPAC` apareixia com a text pla (sense ser un títol de secció) |
| **Nou** | `## El GATCPAC` (secció d'acordió igual que les altres) |
| **Motiu** | Perquè l'acordió funcioni correctament, totes les seccions han de ser `##`. El contingut és idèntic. |
| **Estat** | Pendent de revisió |

---

### 3. Text introductori lleugerament condensat

| Camp | Contingut |
|------|-----------|
| **Original** | El tercer paràgraf introductori contenia: *"Alhora, es fixen en l'arquitectura vernacular i la construcció tradicional pròpies del país, les quals són, al cap i a la fi, funcionalisme pur."* |
| **Nou** | Aquesta frase s'ha eliminat de la introducció visible (quedava dins l'acordió de tota manera) |
| **Motiu** | Simplificació de la introducció visible. El contingut complet continua a la secció `## El GATCPAC`. |
| **Estat** | Pendent de revisió |

---

### 4. Secció "Josep Lluís Sert i López" → sub-heading corregit

| Camp | Contingut |
|------|-----------|
| **Original** | `## Josep Lluís Sert I López` (la "I" en majúscula per error d'import WP) |
| **Nou** | `## Josep Lluís Sert i López` (corregit) |
| **Motiu** | Error tipogràfic de l'import automàtic de WordPress. |
| **Estat** | Pendent de revisió |

---

### 5. Noms d'arquitectes coautors → h3

| Camp | Contingut |
|------|-----------|
| **Original** | `Josep Torres i Clavé`, `Joan Baptista Subirana Subirana`, `Luis Lacasa Navarro` apareixien com a text pla |
| **Nou** | `### Josep Torres i Clavé`, etc. (sub-títols h3) |
| **Motiu** | Millorar jerarquia visual i accessibilitat. El contingut és idèntic. |
| **Estat** | Pendent de revisió |

---

### 6. Noms d'altres arquitectes → h3 + dates separades

| Camp | Contingut |
|------|-----------|
| **Original** | `Sixte Illescas i Mirosa (Barcelona, 1903 – 1986)` en una sola línia de text pla |
| **Nou** | `### Sixte Illescas i Mirosa` + `(Barcelona, 1903 – 1986)` en línies separades |
| **Motiu** | Millorar jerarquia visual. El contingut és idèntic, sols separat. |
| **Estat** | Pendent de revisió |

---

### 7. Anys eliminats de la secció "Llistat"

| Camp | Contingut |
|------|-----------|
| **Original** | La secció `## Llistat` contenia: `1928 / 1929 / 1930 / 1931 / 1932 / 1933 / 1934 / 1935 / 1936 / 1937 / 1938` |
| **Nou** | La secció `## Llistat` és buida (el llistat real d'edificis es genera dinàmicament des de les fitxes) |
| **Motiu** | Aquests anys eren marcadors de lloc de l'import WP. El llistat real d'edificis s'ha importat com a fitxes individuals i el web els agrupa per any automàticament. |
| **Estat** | Pendent de revisió |

---

### 8. Plànol descarregable → majúscules corregides

| Camp | Contingut |
|------|-----------|
| **Original** | `## Plànol Descarregable` |
| **Nou** | `## Plànol descarregable` |
| **Motiu** | Correcció tipogràfica (capitalització de títols en català). |
| **Estat** | Pendent de revisió |

---

### 9. Secció "Visites" → links afegits

| Camp | Contingut |
|------|-----------|
| **Original** | `Visites:` (text incomplet, sense contingut) |
| **Nou** | Llista amb links: Casa Bloc → museudeldisseny.cat / Fundació Joan Miró → fmirobcn.org / Pavelló de la República → ub.edu |
| **Motiu** | El web original tenia aquesta informació però no es va importar correctament. S'han posat URLs estàndard. |
| **Estat** | ⚠️ **URGENT** — Cal confirmar les URLs correctes. Especialment el Pavelló de la República (l'URL original del WP era `www.elglobusvermell.org`, que no sembla correcte). |

---

### 10. Secció "Més informació" → majúscules corregides

| Camp | Contingut |
|------|-----------|
| **Original** | `## Més Informació Sobre Josep Lluís Sert I El Gatcpac` |
| **Nou** | `## Més informació sobre Josep Lluís Sert i el GATCPAC` |
| **Motiu** | Correcció tipogràfica. |
| **Estat** | Pendent de revisió |

---

## Publicacions pendents de revisió

Els continguts de les publicacions següents s'han editat automàticament (estructura h2/h3, neteja del Llistat). Pendent de documentar canvi per canvi:

- [ ] 09-25 — Arquitectura a Barcelona 2010–2025
- [ ] 50-75 — Arquitectura Moderna a Barcelona 1950–1975
- [ ] 76-08 — Arquitectura a Barcelona 1975–2008
- [ ] barceloneta — La Barceloneta
- [ ] biblioteques — Biblioteques de Barcelona
- [ ] interiors-illa — Jardins interiors d'illa
- [ ] marina — La Marina del Port
- [ ] masies — Masies de Barcelona
- [ ] mercats — Mercats de Barcelona
- [ ] new-babylon — La New Babylon de Constant
- [ ] poblenou — El patrimoni industrial del Poblenou
- [ ] tapies — La Barcelona de Tàpies

---

## Notes generals

- **Import WP → Hugo**: L'import automàtic ha convertit tots els títols de secció a "Title Case" (Primera Lletra En Majúscula), que no és el sistema tipogràfic català estàndard. S'han corregit a mesura que s'han editat les pàgines.
- **Contingut del Llistat**: Els llistats d'edificis de cada publicació s'han substituït per fitxes individuals importades. El web genera el llistat automàticament. Qualsevol diferència entre el llistat original WP i el llistat actual pot indicar un edifici que falta importar.
- **Imatges**: Les imatges dels edificis no s'han importat encara (pendent d'accés al servidor de producció).
