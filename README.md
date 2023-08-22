<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🔬 From Data Scientist to Garderner 🌱

</h1>

-----

## El repte 👨‍🔬👩‍🔬

Aquest any, apostem per un problema molt més ampli que abarqui no només la part de data scientist de la unitat d'Applied Artificial Intelligence, sinó que també requereixi experimentar altres camps com pot ser TODO

El repte està dividit en missions, tractant cada missió una disciplina diferent. A pesar d’això, no patiu! 🥴 Sabem que consteu només de 24h… No només valorem el nombre de missions que completeu, sinó que aprengueu del repte i sigueu capaços de ser prou analítics per aportar una solución i un punt de vista als problemes que es plantegen. Si en algun moment veieu que no us surt una missió, podeu passar a la següent o… fins i tot, crear les vostres pròpies missions amb els recursos que se us dona!


## Les missions 🎨

### Com començar?

Com que estem parlant d’un hort, hem relacionat cada missió amb una planta, a pesar de que no necessàriament es trobin totes a l‘hort. 
Us recomanem python com a llenguatge de programació, i en cas de fer missions on s’hagi de visualitzar dades, recomanem també l’ús de [notebooks](https://jupyter.org/). Aquestes son les llibreries més utilitzades per a dur a terme les tasques que es presenten en les missions.

Per la conexió al broker mqtt

- [paho.mqtt](https://pypi.org/project/paho-mqtt/)
  
Per a tractar dades

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [matplotlib](https://pypi.org/project/matplotlib/)

Coneixements de Machine Learning (ML) i Deep Learning (DL) seran útils en una de les missions. Us deixem aquí unes
llibreries.

- [scikit-learn](https://scikit-learn.org/stable/install.html)
- [tensorflow](https://www.tensorflow.org/)
- [pytorch](https://pytorch.org/)

Pel que fa a la visualització dels models:

- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://seaborn.pydata.org/)
- [plotly](https://plotly.com/)
- [tensorboard](https://www.tensorflow.org/tensorboard)
- [streamlit](https://streamlit.io/)

### Recursos 📦
L’única missió obligatoria en aquest repte és la primera, ja que no disposeu de dades inicialmente, a part de:

url: **HOST i PORT**

llista de topics:
- huerto/plantas
- huerto/team/_id_equipo_
  
Per tant, abans de poder començar amb cap altra missió, haureu de completar la missió margarita 🌼

### 🌼 MISSIÓ MARGARITA 
Abans de poder començar cap tasca, cal obtenir dades, i per a no centrar-nos únicament en la feina d’un data scientist, aquestes dades s’han d’obtenir a través d’un broker mqtt, protocol que s'utilitza per a IoT.

A les nostres instal·lacions tenim un hort enviant dades a temps real al topic huerto/plantas. Volem que obtingueu aquestes dades connectant-vos-hi amb el link proporcionat anteriorment. Demaneu a la taula d’eurecat que us donin un usuari i contrasenya per a poder fer la connexió, i d’aquesta manera també tindreu un equip assignat per les pròximes missions.

### 🌷 MISSIÓ TULIPA
Un cop ja teniu les dades, podeu transmetre les vostres pròpies al broker amb les plantes que trobareu a la taula d’eurecat. Demostreu que heu complert la missió margarita, i us donaran la planta i tot el hardware necessari per a poder obtenir les vostres pròpies dades. Tenint el sistema de gestió de dades establert i la possibilitat de crear noves dades, hi ha moltes aplicacions possibles d’IoT 😉. Envieu la informació de la vostra planta al tòpic del vostre equip: huerto/team/{Lletra del vostre equip}

### 🎋 MISSIÓ BAMBÚ
Per culpa d’algun becari >:(, les dades que vam enregistrar inicialment no estan completes, ja que falta el tipus de planta del que es tracta cada entrada. Per a no perdre tot aquest progrés, vam guardar aquestes dades en un dataset **TBD: com donar el _dataset_**.

Donat que el comportament de les plantes és el mateix que el de les que sí que tenen l’espècie especificada, utilitza les dades que ja has obtingut per a predir quin tipus de planta es cadascuna del dataset incomplert. 

### 🥑 MISSIÓ ALBOCAT
Les plantes es moriran de set si et passes tota l’estona programant! Com que estar pendents de les plantes i regar-les regularment no sembla ser una opció, us hem donat també una bomba d’aigua per a que pugueu automatitzar-ho. Amb la informació d’humitat de les plantes que teniu, automatitzeu el reg per a la vostra planta adequadament.

### 🍑 MISSIÓ PRÈSSEC
TODO: no se si fer missió de front o deixar-ho obert


## La puntuació 👀

Tindrem en compte l'originalitat de les sol·lucions i de la presentació, el percentatge de missions complertes,
l'eficàcia, l'eficiència, l'excelència i l'èxit en les sol·lucions, el treball en equip, la comunicació i volem saber el
per què heu de ser l'equip guanyador.

Molta sort!
