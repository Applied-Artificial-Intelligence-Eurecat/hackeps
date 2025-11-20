<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

💫  NebulOuS: El teu propi clúster Multi-Cloud-edge ☁️

</h1>

-----
# El repte 🔎

Google Cloud, Amazon Web Services, Microsoft Azure... grans proveïdors que poden acabar fallant, i ho fan (alguns més que d'altres 😶‍🌫️). I en aquest moment, tothom hagués desitjat no dependre només d'un. 
Per això, aquest any us proposem ajudar aquell pobre diable que es va equivocar confiant només en un d'ells, i creeu una plataforma per crear clústers de màquines en diferents proveïdors 🤙 Desenvolupament de Programari, IA, DevOPS... en aquest repte podreu practicar totes les disciplines per aconseguir el vostre objectiu 😎
A més, pensem en allò local: qui no té per casa un servidor de 8 CPU i 16 GB de RAM esperant ser aprofitat per desplegar coses?
## Objectius
L'objectiu final pot ser fàcil de dir: **una plataforma per a la creació de clústers-multicloud-edge**, però aconseguir-ho pot ser una mica més aclaparador.

Per això, us suggerim alguns punts funcionals, que com diem cada any: **NO**, no cal que feu tots els punts (és una hackató), i sou lliures de donar-li el vostre propi enfocament original a la plataforma, nosaltres només suggerim idees ;) I si voleu seguir les idees, tampoc cal que les feu en aquest ordre... Si alguna cosa no us surt, intenteu passar a la següent.

I si no... Pregunteu!
<h4 align="center">

![](https://camo.githubusercontent.com/abee1b0ea2fb94ffd75986431a093a0f22aeb534a70d11b3fa493f2eda877355/68747470733a2f2f6d656469612e74656e6f722e636f6d2f616556383058443443536741414141642f677569646c696e65732d706972617465732d6f662d7468652d63617269626265616e2e676966)

_El Codi és més aviat el que en diries "directrius" que regles de veritat._
</h4>

### Gestió de dispositius
**000 - Hola? Sóc jo!**

Aconseguir connectar amb l'API de GCP i AWS a partir de les credencials que us facilitarem, i fins i tot permetre múltiples comptes registrats.

**001 - Cloud? Això és només l'ordinador d'un altre!**

A més del cloud, també és interessant poder comptar amb dispositius _edge_, com el vostre propi ordinador (o una VM), raspberries, etc. Tenir una llista d'aquests dispositius i poder donar-los d'alta i baixa també pot ser interessant. 
Donar d'alta i baixa nodes Edge 
> Si voleu connectar-vos per SSH a raspberries o ordinadors de companys, a part de compte amb els tallafocs, useu xarxa des del mòbil, ja que Eduroam sol tenir el mal costum de bloquejar connexions d'aquest tipus.

**010 - Què hi ha al cloud?**

Poder veure quins nodes poden crear-se en els proveïdors cloud: tipus de màquina, recursos, costos, etc. A més, és interessant poder filtrar o buscar tipus de màquines que compleixin certs requisits de HW i CPU.

### Creació del clúster

**011 - El clúster s'haurà de crear**

A partir d'una necessitat de X màquines amb Y recursos cada màquina, caldrà triar en quin proveïdor cloud i quines instàncies desplegar, o quins dispositius edge utilitzar.

> És totalment vàlid permetre a l'usuari triar manualment quines instàncies utilitzar, encara que també podeu intentar triar-ho "automàticament" a partir de mètriques que considereu vosaltres (preu? ping? ubicació?)

**100 - EMBUSTERO! Això no és un clúster**

Un cop triats els nodes _edge_ i/o creades les màquines cloud, s'hauria d'instal·lar i configurar (automàticament) en elles el programari necessari perquè actuïn com a clúster.

> Algunes opcions, de menys a més complexes, són Nomad, Docker Swarm, K3s o Kubernetes (però podeu usar el que vulgueu, com si voleu desenvolupar alguna cosa pròpia)

### Monitorització i desplegament

**101 - Tot va bé, molt bé, regular... malament!**

Permetre a l'usuari revisar l'estat del/dels clústers i el consum dels recursos dels nodes.

**110 - I això per a què serveix?**

Permetre a l'usuari desplegar una aplicació en el clúster.

## Què us donem? 
Als equips interessats a participar, us deixarem:
- Un Service Account per poder crear i gestionar màquines a `Google Cloud` (Cloud Engine)
- Una API Key per poder crear i gestionar màquines a `Amazon Web Services` (EC2)
- Accés a una API de LLM perquè pugueu generar i processar text natural 

## Consideracions
Queda totalment prohibit compartir la clau que se us assigni amb altres grups.

Procureu crear totes les màquines en regions europees.

Per seguretat, no es permet crear VMs amb gràfiques associades.

Per evitar-vos problemes, a Google Cloud Platform, es permet connexió des de fora des de qualsevol IP cap a tots els ports de les màquines que creeu.


### MOLT, MOLT, MOLTÍSSIM IMPORTANT
Si us plau, assegureu-vos d'EXCLOURE les credencials del repositori públic de GitHub. Podeu crear un fitxer `.gitignore` a la base del vostre projecte i afegir:
```.gitignore
**.json
```
Tot avís molt important té una història al darrere

![](https://i.imgflip.com/aaq9wn.jpg)

## Documentació i informació
Podeu connectar-vos a una màquina via [**SSH**](https://www.cloudflare.com/es-es/learning/access-management/what-is-ssh/). A més de connectar-vos per "usuari i contrasenya", també podeu registrar una clau SSH que podeu generar amb:

```sh
ssh-keygen -t rsa -b 4096 -C "username"
```

Això us dóna una clau privada (amb el nom que indiqueu) i una pública (el nom que indiqueu + `.pub`). En crear un equip tant a AWS com a GCP podeu indicar-li la clau pública perquè pugueu connectar-vos amb SSH després:
```sh
ssh -i <arxiu> username@IP-DE-LA-MÀQUINA
```

### Clústers
```arduino
[AWS]          [Azure]          [GCP]
 Client VM     Client VM       Client VM
      \           |              /
       \          |             /
        \         |            /
            Master Node (VM)
```
- [Docker Swarm](https://docs.docker.com/engine/swarm/)
- [Nomad](https://developer.hashicorp.com/nomad)
- [K3s](https://k3s.io/)
- [K8s (Kubernetes)](https://kubernetes.io/)


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/1280px-Google_Cloud_logo.svg.png" width="300"/>

A Google Cloud Platform podeu utilitzar línia de comandes, i necessitareu instal·lar i configurar [`gcloud`](https://docs.cloud.google.com/sdk/docs/install).
També teniu biblioteques específiques per a gairebé cada llenguatge de programació:
- [Go](https://docs.cloud.google.com/go/docs)
- [JavaScript](https://docs.cloud.google.com/nodejs/docs)
- [Python](https://docs.cloud.google.com/python/docs)
- [Java](https://docs.cloud.google.com/java/docs)
- [C++](https://docs.cloud.google.com/cpp/docs)
- [C#](https://docs.cloud.google.com/dotnet/docs)

Teniu exemples de com usar les biblioteques a [el compte de Google Cloud Platform de Github](https://github.com/GoogleCloudPlatform).
En concret, el _producte_ que s'utilitza és [Compute Engine](https://cloud.google.com/products/compute?hl=es)

Es recomana que poseu l'idioma de la documentació en anglès, ja que les versions al castellà són bastant deficients.

A més, teniu uns exemples ChatGPT made perquè pugueu provar sense tornar-vos bojos en aquest mateix repositori, a `examples\google-cloud-platform`. Reviseu el README associat al llenguatge que vulgueu provar.

- [Python](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/tree/main/examples/google-cloud-platform/python)
- [Java](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/tree/main/examples/google-cloud-platform/java)


<img src="https://miro.medium.com/v2/resize:fit:1200/1*neG4D9C8UcJvNn6bverfIA.png" width="300"/>


# Guanyadors 🏅
En aquesta ocasió, s'anomenaran dos equips guanyadors:
- **Guanyadors:** Un premi a l'equip que aconsegueixi una solució més equilibrada entre qualitat, execució i idea
- **Joves promeses:** Premi destinat a equips els membres dels quals no tinguin coneixements previs, que presentin una solució ben ideada i demostrin la seva capacitat d'aprenentatge.

### Què es valorarà? 
Es valorarà tant la demo presentada durant l'exposició final com tota la informació inclosa en la publicació de Devpost (recordeu que podeu actualitzar-la fins i tot després del tancament). A partir d'això avaluarem, **principalment**:

**Per al primer premi**
- **Idees implementades:** Es tindrà en compte el nivell d'originalitat, les propostes que vagin més enllà del bàsic, els fluxos plantejats i qualsevol funcionalitat nova que resulti útil o pràctica.

- **Funcionalitat:** Com de bé funciona el projecte en el seu conjunt, l'estat de cada part, i la qualitat de la integració entre elles.

- **Arquitectura:** Valorarem si l'arquitectura proposada tindria sentit en un entorn real, si és escalable i si està ben plantejada.

- **Tecnologies:** No importa el llenguatge en si, sinó les tecnologies complementàries usades: frameworks web (React, Angular, Vue…), bases de dades (Mongo, Postgres, MariaDB…), contenidors (Docker), etc.

- **Qualitat del codi:** Tot i ser una hackató, es tindrà en compte evitar abusar de hardcoding, mantenir unes mínimes bones pràctiques (indentació, tipat en llenguatges no estrictament tipats, organització del projecte…).

**Per a joves promeses**
- **Idees implementades:** Igual que en la categoria general, es valorarà l'originalitat i l'aportació de funcionalitats útils més enllà del bàsic.

- **Aprenentatge:** Si hi havia o no experiència prèvia, què heu après en aquestes 24 hores, els principals reptes trobats i com els heu solucionat.

- **Treball en equip:** Com us heu organitzat, repartiment de tasques i dinàmica de col·laboració.

- **Qualitat del codi:** Mateixos criteris que en la categoria principal: evitar hardcoding innecessari i mantenir un mínim d'ordre i coherència.

- **Presentació de la idea:** Claredat en explicar la proposta, el seu enfocament i el seu objectiu.


## El premi 🤑

- Xec Amazon per valor de 1000€ per al **primer premi**
- Xec Amazon per valor de 200€ per al premi de **joves promeses**
