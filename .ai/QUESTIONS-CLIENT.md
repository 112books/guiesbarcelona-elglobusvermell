# QUESTIONS-CLIENT.md — Preguntes i propostes per a El Globus Vermell

Llegenda: ⏳ Pendent resposta | ✅ Resolt | 💡 Proposta LinuxBCN

---

## Preguntes pendents de resposta

### Jorge
- 🔴 Dades d'accés al servidor actual (host, usuari, ruta, clau SSH)

### Xavi
- ⏳ **"El projecte en xifres"** — La portada alternativa mostra les xifres del projecte (edificis, guies, anys). Decidir on ha d'anar aquest element: a la portada (ja implementat), a Crèdits (on ja hi ha tota la informació del projecte) o a Presentació (on s'explica el projecte al visitant nou). Presentació sembla la ubicació més lògica per a qui arriba per primer cop.
- ⏳ **Autoria fotografies** — Les fotos dels edificis van amb © o amb una altra llicència? Cal confirmar si el símbol © és correcte o si s'ha d'usar una altra forma de crèdit (ex: CC BY, sense reserva de drets, etc.). Afecta el peu de foto de totes les fitxes.
- ⏳ **Locucions (text a veu)** — Dues opcions: (A) Web Speech API, gratuïta, veu del sistema operatiu, ja implementada com a prova; (B) Piper TTS, veu neutra de qualitat, programari lliure, requereix servidor, ja pressupostada. Les locucions són importants per a l'accessibilitat de persones amb dificultats visuals (WCAG 2.1, criteri 1.1.1 i recomanació 1.3.4). Si s'implementa la opció B, cal reflectir-ho a Crèdits (tecnologia) i a la Declaració d'Accessibilitat.
- ⏳ Confirmar pressupost 3.900€ + 50% bestreta per iniciar Flutter
- ⏳ Accés a guiesbarcelona.elglobusvermell.org (Xavi diu que ha demanat)
- ⏳ Decisió de disseny: colors per publicació vs nou rebrand
- ⏳ Esquema de "En paper": portada + botó PDF descarregable?
- ⏳ Separar arquitectes combinats: ho fem nosaltres o ho revisa Xavi?
- ⏳ Llicència del peu de pàgina: © o Creative Commons?
- ⏳ Contrasenya admin backoffice
- Pendent — **Filtre de temes** — Xavi proposa valorar un filtre de temes (Èpoques, Arquitectura temàtica, Barris, Art) com el d'«En paper», potser també al mapa, però no n'està segur. Cal concretar-ne l'abast.
- Pendent — **Filtre del mapa (bug)** — En seleccionar una guia no canvia res visualment. Cal acordar què ha de fer: atenuar, amagar, ressaltar d'una altra manera, o fer zoom/llistat. Veure `.ai/RESPOSTES-XAVI-2026-09-30.md` secció 4.
- Pendent — **M5 temes transversals** — Confirmar que volen pàgina pròpia amb el seu mapa (en lloc del botó (i)).
- Pendent — **Carrusel d'«En paper» a escriptori** — Amagar la barra de desplaçament, arrossegar amb el cursor i portades una mica més grans.
- Pendent — **F6 fotos en blanc i negre** — Consens d'equip; possibilitat de color parcial (patrimoni industrial) i la resta B/N.
- Pendent — **P7 splash mòbil** — Mostrar el logo i allargar una mica l'instant.
- Pendent — **ENQ-lectura** — Alinear el botó a la dreta com a les fitxes i revisar la veu.
- Pendent — **PR1 anys de les xifres** — Revisar 1400-2026 vs s. XIV-2026, lligat a arreglar les fitxes.
- Pendent — **G1 amplada de columna** — Preparar una prova amb 2-3 amplades.
- Pendent — **Icones mòbil** — La icona de mapa passa a «En paper»; el mapa estrena pin clàssic.
- Pendent — **GR1/GR2 paleta definitiva** — Xavi l'enviarà.
- Pendent — **M3 pins multicolor** — Sí, meitat/meitat o pastís de 3 colors; depèn de la paleta.
- Pendent — **T07 formulari únic** — Valorar un sol formulari a Contacte per a tot.
- Pendent — **Cercador general** — Decidir si cal un cercador general a tot el web o només el d'elements.
- Pendent — **Decisions encara sense resposta** — autoria de fotos, separació d'arquitectes combinats, distribució de guies a la portada (6·6·1 vs 5·5·3), mapa en grays i tipografia (GR3). Detall a `.ai/RESPOSTES-XAVI-2026-09-30.md` secció 3.

---

## Propostes LinuxBCN per a El Globus Vermell

### 💡 Arxiu fotogràfic de Catalunya — fotografies per a edificis sense imatge
Contactar amb l'Arxiu Nacional de Catalunya (o l'Arxiu Fotogràfic de Barcelona)
per obtenir imatges dels edificis dels quals no es disposa de fotografia pròpia.
Podria cobrir una part significativa dels punts del mapa que ara apareixen sense foto.

### 💡 Autoria de fotografies
Cal afegir crèdit fotogràfic a totes les imatges, tant si són d'El Globus Vermell
com si provenen d'arxius externs. Format suggerit: peu de foto discret a la fitxa
de l'edifici (© El Globus Vermell / © Arxiu Fotogràfic de Barcelona, etc.).

### 💡 Portada alternativa al web de guies *(en desenvolupament — vegeu HOME-ALTERNATIVA.md)*
L'actual portada posa el focus en el mapa. La nova portada presentaria el projecte
globalment: frase contundent, guia destacada aleatòria amb un edifici seu,
accés a totes les guies i al mapa, arquitecte/estudi aleatori, i secció
de recursos educatius. Vegeu `.ai/HOME-ALTERNATIVA.md` per al pla complet.

---

## Resolt
- ✅ "Filtrar per publicacions" al mapa: tots atenuats a l'inici, ressaltar en marcar
- ✅ **T06 — Bloc "Publicacions" al mapa**: Xavi confirma mantenir-lo (resposta a l'eina de revisió, 30/9).
- ✅ **T07 — "Suggerir un canvi"**: Xavi confirma mantenir-lo només fora de Presentació, a Contacte, amb un únic formulari per a tot (30/9).
