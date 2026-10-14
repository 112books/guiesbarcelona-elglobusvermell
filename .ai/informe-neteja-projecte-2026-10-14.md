# Proposta de neteja — informació encallada a «projecte»

Generat per `scripts/proposa-neteja-projecte.py` (només lectura: **no s'ha aplicat res**).

Origen: correu de Xavi del 9/10 (B2/B4): «moltes informacions han quedat encallades dins l'etiqueta projecte… Ho fem nosaltres manualment fitxa per fitxa?».

**Regla:** no s'esborra res. Cada proposta mou text d'un camp a un altre dins la mateixa fitxa, i la plantilla deixa de mostrar-lo repetit.

## Resum

| Patró | Casos | AUTO | REVISA | MANUAL |
|---|---|---|---|---|
| 1. Autor i any barrejats al camp «any» de la intervenció | 21 | 11 | 2 | 8 |
| 2. «projecte_text» repetit | 31 | 31 | 0 | 0 |
| 3. «Edifici original» que hauria de ser una intervenció «Projecte original» | 19 | 12 | 4 | 3 |
| 4. Etiqueta «Categoria:» del WordPress dins la descripció | 50 | 48 | 2 | 0 |
| 5. Premis dins la descripció | 4 | 0 | 4 | 0 |
| 6. «Projecte original», «Reforma», «Rehabilitació»… dins la descripció | 69 | 1 | 33 | 35 |
| **Total** (154 fitxes) | **194** | **103** | **45** | **46** |

- **AUTO:** patró inequívoc; es pot aplicar per script un cop aprovat.
- **REVISA:** el script fa la proposta, però cal una ullada (noms, anys aproximats, tipologia ja plena).
- **MANUAL:** text truncat a la migració, diverses fases o dades que falten; es completa amb el WordPress en producció.

## 1. Autor i any barrejats al camp «any» de la intervenció (21)

| Fitxa | Ara | Proposta | Tipus |
|---|---|---|---|
| `ca-lilla` | any: «Carlos Martínez Sánchez. 1930/1940» | autors: «Carlos Martínez Sánchez» · any: «1930/1940» | AUTO |
| `can-ricart` | any: «Josep Oriol i Bernadet. 1853-1860 + Josep Fontserè. 1860-1877» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |
| `carrer-cristobal-de-moura` | any: «Ajuntament de Barcelona. 2019 + 2025» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |
| `casa-josep-magret` | any: «Josep Graner i Prat. 1910, aprox.» | autors: «Josep Graner i Prat» · any: «1910, aprox.» | AUTO |
| `casa-josep-torras` | any: «Josep Graner i Prat. 1900, aprox.» | autors: «Josep Graner i Prat» · any: «1900, aprox.» | AUTO |
| `casa-lluis-cairo` | any: «Domènec Boada Piera. 1910, aprox.» | autors: «Domènec Boada Piera» · any: «1910, aprox.» | AUTO |
| `centre-civic-baro-de-viver` | any: «Territori24, 2014» | autors: «Territori24» · any: «2014» | AUTO |
| `edifici-dhabitatges-maquinista` | any: «Domènec Boada Piera. 1910, aprox.» | autors: «Domènec Boada Piera» · any: «1910, aprox.» | AUTO |
| `edifici-ricard-ametlla-montana` | any: «Pere Armengou. 1947 + 1956» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |
| `entorns-del-mercat-del-born` | any: «Vora. 2013 + 2019» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |
| `fabrica-dalbert-musteros` | any: «Josep Pansas Coll (?). Inici s. xx» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |
| `fabrica-de-creacio-fabra-i-coats` | any: «Manuel Ruisánchez i Francesc Bacardit (BAMMP)» | autors: «Manuel Ruisánchez i Francesc Bacardit (BAMMP)» · any: (buit) | REVISA |
| `olis-pallares` | any: «Josep A. Capdevila (?). Inici s. xx» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |
| `passeig-de-sant-joan` | any: «Lola Domènech. 2011 + 2014» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |
| `passeig-maritim-de-la-barceloneta` | any: «Olga Tarrasó, Jordi Henrich, Jaume Artigues i Miquel Roig. 1997-2001» | autors: «Olga Tarrasó, Jordi Henrich, Jaume Artigues i Miquel Roig» · any: «1997-2001» | AUTO |
| `pastes-magin-quer` | any: «Josep M. Plantada. Inici s. xx» | autors: «Josep M. Plantada» · any: «Inici s. xx» | REVISA |
| `pla-de-palau-i-passeig-joan-de-borbo` | any: «Olga Tarrasó i Jordi Henrich. 1988-1994» | autors: «Olga Tarrasó i Jordi Henrich» · any: «1988-1994» | AUTO |
| `placa-soller-i-ateneu-la-bobila` | any: «Barrio Peraire. 2021-2022» | autors: «Barrio Peraire» · any: «2021-2022» | AUTO |
| `tallers-nuevo-vulcano` | any: «Julio Isamat Vila. 1931-1951» | autors: «Julio Isamat Vila» · any: «1931-1951» | AUTO |
| `torre-de-les-aigues-del-besos` | any: «Pere Falqués i Urpí. 1880-1882» | autors: «Pere Falqués i Urpí» · any: «1880-1882» | AUTO |
| `torre-del-rellotge` | any: «Joris Prosper van Verboom. 1772. Conversió en rellotge: 1904» | Diverses fases o autoria dubtosa: separar a mà | MANUAL |

## 2. «projecte_text» repetit (31)

| Fitxa | Ara | Proposta | Tipus |
|---|---|---|---|
| `ca-lilla` | projecte_text: «Carlos Martínez Sánchez. 1930/1940» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `can-ricart` | projecte_text: «Josep Oriol i Bernadet. 1853-1860 + Josep Fontserè. 1860-1877» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `carrer-cristobal-de-moura` | projecte_text: «Ajuntament de Barcelona. 2019 + 2025» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `casa-josep-magret` | projecte_text: «Josep Graner i Prat. 1910, aprox.» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `casa-josep-torras` | projecte_text: «Josep Graner i Prat. 1900, aprox.» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `casa-lluis-cairo` | projecte_text: «Domènec Boada Piera. 1910, aprox.» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `casino-familiar` | projecte_text: «Finals s. xix» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `castell-del-port` | projecte_text: «Segles XI-XV» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `centre-civic-baro-de-viver` | projecte_text: «Territori24, 2014» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `colonia-santiveri` | projecte_text: «1915-1920» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `edifici-dhabitatges-maquinista` | projecte_text: «Domènec Boada Piera. 1910, aprox.» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `edifici-dhabitatges-salamanca` | projecte_text: «1910, aprox.» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `edifici-dhabitatges-sant-carles` | projecte_text: «Final segle XIX – principi segle XX» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `edifici-ricard-ametlla-montana` | projecte_text: «Pere Armengou. 1947 + 1956» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `entorns-del-mercat-del-born` | projecte_text: «Vora. 2013 + 2019» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `fabrica-dalbert-musteros` | projecte_text: «Josep Pansas Coll (?). Inici s. xx» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `fabrica-de-creacio-fabra-i-coats` | projecte_text: «Manuel Ruisánchez i Francesc Bacardit (BAMMP)» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `magatzem-de-draps-de-francisco-munne-bau` | projecte_text: «Finals s. xix o principis s. xx» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `olis-pallares` | projecte_text: «Josep A. Capdevila (?). Inici s. xx» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `passeig-de-sant-joan` | projecte_text: «Lola Domènech. 2011 + 2014» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `passeig-maritim-de-la-barceloneta` | projecte_text: «Olga Tarrasó, Jordi Henrich, Jaume Artigues i Miquel Roig. 1997-2001» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `pastes-magin-quer` | projecte_text: «Josep M. Plantada. Inici s. xx» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `pla-de-palau-i-passeig-joan-de-borbo` | projecte_text: «Olga Tarrasó i Jordi Henrich. 1988-1994» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `placa-soller-i-ateneu-la-bobila` | projecte_text: «Barrio Peraire. 2021-2022» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `tallers-nuevo-vulcano` | projecte_text: «Julio Isamat Vila. 1931-1951» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `torre-de-les-aigues-del-besos` | projecte_text: «Pere Falqués i Urpí. 1880-1882» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `torre-del-rellotge` | projecte_text: «Joris Prosper van Verboom. 1772. Conversió en rellotge: 1904» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `xemeneia-de-la-foneria-giralt` | projecte_text: «Segona dècada s. xx» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `xemeneia-de-la-ram` | projecte_text: «Segona dècada s. xx» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `xemeneia-de-lelectrolisis` | projecte_text: «Principis s. xix» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |
| `xemeneia-de-tallada-i-lora` | projecte_text: «Segona dècada s. XX» | Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva) | AUTO |

## 3. «Edifici original» que hauria de ser una intervenció «Projecte original» (19)

| Fitxa | Ara | Proposta | Tipus |
|---|---|---|---|
| `biblioteca-clara` | edifici_original: «Habitatge i taller-estudi de Josep Clarà. Raimon Duran i Reynals. 1920» | nova intervenció «Projecte original»: autors «Raimon Duran i Reynals» · any «1920» · descripció «Habitatge i taller-estudi de Josep Clarà» | AUTO |
| `biblioteca-crai-de-la-ciutadella-diposit-de-les-aigues-universitat-pompeu-fabra` | edifici_original: «Dipòsit d’aigües. Josep Fontserè i Mestre. 1880» | nova intervenció «Projecte original»: autors «Josep Fontserè i Mestre» · any «1880» · descripció «Dipòsit d’aigües» | AUTO |
| `biblioteca-de-catalunya` | edifici_original: «Hospital de la Santa Creu. Guillem Abiell. 1406.» | nova intervenció «Projecte original»: autors «Guillem Abiell» · any «1406» · descripció «Hospital de la Santa Creu» | AUTO |
| `biblioteca-de-lateneu-barcelones` | edifici_original: «Palau Savassona. Francesc Ferrer de Llupià. 1796» | nova intervenció «Projecte original»: autors «Francesc Ferrer de Llupià» · any «1796» · descripció «Palau Savassona» | AUTO |
| `biblioteca-francesc-candel` | edifici_original: «Fàbrica Lámparas Z – Philips. Antoni Grau. 1954» | nova intervenció «Projecte original»: autors «Antoni Grau» · any «1954» · descripció «Fàbrica Lámparas Z – Philips» | AUTO |
| `biblioteca-francesca-bonnemaison` | edifici_original: «Casa senyorial. s.» | Text truncat o sense any: completar amb el WordPress en producció | MANUAL |
| `biblioteca-gotic-andreu-nin` | edifici_original: «Gran Hotel Falcón. Juli Marial. 1879» | nova intervenció «Projecte original»: autors «Juli Marial» · any «1879» · descripció «Gran Hotel Falcón» | AUTO |
| `biblioteca-horta-can-mariner` | edifici_original: «Masia de Can Mariner. s.» | Text truncat o sense any: completar amb el WordPress en producció | MANUAL |
| `biblioteca-ignasi-iglesias-can-fabra` | edifici_original: «Filatura Fabra i Coats. 1880» | nova intervenció «Projecte original»: autors «» · any «1880» · descripció «Filatura Fabra i Coats» | REVISA |
| `biblioteca-la-fraternitat` | edifici_original: «Cooperativa Obrera La Fraternitat de la Barceloneta. Francesc Guàrdia i Vial. 1918» | nova intervenció «Projecte original»: autors «Francesc Guàrdia i Vial» · any «1918» · descripció «Cooperativa Obrera La Fraternitat de la… | AUTO |
| `biblioteca-les-roquetes-rafa-juncadella` | edifici_original: «Centre Cívic. Marcià Codinachs. 1992» | nova intervenció «Projecte original»: autors «Marcià Codinachs» · any «1992» · descripció «Centre Cívic» | AUTO |
| `biblioteca-montbau-albert-perez-baro` | edifici_original: «Escola Enric Borràs. Anys 60 del s.» | Text truncat o sense any: completar amb el WordPress en producció | MANUAL |
| `biblioteca-montserrat-abello` | edifici_original: «Fàbrica Benet Campabadal. Antoni Pons i Domínguez. 1924» | nova intervenció «Projecte original»: autors «Antoni Pons i Domínguez» · any «1924» · descripció «Fàbrica Benet Campabadal» | AUTO |
| `biblioteca-nou-barris-aurora-diaz-plaja` | edifici_original: «Institut Mental de la Santa Creu. Josep Oriol i Bernadet. 1889» | nova intervenció «Projecte original»: autors «Josep Oriol i Bernadet» · any «1889» · descripció «Institut Mental de la Santa Creu» | AUTO |
| `biblioteca-poble-sec-francesc-boix` | edifici_original: «Escola construïda per la societat benèfica Juntas de Señoras de Salas de Asilos. 1889.» | nova intervenció «Projecte original»: autors «» · any «1889» · descripció «Escola construïda per la societat benèfica Juntas de Señoras d… | REVISA |
| `biblioteca-poblenou-manuel-arranz` | edifici_original: «Fàbrica tèxtil de Can Saladrigas. Francisco Pascual. 1884» | nova intervenció «Projecte original»: autors «Francisco Pascual» · any «1884» · descripció «Fàbrica tèxtil de Can Saladrigas» | AUTO |
| `biblioteca-sant-pau-santa-creu` | edifici_original: «Hospital de la Santa Creu. Guillem Abiell. 1406.» | nova intervenció «Projecte original»: autors «Guillem Abiell» · any «1406» · descripció «Hospital de la Santa Creu» | AUTO |
| `biblioteca-vapor-vell` | edifici_original: «Fàbrica tèxtil El Vapor Vell. 1846» | nova intervenció «Projecte original»: autors «» · any «1846» · descripció «Fàbrica tèxtil El Vapor Vell» | REVISA |
| `illa-dequipaments-alchemika` | edifici_original: «Fàbrica tèxtil Bonaventura Costa i Font. Francesc Mitjans i Miró Miró. 1948» | nova intervenció «Projecte original»: autors «Francesc Mitjans i Miró Miró» · any «1948» · descripció «Fàbrica tèxtil Bonaventura Costa i… | REVISA |

## 4. Etiqueta «Categoria:» del WordPress dins la descripció (50)

| Fitxa | Ara | Proposta | Tipus |
|---|---|---|---|
| `acabados-tintes-y-estampados` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica tèxtil. Actualment, sense ús.» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | REVISA |
| `antic-escorxador` | intervencions[0].descripcio: «Categoria: Altres edificis Antic escorxador. Actualment les dues naus tenen un ú» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | REVISA |
| `ca-lilla` | intervencions[0].descripcio: «Categoria: Recinte industrial Indústria de blanqueig de teixits, tints i apresto» | tipologia: «Recinte industrial» (si està buida) i treure l'etiqueta del text | AUTO |
| `caldereria-de-joan-feiner` | intervencions[0].descripcio: «Categoria: Fàbrica Antic taller de caldereria. Actualment, bar nocturn L’Ovella » | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `can-culleres` | intervencions[0].descripcio: «Categoria: Altres edificis Fàbrica de coberts d’alpaca i llautó Metales y Plater» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `can-pico-biciclot` | intervencions[1].descripcio: «Categoria: Altres edificis Magatzem i habitatge de Miquel Picó. Actualment, Bici» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `can-ricart` | intervencions[0].descripcio: «Categoria: Recinte industrial Can Ricart va ser una de les primeres fàbriques d’» | tipologia: «Recinte industrial Can» (si està buida) i treure l'etiqueta del text | AUTO |
| `casino-familiar` | intervencions[0].descripcio: «Categoria: Altres edificis Centre de la Joventut Democràtica Radical Instructiva» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `casino-lalianca-del-poblenou` | intervencions[0].descripcio: «Categoria: Altres edificis Entitat cultural. Actualment, mateix ús.» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `centre-moral-del-poblenou` | intervencions[0].descripcio: «Categoria: Altres edificis Entitat cultural. Actualment, mateix ús.» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `colores-hispania` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de tints i acabats tèxtils. Actualment, sense ús.» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `cooperativa-la-flor-de-maig-sucursal` | intervencions[0].descripcio: «Categoria: Altres edificis Sucursal de la cooperativa obrera i fàbrica de gasose» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `cunill-orfebres` | intervencions[0].descripcio: «Categoria: Fàbrica Seu del taller d’orfebreria Cunill e Hijos (posteriorment Cun» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `edifici-del-rellotge` | intervencions[0].descripcio: «Categoria: Altres edificis Magatzem i habitatges per a treballadors de l’empresa» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `edifici-ricard-ametlla-montana` | intervencions[0].descripcio: «Categoria: Altres edificis Usos industrials. Actualment, mateix ús.» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `fabrica-dalbert-musteros` | intervencions[1].descripcio: «Categoria: Fàbrica Fàbrica. Actualment, coworking , estudis d’artistes, sala de » | tipologia: «Fàbrica Fàbrica. Actualment, coworking , estudis d’artistes, sala de concerts i discoteca Razzmatazz, etc.» (si està buida) i… | AUTO |
| `fabrica-de-gel-la-siberia` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de gel. Actualment, pendent d’una reforma de gran par» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `fabrica-de-gel-sant-antoni` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de gel. Actualment, seu d’una empresa de roba.» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `fabrica-de-joan-guell` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de teixits. Actualment, sense ús, pendent de reforma » | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `fabrica-letona` | intervencions[0].descripcio: «Categoria: Fàbrica Indústria làctica. Actualment en desús.» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `fabrica-valls-teixidor-i-jordana` | intervencions[0].descripcio: «Categoria: Fàbrica amb xemeneia Fàbrica de productes mèdics, ortopèdics i farmac» | tipologia: «Fàbrica amb xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `filatura-el-canem` | intervencions[1].descripcio: «Categoria: Fàbrica Filatura de jute. Actualment, Centre d’Urgències i Emergèncie» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `frigo-farga` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de gelats, xocolates i torrons, encara en funcionamen» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `galetes-i-xocolata-solsona-i-rius` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de galetes i xocolates. Actualment, seu d’una empresa» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `galetes-vinas-la-galeta` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de galetes. Actualment, oficines i espais comercials » | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `habitatges-de-can-culleres` | intervencions[0].descripcio: «Categoria: Altres edificis» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `huracan-motors-razzmatazz` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de motors. Actualment, sala de concerts i discoteca R» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `industrias-deslite` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de coixinets. Actualment, pendent d’una reforma de gr» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `industrias-waldes` | intervencions[0].descripcio: «Categoria: Fàbrica Magatzems i trulls. Des de 1924, seu d’Industrias Waldes (emp» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `la-union-metalurgica` | intervencions[0].descripcio: «Categoria: Fàbrica Pavelló d’entrada d’una indústria de materials i objectes met» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `magatzem-de-draps-de-francisco-munne-bau` | intervencions[0].descripcio: «Categoria: Altres edificis Magatzem de draps. Actualment, seu del BAU (Centre Un» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `magatzem-del-banco-hispano-americano` | intervencions[0].descripcio: «Categoria: Altres edificis Magatzem i habitatge. Actualment, comerços i habitatg» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `magatzem` | intervencions[0].descripcio: «Categoria: Altres edificis Magatzem. Actualment, mateix ús.» | tipologia: «Altres edificis Magatzem. Actualment, mateix ús.» (si està buida) i treure l'etiqueta del text | AUTO |
| `nau-industrial-modernista` | intervencions[0].descripcio: «Categoria: Fàbrica Magatzem industrial d’estil modernista. Actualment, edifici m» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `naus-industrials-adossades` | intervencions[0].descripcio: «Categoria: Fàbrica Conjunt de tres naus d’estil modernista.» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `olis-pallares` | intervencions[1].descripcio: «Categoria: Altres edificis Magatzem d’olis i habitatges. Actualment, ús industri» | tipologia: «Altres edificis» (si està buida) i treure l'etiqueta del text | AUTO |
| `palo-alto` | intervencions[0].descripcio: «Categoria: Recinte industrial Filatura de llana Gal i Puigsech. Actualment anome» | tipologia: «Recinte industrial» (si està buida) i treure l'etiqueta del text | AUTO |
| `pastes-magin-quer` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica de pastes alimentàries per a sopes. Actualment, seu d» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `tallers-oliva-artes` | intervencions[2].descripcio: «Categoria: Fàbrica Tallers de construcció mecànica. Actualment un edifici és la » | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `tules-y-encajes` | intervencions[0].descripcio: «Categoria: Fàbrica Fàbrica tèxtil. Actualment, sense ús.» | tipologia: «Fàbrica» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-buigas-i-samso` | intervencions[0].descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-can-folch` | intervencions[0].descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-can-girona-macosa` | intervencions[0].descripcio: «Categoria: xemeneia» | tipologia: «xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-la-foneria-giralt` | intervencions[0].descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-la-nubiola` | descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-la-ram` | intervencions[0].descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-lelectrolisis` | intervencions[0].descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia-de-tallada-i-lora` | intervencions[0].descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `xemeneia` | descripcio: «Categoria: Xemeneia» | tipologia: «Xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |
| `yorka-abans-apresto-de-sederias` | intervencions[0].descripcio: «Categoria: Fàbrica amb xemeneia Indústria tèxtil. Actualment, seu d’una agència » | tipologia: «Fàbrica amb xemeneia» (si està buida) i treure l'etiqueta del text | AUTO |

## 5. Premis dins la descripció (4)

| Fitxa | Ara | Proposta | Tipus |
|---|---|---|---|
| `entorns-del-mercat-del-born` | intervencions[0].descripcio: «Premi Ciutat de Barcelona» | premis: «Premi Ciutat de Barcelona» | REVISA |
| `fabrica-de-creacio-fabra-i-coats` | intervencions[0].descripcio: «Premi Ciutat de Barcelona» | premis: «Premi Ciutat de Barcelona» | REVISA |
| `la-borda-cohabitatges-cooperatius` | intervencions[0].descripcio: «Premi Ciutat de Barcelona Premi Emergent Mies van der Rohe» | premis: «Premi Ciutat de Barcelona» | REVISA |
| `passeig-maritim-de-la-barceloneta` | intervencions[0].descripcio: «Premi FAD d’Espais Exteriors 1996 La part de passeig més propera al barri se sit» | premis: «Premi FAD d’Espais Exteriors 1996» | REVISA |

## 6. «Projecte original», «Reforma», «Rehabilitació»… dins la descripció (69)

| Fitxa | Ara | Proposta | Tipus |
|---|---|---|---|
| `biblioteca-francesca-bonnemaison` | descripcio: «Remodelació: Institut de Cultura i Biblioteca Popular per a la Dona. Josep Fontserè i Mest» | «Remodelació» dins el text: passar-ho a intervenció a mà | MANUAL |
| `biblioteca-gotic-andreu-nin` | intervencions[0].descripcio: «Andreu Nin Polític marxista, escriptor i traductor. 1892-1937 Trasllat previst segons Pla » | «Reforma» dins el text: passar-ho a intervenció a mà | MANUAL |
| `biblioteca-montbau-albert-perez-baro` | descripcio: «Biblioteca: 1991 Remodelació: Oliveras Boix Arquitectes. 2015» | Ja és a les intervencions (Remodelació: Oliveras Boix Arquitectes, 2015): treure-ho només del text | AUTO |
| `biblioteca-sofia-barat` | descripcio: «Sofia Barat Religiosa. 1779-1865 Arquitecte: Judith Masana. 2000 Trasllat previst segons P» | «Reforma» dins el text: passar-ho a intervenció a mà | MANUAL |
| `ca-lalier` | intervencions[0].descripcio: «Projecte original:1853 / 1877 (naus actuals) Categoria: Fàbrica amb xemeneia L’antiga fàbr» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `caixaforum` | intervencions[0].descripcio: «Projecte original: Fàbrica Casaramona. Josep Puig i Cadafalch. 1911» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `can-felipa` | intervencions[0].descripcio: «Projecte original: 1885 / Inici s. xx (menjadors) Categoria: Fàbrica Fàbrica tèxtil CATEX » | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `can-framis-fundacio-vila-casas` | intervencions[0].descripcio: «Projecte original: Primera meitat s. xix Premi Ciutat de Barcelona d’Arquitectura 2009 Cat» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `can-gili-nou` | intervencions[0].descripcio: «Projecte original:1876-1880 Categoria: Fàbrica Farinera i magatzems. Actualment, habitatge» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `can-gili-vell` | intervencions[0].descripcio: «Projecte original: 1877 / 1903 (xemeneia) Categoria: Fàbrica amb xemeneia Farinera La Fama» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `can-jaumandreu-vapor-de-la-llana` | intervencions[1].descripcio: «Projecte original:Joaquim Vilaseca i Ribera i Josep Marimon i Cot. 1873 Categoria: Fàbrica» | nova intervenció «Projecte original»: autors «Joaquim Vilaseca i Ribera i Josep Marimon i Cot» · any «1873» | REVISA |
| `can-saladrigas` | intervencions[0].descripcio: «Projecte original: Joan Barba, Pedro Molinas Coll, Pedro Bosch, Maldo Waura i Francisco Pa» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `casa-lesseps` | intervencions[0].descripcio: «Projecte original: Segle XVIII A l’altra banda de l’església, i simètrica respecte a l’edi» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `centre-de-cultura-contemporania-de-barcelona-cccb` | intervencions[0].descripcio: «Projecte original: Casa de la Caritat. Josep Oriol Mestres. 1861 Premi Ciutat de Barcelona» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `cooperativa-la-flor-de-maig` | intervencions[0].descripcio: «Projecte original:1896 Categoria: Altres edificis Cooperativa obrera. Actualment, ateneu p» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `cooperativa-pau-i-justicia-sala-beckett` | intervencions[0].descripcio: «Projecte original: Josep Masdeu. 1924 Premi Ciutat de Barcelona d’Arquitectura Categoria: » | nova intervenció «Projecte original»: autors «Josep Masdeu» · any «1924» | REVISA |
| `cosmocaixa-barcelona` | intervencions[0].descripcio: «Projecte original: Asil per a cecs Empar de Santa Llúcia. Josep Domènech i Estapà. 1909 Am» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `edifici-dhabitatges-placa-sant-miquel` | intervencions[0].descripcio: «Projecte original: Segle XVIII Aquest edifici té l’origen en les cases originals del barri» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `el-born-muhba-mercat-del-born` | descripcio: «Projecte original: Josep Fontserè i Mestre i Josep Maria Cornet i Mas. 1876 Enric Sòria i » | nova intervenció «Projecte original»: autors «Josep Fontserè i Mestre i Josep Maria Cornet i Mas» · any «1876» | REVISA |
| `el-sucre` | intervencions[0].descripcio: «Projecte original: c. 1911 Categoria: Fàbrica Sucrera Compañía de Industrias Agrícolas. Ac» | «Projecte original» sense autor clar: passar-ho a intervenció a mà | MANUAL |
| `escola-josep-maria-jujol` | intervencions[0].descripcio: «Adreça: Riera de Sant Miquel, 39 Projecte original: Tallers Manyach. Josep Maria Jujol. 19» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `esglesia-de-sant-miquel-del-port` | intervencions[0].descripcio: «Projecte original: Pedro Martín Cermeño. Damià Ribas i Francisco Paredes. 1755 Originalmen» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `farinera-la-asuncion` | intervencions[0].descripcio: «Projecte original: Josep Plantada i Artigas. 1917 Categoria: Fàbrica Farinera. Actualment,» | nova intervenció «Projecte original»: autors «Josep Plantada i Artigas» · any «1917» | REVISA |
| `la-escocesa` | descripcio: «Projecte original: 1852 Múltiples reformes i ampliacions posteriors Categoria: Recinte ind» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `la-favorita` | intervencions[0].descripcio: «Projecte original: Inici s. xx Categoria: Fàbrica Fàbrica de teixits. Actualment, seu de d» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-canyelles` | descripcio: «Projecte original: Albert de Pablo. 1987» | nova intervenció «Projecte original»: autors «Albert de Pablo» · any «1987» | REVISA |
| `mercat-de-ciutat-meridiana` | intervencions[0].descripcio: «Projecte original: 1968» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-felip-ii` | intervencions[0].descripcio: «Projecte original: Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas). 1966» | nova intervenció «Projecte original»: autors «Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas)» · any «1966» | REVISA |
| `mercat-de-galvany` | descripcio: «Projecte original: Pere Falqués i Urpí. 1868-1927» | nova intervenció «Projecte original»: autors «Pere Falqués i Urpí» · any «1868-1927» | REVISA |
| `mercat-de-la-barceloneta` | intervencions[0].descripcio: «Projecte original: Antoni Rovira i Trias. 1884 Premi Ciutat de Barcelona La construcció or» | nova intervenció «Projecte original»: autors «Antoni Rovira i Trias» · any «1884» | REVISA |
| `mercat-de-la-boqueria` | intervencions[0].descripcio: «Projecte original: Josep Mas i Vilà / Antoni de Falguera. 1840 / 1914 Façana posterior: Ca» | nova intervenció «Projecte original»: autors «Josep Mas i Vilà / Antoni de Falguera» · any «1840» | REVISA |
| `mercat-de-la-concepcio` | intervencions[0].descripcio: «Projecte original: Antoni Rovira i Trias. 1888» | nova intervenció «Projecte original»: autors «Antoni Rovira i Trias» · any «1888» | REVISA |
| `mercat-de-la-guineueta` | intervencions[0].descripcio: «Projecte original: Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas). 1965» | nova intervenció «Projecte original»: autors «Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas)» · any «1965» | REVISA |
| `mercat-de-la-llibertat` | intervencions[0].descripcio: «Projecte original: Miquel Pasqual i Tintorer i Francesc Berenguer i Mestres (decoració). 1» | nova intervenció «Projecte original»: autors «Miquel Pasqual i Tintorer i Francesc Berenguer i Mestres (decoració)» · any «1888» | REVISA |
| `mercat-de-la-marina` | descripcio: «Projecte original: 1973 Nou mercat (canvi d’ubicació): Albert de Pineda. 2003» | nova intervenció «Projecte original»: autors «1973 Nou mercat (canvi d’ubicació): Albert de Pineda» · any «2003» | REVISA |
| `mercat-de-la-merce` | descripcio: «Projecte original: Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas). 1961» | nova intervenció «Projecte original»: autors «Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas)» · any «1961» | REVISA |
| `mercat-de-la-montserrat` | descripcio: «Projecte original: Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas). 1960» | nova intervenció «Projecte original»: autors «Estudi AGR (Josep Anglada, Daniel Gelabert i Josep Ribas)» · any «1960» | REVISA |
| `mercat-de-la-sagrada-familia` | descripcio: «Projecte original: 1944 Nou edifici: 1993» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-la-trinitat` | intervencions[0].descripcio: «Projecte original: 1977» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-la-vall-dhebron-teixonera` | intervencions[0].descripcio: «Projecte original: 1969» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-les-corts` | intervencions[0].descripcio: «Projecte original: 1961» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-les-tres-torres` | descripcio: «Projecte original: Joan Baptista Subirana. 1958» | nova intervenció «Projecte original»: autors «Joan Baptista Subirana» · any «1958» | REVISA |
| `mercat-de-lesseps` | intervencions[0].descripcio: «Projecte original: 1974» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-lestrella` | descripcio: «Projecte original: 1957» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-nuria` | descripcio: «Projecte original: Fernando Bendala i Samuel Mañá. 1966» | nova intervenció «Projecte original»: autors «Fernando Bendala i Samuel Mañá» · any «1966» | REVISA |
| `mercat-de-provencals` | intervencions[0].descripcio: «Projecte original: 1974» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-sant-andreu` | descripcio: «Projecte original: Jacint Boada i Batllori. 1914 Pendent de nou edifici» | nova intervenció «Projecte original»: autors «Jacint Boada i Batllori» · any «1914» | REVISA |
| `mercat-de-sant-antoni` | intervencions[0].descripcio: «Projecte original: Antoni Rovira i Trias. 1882 Inclou els Encants de Sant Antoni especiali» | nova intervenció «Projecte original»: autors «Antoni Rovira i Trias» · any «1882» | REVISA |
| `mercat-de-sant-gervasi` | intervencions[0].descripcio: «Projecte original: 1968» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-sant-marti` | intervencions[0].descripcio: «Projecte original: 1966» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-de-santa-caterina-i-habitatges-per-ancians` | intervencions[0].descripcio: «Projecte original: Josep Mas i Vilà i Josep Buxareu. 1848 Premi Ciutat de Barcelona» | nova intervenció «Projecte original»: autors «Josep Mas i Vilà i Josep Buxareu» · any «1848» | REVISA |
| `mercat-de-sants` | intervencions[0].descripcio: «Projecte original: Pere Falqués i Urpí. 1892-1913» | nova intervenció «Projecte original»: autors «Pere Falqués i Urpí» · any «1892-1913» | REVISA |
| `mercat-de-sarria` | intervencions[0].descripcio: «Projecte original: Marcel·lià Coquillat i Arnau Calvet. 1911» | nova intervenció «Projecte original»: autors «Marcel·lià Coquillat i Arnau Calvet» · any «1911» | REVISA |
| `mercat-del-besos` | descripcio: «Projecte original: 1968» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-del-bon-pastor` | descripcio: «Projecte original: Enric Piqué Marco i Antoni Canyelles i Torrent. 1960 Nou edifici: AA25 » | nova intervenció «Projecte original»: autors «Enric Piqué Marco i Antoni Canyelles i Torrent» · any «1960» | REVISA |
| `mercat-del-carmel` | descripcio: «Projecte original: 1969» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `mercat-del-clot` | intervencions[0].descripcio: «Projecte original: Pere Falqués i Urpí. 1889» | nova intervenció «Projecte original»: autors «Pere Falqués i Urpí» · any «1889» | REVISA |
| `mercat-del-guinardo` | descripcio: «Projecte original: Bonaventura Bassegoda i Musté. 1954 Remodelació i nou edifici: Lluís Ca» | nova intervenció «Projecte original»: autors «Bonaventura Bassegoda i Musté» · any «1954» | REVISA |
| `mercat-del-ninot` | intervencions[0].descripcio: «Mercat a l’aire lliure: 1894 Projecte original: Antoni de Falguera i Joaquim Vilaseca. 193» | nova intervenció «Projecte original»: autors «Antoni de Falguera i Joaquim Vilaseca» · any «1933» | REVISA |
| `mercat-del-poblenou` | intervencions[0].descripcio: «Projecte original: Pere Falqués i Urpí. 1889» | nova intervenció «Projecte original»: autors «Pere Falqués i Urpí» · any «1889» | REVISA |
| `mercat-delabaceria` | descripcio: «Projecte original: Joan Torras Guardiola. 1892» | nova intervenció «Projecte original»: autors «Joan Torras Guardiola» · any «1892» | REVISA |
| `mercat-dhorta` | descripcio: «Projecte original: Ramon Térmens i Mauri. 1951 Pendent de remodelació» | nova intervenció «Projecte original»: autors «Ramon Térmens i Mauri» · any «1951» | REVISA |
| `mercat-dhostafrancs` | intervencions[0].descripcio: «Projecte original: Antoni Rovira i Trias. 1888» | nova intervenció «Projecte original»: autors «Antoni Rovira i Trias» · any «1888» | REVISA |
| `naus-de-la-familia-ametller` | intervencions[0].descripcio: «Rehabilitació: G56. 2008 Categoria: Fàbrica Magatzems per llogar (llogaters: Galetes Solso» | «Rehabilitació» sense autor clar: passar-ho a intervenció a mà | MANUAL |
| `palau-de-mar-magatzems-generals-de-comerc` | intervencions[0].descripcio: «Projecte original: Maurici Garrán i Elies Rogent. 1881-1900 Construït per emmagatzemar les» | nova intervenció «Projecte original»: autors «Maurici Garrán i Elies Rogent» · any «1881-1900» | REVISA |
| `piscina-de-salts-de-montjuic` | intervencions[0].descripcio: «Projecte original: Josep Serra Robert. 1929» | nova intervenció «Projecte original»: autors «Josep Serra Robert» · any «1929» | REVISA |
| `seu-central-de-la-diputacio-de-barcelona` | intervencions[0].descripcio: «Adreça: Rbla. Catalunya, 126 Projecte original: Casa Serra. Josep Puig i Cadafalch. 1908» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |
| `torre-de-les-aigues-del-besos` | intervencions[0].descripcio: «Rehabilitació: Antoni Vilanova i Eduard Simó. 2010-2014 Categoria: Xemeneia La Torre de le» | nova intervenció «Rehabilitació»: autors «Antoni Vilanova i Eduard Simó» · any «2010-2014» | REVISA |
| `vapor-llull` | intervencions[1].descripcio: «Projecte original: Inici s. xx (1902?) Premi Ciutat de Barcelona d’Arquitectura 1998 Categ» | «Projecte original» dins el text: passar-ho a intervenció a mà | MANUAL |

