<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🔬 La IA ens deixarà sense treball i haurem de plantar tomàquets i criar gallines 🌱

</h1>

-----

# El repte 👨‍🌾👩‍🌾

Aquest any, apostem per un problema molt més ampli que inclogui no només la part de data scientist de la unitat d'Applied Artificial Intelligence, sinó que també requereixi experimentar altres camps, com pot ser TODO


## Les missions 🍅
Per a familiaritzar-nos amb les plantes per a quan hàgim d'anar a plantar tomàquets, hem fundat el Departament Vegetal d'AAI i definit un pla d'execució format per cinc missions:

- 🌼 **Missió Margarida**
- 🌷 **Missió Tulipa**
- 🎋 **Missió Bambú**
- 🥑 **Missió Alvocat**
- 🍑 **Missió Préssec**

A excepció de la `🌼 MISSIÓ MARGARITA`, aquestes missions no són necessàriament seqüencials: podeu fer-les de manera paral·lela entre els companys, o anar saltant d'una a una altra en funció de la vostra inspiració... Fins i tot podeu no fer algunes i inventar-vos-en d'altres. 

No dubtéu en vindre a la ambaixada del Departament Vegetal d'AAI (AKA les taules de la HackEPS on es troven els representants d'Eurecat) per validar les vostres idees si teniu algún dubte sobre si entra dins de la idea general del repte.

La `🌼 MISSIÓ MARGARIDA` **ÉS OBLIGATÒRIA**.

![](https://media.tenor.com/aeV80XD4CSgAAAAd/guidlines-pirates-of-the-caribbean.gif)

No patiu! 🥴 Sabem que conteu només amb 24h… No valorem exclusivament el nombre de missions que completeu, sinó que aprengueu del repte i sigueu capaços de ser prou analítics per aportar una solució i un punt de vista als problemes que se us plantegen.


### 🌼 MISSIÓ MARGARIDA 
Abans de poder començar cap tasca, cal obtenir dades. 

A les nostres instal·lacions tenim un hort enviant dades a un servidor d'Eurecat mitjançant el procol MQTT a temps real. En aquest servidor es troba un broker Mosquitto. Demaneu a la taula d’eurecat que us donin un usuari i contrasenya per a poder fer la connexió i escoltar els missatges que transmeten les plantes cap al topic `hort/plantes`

El Departament Vegetal necessita poder guardar les dades d'alguna forma per la posterior visualització i anàlisi.

### 🌷 MISSIÓ TULIPA
Un cop disposeu d'un sistema per guardar les dades a temps real, sol·liciteu al Departament Vegetal d'AAI d'Eurecat el _Ultimate SensorPlanta Kit 2023_.

Aquest kit conté el material necessari per a poder connectar una nova planta a l'hort digital i enviar les dades de la planta al topic `/hort/team/{nom assignat a l'equip}`

Envieu les dades disponibles de la nova planta al servidor i enregistreu-les juntament amb la resta de dades de l'hort.

### 🎋 MISSIÓ BAMBÚ
Per culpa d’algun becari >:(, les dades que vam enregistrar inicialment no estan completes, ja que falta el tipus de planta del que es tracta cada entrada. Per a no perdre tot aquest progrés, la unitat de nyaps va guardar aquestes dades en un dataset **TBD: com donar el _dataset_**.

Departament Vegetal vol conèixer el tipus de planta de les dades antigues, però només sabem que el comportament de les plantes actuals és similar al de les plantes enregistrades al dataset.

### 🥑 MISSIÓ ALVOCAT
L'obsessió per programar preocupa al Departament Vegetal, ja que les plantes es moriran de set si continua aquesta dinàmica! Com que agafar una regadora i regar-les regularment no sembla ser una opció, s'ha fet entrega d'una bomba d’aigua perquè pugueu automatitzar-ho. 

Afegiu la bomba d'aigua al sistema i habiliteu algun mecanisme per a regar la planta.

### 🍑 MISSIÓ PRÉSSEC
Interactuar amb les dades és gairebé tan important com tenir-les. El departament de desenvolupament d'interfícies atractives, col·laboradors habituals del departament vegetal de AAI, ha estat subcontractat per idear una manera de poder explotar aquestes dades, però estan més secs d'idees que una noguera al gener.

Ideeu, dissenyeu i desenvolupeu eines relacionades amb el curo del hort digital, que idealment facin ús de les dades recollides en qualsevol de les altres missions.

## Com començar?

### Recursos 📦
Inicialment disposareu d'accés a un Broker MQTT:
> IP: 84.88.76.18
>
> Port: 1883
>
> Usuari i contrasenya: _Vine a preguntar!_

Topics MQTT:
> `hort/plantes`
>
> `hort/team/{Nom assignat a l'equip}`

Una vegada avançada la missió margarida, podreu sol·licitar el _Ultimate SensorPlanta Kit 2023_ a la nostra taula, el qual constarà de:
|    **ESP3288**   	|      **Cable MicroUSB**     	|           **Planta**          	|
|:----------------:	|:---------------------------:	|:-----------------------------:	|
|    **Díodes**    	|        **Protoboard**       	|       **Bomba d'aigua**       	|
| **Resistències** 	| **Convertidor de Voltatge** 	| **Diversos sensors i cables** 	|

### Recomanacions
Us recomanem que feu servir el llenguatge de programació amb el que estigueu més còmodes. Per programar el microcontrolador, podreu fer servir C, C++, Micro-Python, Lua o JavaScript. Per la visualització de dades, podeu fer servir python, juntament amb la utilització de [notebooks](https://jupyter.org/).

Aquestes són algunes biblioteques (**LIBRARY != LLIBRERIA**) i eines que podríeu utilitzar per a dur a terme les tasques que es presenten en les missions:

Per la connexió al broker MQTT:
- [MQTTX](https://mqttx.app/)
- [Eclipse PAHO (biblioteca MQTT per a molts llenguatges populars)](https://eclipse.dev/paho/)

Pel desenvolupament del Microcontrolador:
- [Arduino IDE](https://www.arduino.cc/en/software)
- [ESP8266 Datasheet (Summary)](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/documentation/NodeMCU%20Documentation.pdf)
- [ESP8266 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf) 

Per a tractar dades
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [matplotlib](https://pypi.org/project/matplotlib/)

## La puntuació 👀

Tindrem en compte l'originalitat de les solucions i de la presentació, el percentatge de missions complertes,
l'eficàcia, l'eficiència, l'excel·lència i l'èxit en les solucions, el treball en equip, la comunicació i volem saber per què heu de ser l'equip guanyador.

### El premi 🏆
- 800€ pel 1r Premi
- 200€ pel 2n Premi 

Molta sort!
