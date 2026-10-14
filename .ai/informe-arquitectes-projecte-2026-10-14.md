# Informe — Duplicitat «Arquitectes» / «Projecte» (14/10/2026)

**Origen:** nota del full de ruta «Per al 14/10 — verificar per què a cada fitxa surten Arquitectes i Projecte amb la mateixa informació, i confirmar si ho havia demanat Xavi».

## Per què passa

- **Sí, ho va demanar Xavi** (mail 31/8, punt 6; `docs/2026-08-31-mail-xavi-2-respostes-disseny.md`): fila `Arquitectes` amb tots els autors clicables + fila `Projecte` (autors + any, no clicables).
- **El 9/10 (F5) ho revisa:** «La idea és fer desaparèixer la informació repetida i, per tant, el camp arquitectes… que sigui a intervencions on l'arquitecte pugui ser clicable».
- Ja fet el 10/10 (`598c117`, `a712805`): tipus «Projecte» per defecte i autors clicables dins les intervencions.

## Dades (658 fitxes)

| Grup | Fitxes | Què es veu ara |
|---|---|---|
| Arquitectes + intervencions, **tots els noms coincideixen** | **212** | Fila repetida |
| Arquitectes + intervencions, **noms escrits diferent** | 10 | Repetida, i el nom de «Projecte» no enllaça |
| Només `arquitectes` | 79 | Una sola fila, correcte |
| Només `intervencions` | 101 | Una sola fila, correcte |
| Sense autoria | 255 | — |

Tipus d'intervenció: projecte 262 · remodelació 54 · reforma 12 · ampliació 6 · reconstrucció 1 · remunta 1.

## Proposta (no esborra cap dada)

1. **Plantilla:** amagar la fila `Arquitectes` quan tots els noms ja surten als autors de les intervencions. El camp `arquitectes` es conserva (alimenta la pàgina de cada arquitecte i els enllaços).
   - Prova en viu: `?projecte=1` a qualsevol fitxa (classe `fitxa-dada-repetida`, 212 fitxes marcades). Per defecte no canvia res.
2. **Dades (cal aprovació de Joan + registre a `REGISTRE-CANVIS-FITXES.md`):** unificar el nom dins `intervencions[].autors` als 10 casos:

| Fitxa | `arquitectes` | Autors a la intervenció |
|---|---|---|
| centre-darts-santa-monica | Albert Viaplana i Veà, Heliodoro Piñón Pallarés | Reforma: «Albert Viaplana» |
| centre-de-cultura-contemporania-de-barcelona-cccb | Albert Viaplana i Veà, Heliodoro Piñón Pallarés | Reforma: «Viaplana / Piñón» |
| cristalleries-planell | HArquitectes | «H Arquitectes» |
| edifici-dhabitatges-avinguda-meridiana-302 | Antoni de Moragas i Gallissà, Francesc de Riba i Salas | «… i Francesc de Riba de Salas» |
| edifici-dhabitatges-carrer-compte-borrell | ídem | «… i Francisco Ribas de Salas» |
| edifici-dhabitatges-carrer-sant-antoni-i-maria-claret | ídem | «… i Francisco Ribas de Salas» |
| edifici-dhabitatges-via-augusta | ídem | «… i Francisco Riba de Salas» |
| edifici-dhabitatges-i-oficines-can-bruixa | Albert Viaplana i Veà, Heliodoro Piñón Pallarés, Gabriel Mora i Gramunt | «Albert Viaplana, Helio Piñón i Gabriel Mora» |
| edifici-dhabitatges-mediterrani | Antoni Bonet Castellana, Josep Puig i Torné | «Antoni Bonet i Castellana i Josep Puig i Torné» |
| torre-urquinaona | Antoni Bonet Castellana, Josep Puig i Torné | «… i Josep Puig i Torner» |

Atenció: CCCB i Santa Mònica tenen tipus «Reforma». Cal confirmar si Viaplana/Piñón són autors de la reforma (i no del projecte original) abans d'unificar.

**Estat:** decisió al tauler (`fitxa-arquitectes-projecte`), amb enllaços a la prova.
