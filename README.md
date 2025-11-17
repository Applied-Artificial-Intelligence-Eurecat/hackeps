<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

💫  NebulOuS: El teu propi clúster Multi-Cloud-edge ☁️

</h1>

-----
## El repte 🔎

Google Cloud, Amazon Web Services, Microsoft Azure... grans proveïdors que poden acabar fallant, i ho fan (alguns més que d’altres 😶‍🌫️). I en aquest moment, tothom hagués desitjat no dependre’n només d’un.  
Per això, aquest any us proposem ajudar aquell pobre diable que es va equivocar confiant només en un d’ells, i crear una plataforma per crear clústers de màquines en diferents proveïdors 🤙 Desenvolupament de Programari, IA, DevOPS... en aquest repte podreu practicar totes les disciplines per aconseguir el vostre objectiu 😎  
A més, pensem en allò local: qui no té per casa un servidor de 8 CPU i 16 GB de RAM esperant ser aprofitat per desplegar coses?

## Objectius
L’objectiu final pot ser fàcil de dir: **una plataforma per a la creació de clústers-multicloud-edge**, però aconseguir-ho pot ser una mica més abrupte.

Per això, us suggerim alguns punts, que com diem cada any: **NO**, no cal que feu tots els punts (és una hackató), i sou lliures de donar-li el vostre propi enfocament original a la plataforma, nosaltres només suggerim idees ;)

I si alguna cosa no us surt... Pregunteu!
<h4 align="center">

![](https://camo.githubusercontent.com/abee1b0ea2fb94ffd75986431a093a0f22aeb534a70d11b3fa493f2eda877355/68747470733a2f2f6d656469612e74656e6f722e636f6d2f616556383058443443536741414141642f677569646c696e65732d706972617465732d6f662d7468652d63617269626265616e2e676966)

_El Codi és més aviat el que en diries "directrius" que regles de veritat._
</h4>

**00 - Què hi ha al cloud?**

Poder veure quins nodes poden crear-se en els proveïdors cloud  
> Cada proveïdor té les seves màquines amb els seus recursos... Podreu recuperar-los automàticament per poder triar més endavant l’opció més adequada?

**01 - Tant per triar...**  
A partir d’uns recursos, recuperar quins possibles nodes poden crear-se en els diferents proveïdors cloud registrats.  
> Si volem un node amb X GB de RAM i X nuclis de CPU... On l’hauríem de desplegar? Per què? Trieu mètriques o doneu la responsabilitat a l’usuari per trobar l’opció òptima!

**02 - El clúster s’haurà de crear**  
Rebre una llista de nodes i crear un clúster  
> Ja sabeu quines màquines voleu crear? Creeu-les i configureu-les perquè actuïn com un clúster!

**03 - L’usuari importa... oi?**  
Millorar l’experiència d’usuari  
> Una eina CLI per terminal? Una web amb formularis? O un chatbot? O potser una combinació de cada cosa?

**04 - Tot va bé, molt bé, regular... malament!**  
Monitoritzar clústers i nodes  
> Quants recursos queden al clúster? Com va cada node? Intenteu recuperar la informació i mostrar-la a l’usuari!

**05 - Cloud? Això és només l’ordinador d’un altre!**  
Donar d’alta i baixa nodes Edge  
> No tot es redueix al cloud... Us podeu connectar directament a màquines virtuals, raspberrys o altres ordinadors via SSH que poden actuar com a nodes (compte amb les limitacions de xarxa d’Eduroam...)

### Què us donem?
Als equips interessats a participar, us deixarem:
- Un Service Account per poder crear i gestionar màquines a `Google Cloud` (Cloud Engine)
- Una API Key per poder crear i gestionar màquines a `Amazon Web Services` (EC2)
- Accés a una API de LLM perquè pugueu generar i processar text natural

### Com puc fer un clúster?
Podeu usar la tecnologia que vulgueu. Si no teniu por de patir aquestes 24h us podeu arriscar amb K8s (Kubernetes), tot i que us recomanem alternatives més _Hackathon Friendly_ com [Docker Swarm](https://docs.docker.com/engine/swarm/)... Però tampoc us preocupeu gaire si el clúster no acaba de funcionar com a clúster.

### MOLT, MOLT, MOLT IMPORTANT
Si us plau, assegureu-vos d’EXCLOURE les credencials del repositori públic de GitHub. Podeu crear un fitxer `.gitignore` a la base del vostre projecte i afegir:
```.gitignore
**.json
```

Tot avís molt important té una història al darrere
![](https://i.imgflip.com/aaq9wn.jpg)

## Documentació

## Guanyadors 🏅
En aquesta ocasió, s’anomenaran dos equips guanyadors: 
- **Guanyadors:** Un premi a l’equip que aconsegueixi una solució més equilibrada entre qualitat, execució i idea 
- **Joves promeses:** Premi destinat a equips els membres dels quals no tinguin coneixements previs, que presentin una solució ben ideada i demostrin la seva capacitat d’aprenentatge.

### Què es valorarà? 

### El premi 🤑
- Xec Amazon per valor de 1000€ per al **primer premi** 
- Xec Amazon per valor de 200€ per al premi de **joves promeses**
