# ARQUITECTES-URLS.md — Tasca de recerca d'URLs per a una IA

## Context

Estem construint un web sobre arquitectura barcelonina.
Per a cada arquitecte o estudi tenim una fitxa al web, i volem afegir-hi dos enllaços:
1. **Arxiu COAC** — `arquitecturacatalana.cat` — és el perfil al Col·legi d'Arquitectes de Catalunya; **prioritari**
2. **Viquipèdia en català** — `ca.wikipedia.org` — complementari; si no existeix en català acceptem el castellà (`es.wikipedia.org`)

Aquest document conté les llistes de noms que cal cercar. La teva feina és:
- Cercar les dues URLs per a cada entrada de la **llista A** (individus) i la **llista B** (estudis)
- **No cercar** les entrades de la llista C (ja descompostes, els components estan a A i B)
- Per a les entrades de la **llista D** (dubtes), fer una nota breu del que trobes, sense necessitat de trobar URL necessàriament

## Com cercar al COAC

L'URL base és: `https://www.arquitecturacatalana.cat/ca/autors/[slug]`

El slug és el nom en minúscules, sense accents, caràcters especials substituïts per guions.
Exemples:
- Josep Lluís Sert → `josep-lluis-sert`
- MBM Arquitectes → `mbm-arquitectes`
- José Antonio Coderch de Sentmenat → `jose-antonio-coderch-de-sentmenat`

**Verifica sempre que la pàgina existeix realment** (que no retorni 404 ni redirigeixi a una pàgina d'error).
Si el slug no funciona, prova variants (amb/sense accents, amb/sense partícules com "de", "i", etc.).

## Com cercar a la Viquipèdia

L'URL base és: `https://ca.wikipedia.org/wiki/[Nom_amb_guions_baixos]`

Si no existeix en català, prova: `https://es.wikipedia.org/wiki/[Nom]`

**Verifica que la pàgina parla d'un arquitecte**, no d'una altra persona amb el mateix nom.

## Format de resposta

Per a cada entrada de les llistes A i B, retorna **exactament** aquest format (un bloc per entrada):

```
Nom: [nom tal com apareix a la llista]
COAC: [URL completa] o "no trobat"
Wikipedia: [URL completa] o "no trobat"
```

Exemple de resposta correcta:
```
Nom: Josep Maria Fargas
COAC: https://www.arquitecturacatalana.cat/ca/autors/josep-maria-fargas
Wikipedia: https://ca.wikipedia.org/wiki/Josep_Maria_Fargas_i_Falp
```

**Important:**
- No inventes URLs. Si no n'estàs segur, posa "no trobat".
- Copia el nom **exactament** com apareix a la llista (no el modifiquis).
- Processa totes les entrades de A i B, sense ometre'n cap.
- Per a la llista D, afegeix al final una secció `## Resolució de dubtes` amb una nota per a cada entrada.

---

## URLs ja conegudes (no cal cercar)

| Nom | COAC | Wikipedia |
|-----|------|-----------|
| MBM Arquitectes | no trobat | https://ca.wikipedia.org/wiki/MBM_Arquitectes |
| Josep Lluís Sert | no trobat | https://ca.wikipedia.org/wiki/Josep_Llu%C3%ADs_Sert |
| G. Guiteras | no trobat | no trobat |
| Josep Marimon i Cot | no trobat | no trobat |

---

## A — Arquitectes individuals

Cerca una URL per cada entrada. Ordenats alfabèticament.

- A. Espejo
- Adolf Florensa
- Alfonso de Luna
- Alfonso Milà
- Amadeu Llopart
- Ana Coello
- Ana Molino
- Antoni Audet
- Antoni Bonet Castellana
- Antoni Casellas
- Antoni de Ferrater
- Antoni de Moragas i Gallissà
- Antoni Falguera
- Antoni Fisas
- Antoni Grau Palés
- Antoni Perpiñà
- Antoni Pineda i Gualba
- Antoni Puig Gairalt
- Antoni Solanas
- Antoni Vila i Bruguera
- Arata Isozaki
- Albert de Pineda Álvarez
- Albert Viaplana
- Beatriz Borque
- Benedetta Tagliabue
- Bernardo de Solá
- Beth Galí
- Beverly Pepper
- Bonaventura Bassegoda
- Carles Buïgas i Sans
- Carles Enrich
- Carles Martínez
- Carlos Ferrer Kutter
- Carlos Marquès i Maristany
- Carme Ribas
- César Ortiz Echagüe
- Claudi Duran i Ventosa
- Claudi Gil
- Conxita Balcells
- Daniel Gelabert
- Daniel Navas
- Dario Daura
- David Mackay
- Eduard Molas Rifà
- Eduard Valencaso
- Elías Torres Tur
- Emili Donato Folch
- Emili Lluch
- Enric Miralles
- Enric Rello Roque
- Enric Sagnier Villavecchia
- Enric Tous
- Enrico Peressutti
- Ernesto N. Rogers
- Esteve Bonell Costa
- Eusebi Bona i Puig
- Federico Correa
- Franc Llonch
- Francesc Bassó i Birulés
- Francesc de la Guàrdia
- Francesc de Paula Quintana Vidal
- Francesc de Paula Villar Carmona
- Francesc de Riba de Salas
- Francesc Espiau
- Francesc Mitjans i Miró
- Francesc Perales
- Francesc Rius
- Francisco J. Barba Corsini
- Germà Rodríguez Arias
- Guillem Cosp i Vilaró
- Guillem Giráldez i Dávila
- Gustau Gili
- Helio Piñón
- Imma Jansana
- Ítalo Lauro
- Jaime Pastor
- Jaume Bernadas
- Jaume Mestres
- Javier Carvajal Ferrer
- Javier Sanz Rodriguez
- Joan Arias
- Joan Baca
- Joan Baptista Pons Trabal
- Joan Baptista Subirana
- Joan Barba
- Joan Bosch Agustí
- Joan Callís
- Joan Carles Cardenal
- Joan Vallvé i Creus
- Joan Vera
- Joaquim Gili i Morós
- Joaquim Romaguera Llach
- Joaquim Vilaseca
- Jordi Campanillas
- Jorge Vidal
- Josep Alemany i Juvé
- Josep Anglada
- Josep Anglès
- Josep Antoni Ballesteros
- Josep Domènech i Estapà
- Josep Gonzàlez
- Josep Graner i Prat
- Josep Lluís Mateo
- Josep M. Pericas
- Josep Manel Melo
- Josep Maria Casadevall
- Josep Maria Fargas
- Josep Maria Julià
- Josep Maria Martorell i Codina
- Josep Maria Segarra i Solsona
- Josep Maria Sostres i Maluquer
- Josep Masdeu
- Josep Miàs i Gifré
- Josep Pellicer i Gambús
- Josep Plantada i Artigas
- Josep Pujol i Brull
- Josep Ribas
- Josep Roselló i Til
- Josep Soteras i Mauri
- Josep Torres Clavé
- José Antonio Coderch de Sentmenat
- José Antonio Martínez Lapeña
- José Bori Jensana
- José Luis Sanz Magallón
- Juan José Olazabal
- Judith Masana
- Juli M. Fossas i Martínez
- Leandre Albareda i Petit
- Llorenç Massana
- Lluís Cantallops
- Lluís Clotet
- Lluís Comerón
- Lluís Pérez de la Vega
- Lodovico B. Belgiojoso
- Lola Domènech
- Lorenzo García-Barbón
- Luis Castellón
- Manuel Baldrich
- Manuel Brullet
- Manuel de Solà-Morales i de Rosselló
- Manuel de Solà-Morales i Rubió
- Manuel Puig Janer
- Manuel Raspall i Mallol
- Manuel Ribas i Piera
- Manuel Ruisánchez
- Manuel Valls i Vergés
- Marta Cervelló
- Martí Franch
- Meritxell Inaraja
- Miguel Jiménez
- Miquel Mariné
- Miquel Niubó i Munté
- Miquel Ponsetí i Vives
- Màrius Quintana
- Neus Solé
- Nilo Tusquets
- Núria Salvadó
- Oriol Bohigas i Guardiola
- Òscar Tusquets
- Pau Monguió
- Pau Vidal
- Pelayo Martínez Paricio
- Pere Joan Ravetllat
- Pere Llimona
- Pere López i Íñigo
- Pia Wortham
- Rafael García de Castro
- Rafael Moneo
- Rafael Serra Florensa
- Raimon Duran i Reynals
- Ramon Martí
- Ramon Pagès
- Ramon Puig
- Ramon Sanabria
- Ricardo Bofill Levi
- Ricard de Churruca
- Ricard Ribas
- Robert Terradas i Via
- Roger Méndez
- Santiago Balcells Gorina
- Sergi Godia
- Sixte Illescas
- Toyo Ito
- Víctor Rahola
- Xavier Busquets i Sindreu
- Xavier Ruiz i Vallès
- Xavier Subias i Fages

---

## B — Estudis i col·lectius

Cerca una URL per cada entrada (el nom és la identitat de l'estudi, no d'un individu).

- A&EB
- Agence Ter
- AIA
- apocapoc bcn
- Arquitectura-G
- Arriola & Fiol
- Ateliers Jean Nouvel
- B720 Arquitectes
- BAAS
- Barceló Balanzó
- Batlle i Roig
- Bayona-Valero
- BCQ Arquitectes
- BOMA
- Cantallops-Vicente
- Celobert
- Cierto Estudio
- Circular Studio
- Cloud 9
- Coll-Leclerc
- DataAE
- EMBT
- Ensenyat-Tarrida
- Espai LUR
- Garcés-de Seta-Bonet
- HArquitectes
- Haz Arquitectura
- La Boqueria (col·lectiu)
- Lacol
- Länk Arquitectes
- Lussi+Partner AG
- Lussi Studio
- Maio
- MAP Arquitectes
- MBM Arquitectes ← ja conegut, Wikipedia disponible
- OAB (Office of Architecture in Barcelona)
- OP Team Arquitectura
- Oliveras Boix
- Peris+Toral
- Prince Smith & Son
- RCR Arquitectes
- Roldán+Berengué
- SCOB
- slowup
- Straddle3
- Sumo
- SV60 Cordón & Liñán Arquitectos
- Toyo Ito Associates
- Vivas Arquitectos

---

## C — Signatures combinades (ja descompostes, no cal cercar)

Cada signatura de la base de dades era la unió de diversos arquitectes.
Estan descompostos a les llistes A i B. S'indica la forma original → components.

| Forma original al catàleg | Components (a cercar individualment) |
|--------------------------|--------------------------------------|
| AIA + Barceló Balanzó + Gustau Gili | AIA \| Barceló Balanzó \| Gustau Gili |
| Albert Viaplana, Helio Piñón i Gabriel Mora | Albert Viaplana \| Helio Piñón \| Gabriel Mora |
| Albert de Pineda Álvarez – PINEARQ, Manuel Brullet i Alfonso de Luna | Albert de Pineda Álvarez \| Manuel Brullet \| Alfonso de Luna |
| Ana Molino i Sergi Godia | Ana Molino \| Sergi Godia |
| Antoni Bonet Castellana i Josep Puig i Torner [variants] | Antoni Bonet Castellana \| Josep Puig i Torner |
| Antoni de Moragas i Gallissà i Francesc de Riba de Salas [variants] | Antoni de Moragas i Gallissà \| Francesc de Riba de Salas |
| Arata Isozaki, BOMA | Arata Isozaki \| BOMA |
| Arriola & Fiol Arquitectes i Beverly Pepper | Arriola & Fiol \| Beverly Pepper |
| Bayona i Valero + Cantallops Vicente | Bayona-Valero \| Cantallops-Vicente |
| Beatriz Borque i Miquel Mariné | Beatriz Borque \| Miquel Mariné |
| Bernardo de Solá i Josep Maria Julià | Bernardo de Solá \| Josep Maria Julià |
| César Ortiz Echagüe, Manuel Barbero Rebolledo i Rafael de la Joya | César Ortiz Echagüe \| Manuel Barbero Rebolledo \| Rafael de la Joya |
| Clotet-Paricio | Lluís Clotet \| [Paricio: veure dubtes] |
| Coll-Leclerc i Josep Miàs | Coll-Leclerc \| Josep Miàs i Gifré |
| Eduard Molas Rifà, Enric Rello Roque i Josep M. Rovira Gimeno | Eduard Molas Rifà \| Enric Rello Roque \| Josep M. Rovira Gimeno |
| Emili Donato, Miguel Jiménez i Ramon Martí | Emili Donato Folch \| Miguel Jiménez \| Ramon Martí |
| Enric Miralles i Benedetta Tagliabue [variants] | Enric Miralles \| Benedetta Tagliabue |
| EMBT (Benedetta Tagliabue) / EMBT (Enric Miralles i Benedetta Tagliabue) | EMBT (estudi) |
| Ernesto N. Rogers, Lodovico B. Belgiojoso i Enrico Peressutti | Ernesto N. Rogers \| Lodovico B. Belgiojoso \| Enrico Peressutti |
| Eusebi Bona i Puig, Pelayo Martínez Paricio i Josep Maria Segarra i Solsona | Eusebi Bona i Puig \| Pelayo Martínez Paricio \| Josep Maria Segarra i Solsona |
| Federico Correa, Alfonso Milà i José Luis Sanz Magallón | Federico Correa \| Alfonso Milà \| José Luis Sanz Magallón |
| Francesc Bassó i Birulés i Joaquim Gili i Morós | Francesc Bassó i Birulés \| Joaquim Gili i Morós |
| Francesc Mitjans, Josep Soteras i Lorenzo García Barbón | Francesc Mitjans i Miró \| Josep Soteras i Mauri \| Lorenzo García-Barbón |
| G. Giráldez, P. López i J. Subias | Guillem Giráldez i Dávila \| Pere López i Íñigo \| Xavier Subias i Fages |
| Guillem Giráldez i Dávila, Pere López i Íñigo i Xavier Subias i Fages | Guillem Giráldez i Dávila \| Pere López i Íñigo \| Xavier Subias i Fages |
| Guillem Giráldez i Dávila, Pere López i Íñigo, Xavier Subias i Fages, Manuel Baldrich | Guillem Giráldez i Dávila \| Pere López i Íñigo \| Xavier Subias i Fages \| Manuel Baldrich |
| Imma Jansana, Neus Solé i Daniel Navas | Imma Jansana \| Neus Solé \| Daniel Navas |
| Javier Carvajal Ferrer i Rafael García de Castro | Javier Carvajal Ferrer \| Rafael García de Castro |
| Joan Arias i Lluís Pérez de la Vega | Joan Arias \| Lluís Pérez de la Vega |
| Joan Callís i Pia Wortham | Joan Callís \| Pia Wortham |
| Joaquim Vilaseca i Adolf Florensa | Joaquim Vilaseca \| Adolf Florensa |
| Josep Alemany, Oriol Bohigas, Josep Maria Martorell, Francesc Mitjans, Antoni Perpiñà | Josep Alemany i Juvé \| Oriol Bohigas i Guardiola \| Josep Maria Martorell i Codina \| Francesc Mitjans i Miró \| Antoni Perpiñà |
| Josep Anglada, Daniel Gelabert i Josep Ribas | Josep Anglada \| Daniel Gelabert \| Josep Ribas |
| Josep Antoni Ballesteros, Joan Carles Cardenal, Francesc de la Guàrdia, Xavier Ruiz | Josep Antoni Ballesteros \| Joan Carles Cardenal \| Francesc de la Guàrdia \| Xavier Ruiz i Vallès |
| Josep Llinàs – Joan Vera | Josep Llinàs i Carmona \| Joan Vera |
| Josep Llinàs i Carmona | Josep Llinàs i Carmona |
| Josep Lluís Sert | ja conegut |
| Josep Maria Casadevall i Ramon Sanabria | Josep Maria Casadevall \| Ramon Sanabria |
| Josep Maria Fargas i Enric Tous | Josep Maria Fargas \| Enric Tous |
| Josep Soteras i Mauri i Lorenzo García-Barbón | Josep Soteras i Mauri \| Lorenzo García-Barbón |
| Josep Soteras i Mauri, Antoni Pineda i Gualba i Carlos Marquès i Maristany | Josep Soteras i Mauri \| Antoni Pineda i Gualba \| Carlos Marquès i Maristany |
| José Antonio Coderch de Sentmenat i Manuel Valls i Vergés | José Antonio Coderch de Sentmenat \| Manuel Valls i Vergés |
| José Antonio Martínez Lapeña i Elías Torres Tur | José Antonio Martínez Lapeña \| Elías Torres Tur |
| Lacol + La Boqueria | Lacol \| La Boqueria |
| Lluís Clotet i Òscar Tusquets | Lluís Clotet \| Òscar Tusquets |
| Lluís Comerón i Ramon Sanabria | Lluís Comerón \| Ramon Sanabria |
| Lola Domènech, Lussi Studio i Lussi+Partner AG | Lola Domènech \| Lussi Studio \| Lussi+Partner AG |
| MAP Arquitectes (Marta Cervelló i Josep Lluís Mateo) | MAP Arquitectes \| Marta Cervelló \| Josep Lluís Mateo |
| Manuel de Solà-Morales i de Rosselló i Manuel de Solà-Morales i Rubió | Manuel de Solà-Morales i de Rosselló \| Manuel de Solà-Morales i Rubió |
| MBM (Martorell, Bohigas, Mackay) | MBM Arquitectes (same entry) |
| Marta Cervelló i Josep Lluís Mateo | Marta Cervelló \| Josep Lluís Mateo |
| Núria Salvadó i Josep Anglès | Núria Salvadó \| Josep Anglès |
| OAB (Carlos Ferrater) | OAB (Office of Architecture in Barcelona) |
| Oriol Bohigas i Guardiola i Josep Maria Martorell i Codina | Oriol Bohigas i Guardiola \| Josep Maria Martorell i Codina |
| Oriol Bohigas i Guardiola, Josep Maria Martorell i Codina i David Mackay | Oriol Bohigas i Guardiola \| Josep Maria Martorell i Codina \| David Mackay |
| Oriol Bohigas i Josep Maria Martorell | Oriol Bohigas i Guardiola \| Josep Maria Martorell i Codina |
| Oriol Bohigas, Josep Maria Martorell i David Mackay | Oriol Bohigas i Guardiola \| Josep Maria Martorell i Codina \| David Mackay |
| Pau Vidal + Vivas Arquitectos | Pau Vidal \| Vivas Arquitectos |
| Pere Llimona i Xavier Ruiz i Vallès | Pere Llimona \| Xavier Ruiz i Vallès |
| Pere López i Íñigo, Xavier Subias i Fages i Guillem Giráldez i Dávila | Guillem Giráldez i Dávila \| Pere López i Íñigo \| Xavier Subias i Fages |
| Peris+Toral i Jaime Pastor | Peris+Toral \| Jaime Pastor |
| Ricard Bofill Levi / Ricardo Bofill Levi | Ricardo Bofill Levi (forma preferida) |
| Ricard de Churruca i Germà Rodríguez Arias | Ricard de Churruca \| Germà Rodríguez Arias |
| Toyo Ito Associates i Óscar Tusquets / Straddle3 | Toyo Ito Associates \| Òscar Tusquets \| Straddle3 |
| Toyo Ito i B720 | Toyo Ito \| B720 Arquitectes |
| Viaplana / Piñón | Albert Viaplana \| Helio Piñón |
| apocapoc bcn + slowup (Sandra Martín Lara) | apocapoc bcn \| slowup |
| B720 (Fermín Vázquez) | B720 Arquitectes |
| BAAS (Jordi Badia) | BAAS |
| Raimon Duran Reynals | Raimon Duran i Reynals |
| Xavier Busquets Sindreu | Xavier Busquets i Sindreu |

---

## D — Dubtes i entitats incertes

Per a cada entrada, inclou una **nota breu** del que trobes (no cal URL necessàriament, però sí si en trobes).

| Entrada | Dubte |
|---------|-------|
| Amigó / Joan Amigó | Podrien ser el mateix. Confirmar si "Amigó" és el cognom d'un arquitecte diferent o abreviació de Joan Amigó |
| Bonell / Esteve Bonell Costa | Sembla el mateix ("Bonell Costa" és el cognom compost). Confirmar i usar "Esteve Bonell Costa" |
| Cabrera | Identitat desconeguda. Quin Cabrera arquitecte treballa a Barcelona? |
| Clotet-Paricio | Lluís Clotet és conegut. "Paricio" és qui? Paricio Ansuátegui? Confirmar |
| E. i J. Rey Fàbregas | Dos germans o estudi familiar? Noms complets desconeguts |
| Ensenyat-Tarrida | Duo o estudi? Noms individuals: Ensenyat i Tarrida, qui són? |
| Gil | Identitat desconeguda. Quin Gil arquitecte treballa a Barcelona? |
| J. Domènech | Podria ser Josep Domènech i Estapà (ja a la llista A), o un altre Domènech |
| J. Rodríguez | Identitat desconeguda |
| Josep Alemany i Juvé / Josep Alemany | Probablement el mateix. Usar "Josep Alemany i Juvé" |
| Josep Maria Sostres i Maluquer | ATENCIÓ: és una persona diferent de Josep Soteras i Mauri |
| Josep Maria Soteras i Mauri | Possible variant ortogràfica de "Josep Soteras i Mauri". Confirmar si és el mateix o diferent |
| Josep Lluís Mateo | Individual i/o soci de MAP Arquitectes. Té pàgina pròpia al COAC? |
| Lorenzo García-Barbón / Llorenç García-Barbón | Probable mateix arquitecte (nom en castellà/català). Usar "Lorenzo García-Barbón" |
| Mariano Romano Rius (?) | Ja marcat com incert a la base de dades |
| Van der Harst | Cognoms de procedència neerlandesa. Quin arquitecte? |
| Xavier Ruiz i Vallès / Xavier Ruiz | Possible duplicat. "Xavier Ruiz" (d'un col·legi de Ballesteros) podria ser Xavier Ruiz i Vallès |
