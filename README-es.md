<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

💫  NebulOuS: Tu propio cluster Multi-Cloud ☁️

</h1>

-----
## El reto 🔎

Google Cloud, Amazon Web Services, Microsoft Azure...  grandes proveedores que pueden acabar fallando, y lo hacen (algunos más que otros 😶‍🌫️). Y en ese momento, todo el mundo hubiese deseado no depender de uno solo.

Por eso, este año os proponemos ayudar a ese pobre diablo que se equivocó confiando solo en uno de ellos, y  creeis una plataforma para crear clusters de máquinas en distintos proveedores 🤙 Desarrollo de Software, IA, DevOPS... en este reto podréis practicar todas las disciplinas para conseguir vuestro objetivo 😎

## Objetivos
El objetivo final puede ser fácil de decir: **una plataforma para creación de clusters-multicloud**, pero lograrlo puede ser algo más abrumador.

Por ello, os sugerimos algunos puntos, que como decimos todos los años: **NO**, no hace falta que hagáis todos los puntos (es una hackathon), y sois libres darle vuestro propio enfoque original a la plataforma, nosotros solo sugerimos ideas ;)

Y si no os sale algo... ¡Preguntad!
<h4 align="center">

![](https://camo.githubusercontent.com/abee1b0ea2fb94ffd75986431a093a0f22aeb534a70d11b3fa493f2eda877355/68747470733a2f2f6d656469612e74656e6f722e636f6d2f616556383058443443536741414141642f677569646c696e65732d706972617465732d6f662d7468652d63617269626265616e2e676966)

_El Código es más bien lo que llamarías "directrices" que reglas de verdad._
</h4>

**00 - ¿Qué hay en el cloud?**

Poder ver que nodos pueden crearse en los proveedores cloud
 > Cada proveedor tiene sus máquinas con sus recursos... ¿Podréis recuperarlos automáticamente para poder elegir más adelante la mejor opción?

**01 - Tanto entre lo que elegir...**
A partir de unos recursos, recuperar que posibles nodos pueden crearse en los distintos provedores cloud registrados.
> Si queremos un nodo de X GB de RAM y X núcleos de CPU... ¿Dónde deberíamos desplegarlo? ¿Porqué? ¡Elegid métricas o dadle la responsabilidad al usuario para encontrar la opción óptima!

**02 - El cluster habrá que crear**
Recibir una lista de nodos y crear un cluster 
> ¿Ya sabéis que máquinas queréis crear? ¡Creadlas y configuradlas para que actuen como un cluster! 

**03 - El usuario importa... ¿no?**
Mejorad la experiencia de usuario
> ¿Una herramienta cli por terminal? ¿Una web con formularios? ¿O un chatbot? ¿O quizás una mezcla de cada cosa?

**04 - Todo va bien, muy bien, regular... ¡mal!**
Monitorizar clusters y nodos
> ¿Cuántos recuros quedan en el cluster? ¿Cómo va cada nodo? ¡Intentad recuperar la información y mostrarla al usuario!

**05 - ¿Cloud? ¡Eso es solo el ordenador de otro!**
Dar de alta y baja nodos Edge 
> No todo se reduce al cloud... Podéis conectaros directamente a máquinas virtuales, raspberrys u otros ordenadores vía SSH que pueden actuar como nodos ( cuidado con las limitaciones de red de Eduroam...)


### ¿Qué os damos? 
A los equipos interesados en participar, os dejaremos:
- Una Service Account para poder crear y gestionar máquinas en `Google Cloud` (Cloud Engine)
- Una API Key para poder crear y gestionar máquinas en `Amazon Web Services` (EC2)
- Acceso a una API de LLM para que podáis generar y procesar texto natural 


### ¿Cómo puedo hacer un cluster?
Podéis usar la tecnología que queráis. Si no tenéis miedo a sufrir estas 24h podéis arriesgaros con K8s (Kubernetes), aunque os recomendamos alternativas más _Hackathon Friendly_ cómo [Docker Swarm](https://docs.docker.com/engine/swarm/)... Pero tampoco os preocupeis mucho si no termina de ir el cluster como cluster

### MUY, MUCHO, MUCHÍSIMO IMPORTANTE
Por favor, aseguraros de EXCLUIR las credenciales del repositorio publico de GitHub. Podéis crear un archivo `.gitignore` en la base de vuestro proyecto y añadir:
```.gitignore
**.json
```
Todo aviso muy importante tiene una historia detrás
![](https://i.imgflip.com/aaq9wn.jpg)

## Documentación


## Ganadores 🏅
En esta ocasión, se nombrán dos equipos ganadores:
- **Ganadores:** Un premio al equipo que logre una solución más equilibrada entre calidad, ejecución e idea
- **Jóvenes promesas:** Premio destinado a equipos cuyos miembros no tengan conocimientos previos, que presenten una solución bien ideada y demuestren su capacidad de aprendizaje.
### ¿Qué se valorará? 


### El premio 🤑

- Cheque Amazon por valor de 1000€ para el **primer premio**
- Cheque Amazon por valor de 200€ para el premio de **jóvenes promesas**