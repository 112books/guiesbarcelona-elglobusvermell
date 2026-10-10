# Diagnosi dels errors de traspàs (WordPress → Hugo) — 9/10/2026

**Origen:** correu de Xavi del 9/10/2026 (punts S5–S8 de
`.ai/RESPOSTES-XAVI-2026-10-09.md`).
**Abast analitzat:** 657 fitxes de `content/ca/elements/` (frontmatter YAML).

Xavi diu que només ha trobat «els ràpids» i creu que n'hi pot haver més.
Aquest document en fa la diagnosi quantitativa per decidir **què es pot
automatitzar** i **què cal fer a mà, fitxa per fitxa**.

---

## Resum de xifres

| Patró | Fitxes afectades |
|-------|------------------|
| Sense camp `foto` | **299** (de 657) |
| Sense `foto` **entre les biblioteques** | **6** (de 50) |
| `adreca` amb separador ` | ` del text migrat | **38** |
| Sense `adreca` | **20** |
| Coordenades absents o `NaN` | **1** |
| Sense `arquitectes` | **356** |
| Sense `intervencions` **ni** `arquitectes` | **255** |
| `intervencions[].any` sense cap any numèric | **12** |
| Camp `projecte_text` present | **31** |
| Camp `edifici_original` present | **19** |
| `descripcio` que conté una adreça | **31** |
| `intervencions[].descripcio` que conté una adreça | **7** |

> Nota: bona part de les 299 fitxes sense foto i de les 356 sense arquitectes
> és **informació que simplement no es va arribar a migrar**, no un camp
> encallat. Cal no confondre-ho amb els errors de col·locació (S6 i S7).

---

## S5 — Foto de la portada del plànol a les biblioteques

**Estat:** 6 de les 50 fitxes de biblioteques **no tenen cap `foto`**:

- `biblioteca-bon-pastor-josefina-castellvi.md`
- `biblioteca-de-lateneu-barcelones.md`
- `illa-dequipaments-fort-pienc.md`
- `biblioteca-les-roquetes-rafa-juncadella.md`
- `biblioteca-vallcarca-i-els-penitents-maria-antonieta-cot.md`
- `biblioteca-canyelles-maria-angels-rivas.md`

No hi ha cap `foto` duplicada ni cap que apunti a `/img/publicacions/`, així
que la «portada del plànol» no ve d'un camp compartit. Cal revisar cada cas:
probablement la imatge assignada al camp `foto`, o la que es veu a la fitxa,
és la coberta del plànol i no una foto de l'edifici.

**Acció:** revisió visual fitxa per fitxa de les 6 (més, si cal, la resta de
biblioteques). És **manual**.

---

## S6 i S8 — Informació encallada a «projecte»

El frontmatter de les fitxes conté camps **antics** que es van quedar plens amb
text que no els toca:

- **`projecte_text`** (31 fitxes): text de projecte/arquitecte.
- **`edifici_original`** (19 fitxes): descripció de l'edifici original.
- **`intervencions[].any`** (12 fitxes) amb noms o segles en comptes d'un any:
  - `fabrica-dalbert-musteros` → `"Josep Pansas Coll (?). Inici s. xx"`
  - `fabrica-de-creacio-fabra-i-coats` → `"Manuel Ruisánchez i Francesc Bacardit (BAMMP)"`
  - `pastes-magin-quer` → `"Josep M. Plantada. Inici s. xx"`
  - `olis-pallares`, `magatzem-de-draps-de-francisco-munne-bau`, `edifici-dhabitatges-sant-carles`, `castell-del-port`, `casino-familiar`…
- **`intervencions[].descripcio`** (7 fitxes) amb l'adreça o la biografia a dins.

Les 255 fitxes **sense `intervencions` ni `arquitectes`** és un forat
d'informació, no un trasbals: caldrà omplir-lo si es vol completar el web.

**Pregunta de Xavi:** «ho fem nosaltres manualment fitxa per fitxa?»

**Recomanació:**
1. **Automatitzable amb seguretat:** treure el separador ` | ` final de les
   38 `adreca`; normalitzar els espais; detectar i buidar camps clarament
   erronis (`lat: NaN`, `long: NaN`).
2. **Semiautomàtic:** moure de `intervencions[].any` a `intervencions[].descripcio`
   els valors que no són anys (12 fitxes) i separar el nom d'arquitecte.
3. **Manual:** decidir si `projecte_text` i `edifici_original` es conserven com
   a camps propis o s'integren a `intervencions`/`descripcio`; omplir
   arquitectes i fotos que falten.

Es pot preparar un **script de normalització** i revisar-ne el diff abans
d'aplicar-lo (sense tocar els casos dubtosos).

---

## S7 — Camp `adreca` atrapat en altres llocs

- **38 fitxes** tenen un `adreca` que acaba amb el separador de l'antic
  WordPress (` | `), p. ex. `adreca: C. Estadella, 62 |`.
- **31 fitxes** tenen una adreça **dins de `descripcio`** (començant per
  «Adreça:», «C.», «Pl.», «Av.»…), p. ex. `biblioteca-la-fraternitat`,
  `esplanada-forum-pergola-fotovoltaica`, `masia-can-baro`.
- **7 fitxes** la tenen dins d'`intervencions[].descripcio`.
- **20 fitxes** no tenen cap `adreca`.

**Acció:** extreure l'adreça del text i posar-la al camp `adreca` és
**semiautomatitzable** amb una revisió humana del resultat.

---

## Proposta

1. Escriure `scripts/normalitza-traspas.py` que faci les operacions segures
   (neteja de ` | `, espais, `NaN`, detecció d'adreces candidates) i generi un
   **informe de canvis** sense modificar res.
2. Revisar l'informe conjuntament (LinuxBCN + Xavi) i aplicar-lo per lots.
3. La resta (fotos, arquitectes que falten, dubtes) fer-la **manualment**, tal
   com proposa Xavi.

**No s'ha tocat cap dada en aquesta sessió**: aquest document és només la
diagnosi, a l'espera de decidir el mètode.
