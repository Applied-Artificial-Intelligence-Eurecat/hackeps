<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🔬 La IA ens deixarà sense treball i haurem de plantar tomàquets i criar gallines 🌱

</h1>

-----

## El repte 👨‍🔬👩‍🔬

Aquest any, apostem per un problema molt més ampli que abarqui no només la part de data scientist de la unitat d'Applied Artificial Intelligence, sinó que també requereixi experimentar altres camps com pot ser TODO


## Les missions 🎨
Per a familiaritzar-nos amb les plantes per a quan hàgim d'anar a plantar tomàquets, hem assignat una planta a cadascuna de les missions proposades:
- 🌼 MISSIÓ MARGARITA 
- 🌷 MISSIÓ TULIPA
- 🎋 MISSIÓ BAMBÚ
- 🥑 MISSIÓ ALBOCAT
- 🍑 MISSIÓ PRÈSSEC

A excepció de la `🌼 MISSIÓ MARGARITA`, aquestes missions no són necessàriament seqüencials: podeu fer-les de manera paral·lela entre els companys, o anar saltant d'una altra en funció de la inspiració... Fins i tot podeu no fer algunes i inventar-vos unes altres. La missió margarita **ES OBLIGATORIA**.


![](https://media.tenor.com/aeV80XD4CSgAAAAd/guidlines-pirates-of-the-caribbean.gif)

No patiu! 🥴 Sabem que conteu només de 24h… No valorem exclusivament el nombre de missions que completeu, sinó que aprengueu del repte i sigueu capaços de ser prou analítics per aportar una solución i un punt de vista als problemes que es plantegen.


### 🌼 MISSIÓ MARGARITA 
Abans de poder començar cap tasca, cal obtenir dades, i per a no centrar-nos únicament en la feina d’un data scientist, aquestes dades s’han d’obtenir a través d’un broker mqtt, protocol que s'utilitza per a IoT.

A les nostres instal·lacions tenim un hort enviant dades a temps real al topic `hort/plantes`. Volem que obtingueu aquestes dades connectant-vos-hi amb el link proporcionat anteriorment. Demaneu a la taula d’eurecat que us donin un usuari i contrasenya per a poder fer la connexió, i d’aquesta manera també tindreu un equip assignat per les pròximes missions.

### 🌷 MISSIÓ TULIPA
Un cop ja teniu les dades, podeu transmetre les vostres pròpies al broker amb les plantes que trobareu a la taula d’eurecat. Demostreu que heu complert la missió margarita, i us donaran la planta i tot el hardware necessari per a poder obtenir les vostres pròpies dades. Tenint el sistema de gestió de dades establert i la possibilitat de crear noves dades, hi ha moltes aplicacions possibles d’IoT 😉. Envieu la informació de la vostra planta al tòpic del vostre equip: `hort/team/{Nom assignat a l'equip}`

### 🎋 MISSIÓ BAMBÚ
Per culpa d’algun becari >:(, les dades que vam enregistrar inicialment no estan completes, ja que falta el tipus de planta del que es tracta cada entrada. Per a no perdre tot aquest progrés, vam guardar aquestes dades en un dataset **TBD: com donar el _dataset_**.

Donat que el comportament de les plantes és el mateix que el de les que sí que tenen l’espècie especificada, utilitza les dades que ja has obtingut per a predir quin tipus de planta es cadascuna del dataset incomplert. 

### 🥑 MISSIÓ ALBOCAT
Les plantes es moriran de set si et passes tota l’estona programant! Com que estar pendents de les plantes i regar-les regularment no sembla ser una opció, us hem donat també una bomba d’aigua per a que pugueu automatitzar-ho. Amb la informació d’humitat de les plantes que teniu, automatitzeu el reg per a la vostra planta adequadament.

### 🍑 MISSIÓ PRÈSSEC
TODO: no se si fer missió de front o deixar-ho obert

## Com començar?

### Recursos 📦
Inicialment dispondreu d'accés a un Broker MQTT:
> IP: 84.88.76.18
> Port: 1883
> Usuari i contrasenya: _Vine a preguntar!_

Topics MQTT:
- hort/plantes
- hort/team/{Nom assignat a l'equip}

Una vegada avançada la missió margarita, podreu solicitar el _Ultimate Definitive Kit Planta 2023_ al stant, el cual constara de:
1. 1x ESP3288
2. 1x Cable MicroUSB
4. 1x Planta
5. 1x Protoboard
6. 1x Bomba d'aigüa
7. 2x Diodes
8. Diversos sensors i cables   

### Recomanacions
Us recomanem python com a llenguatge de programació, i en cas de fer missions on s’hagi de visualitzar dades, recomanem també l’ús de [notebooks](https://jupyter.org/). Aquestes son algunes biblioteques (**LIBRARY != LLIBRERÍA**) que podrieu utilitzar per a dur a terme les tasques que es presenten en les missions.

Per la conexió al broker MQTT:
- [MQTTX](https://mqttx.app/)
- [Eclipse PAHO](https://eclipse.dev/paho/)

Per el desenvolupament del Microcontrolador:
- [Arduino IDE](https://www.arduino.cc/en/software)
- [ESP8266 Datasheet (Summary)]()
- [ESP8266 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf) 

Per a tractar dades

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [matplotlib](https://pypi.org/project/matplotlib/)

## La puntuació 👀

Tindrem en compte l'originalitat de les sol·lucions i de la presentació, el percentatge de missions complertes,
l'eficàcia, l'eficiència, l'excelència i l'èxit en les sol·lucions, el treball en equip, la comunicació i volem saber el
per què heu de ser l'equip guanyador.

Molta sort!
