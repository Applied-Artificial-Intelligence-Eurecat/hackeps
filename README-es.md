<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

💫  NebulOuS: Tu propio cluster Multi-Cloud-edge ☁️

</h1>

-----

## Índice
  - [El reto 🔎](#el-reto-)
    - [Objetivos](#objetivos)
    - [¿Qué os damos?](#qué-os-damos)
    - [Consideraciones](#consideraciones)
  - [Documentación e información](#documentación-e-información)
    - [Clusters](#clusters)
    - [Google Cloud](#GCP)
    - [Amazon](#AWS)
  - [Ganadores 🏅](#ganadores-)
    - [¿Qué se valorará?](#qué-se-valorará)
    - [El premio 🤑](#el-premio-)

# El reto 🔎

Google Cloud, Amazon Web Services, Microsoft Azure...  grandes proveedores que pueden acabar fallando, y lo hacen (algunos más que otros 😶‍🌫️). Y en ese momento, todo el mundo hubiese deseado no depender de uno solo. 
Por eso, este año os proponemos ayudar a ese pobre diablo que se equivocó confiando solo en uno de ellos, y  creeis una plataforma para crear clusters de máquinas en distintos proveedores 🤙 Desarrollo de Software, IA, DevOPS... en este reto podréis practicar todas las disciplinas para conseguir vuestro objetivo 😎
Además, pensemos en lo local: ¿quién no tiene por casa un servidor de 8 CPU y 16 GB de RAM esperando a ser aprovechado para desplegar cosas?
## Objetivos
El objetivo final puede ser fácil de decir: **una plataforma para creación de clusters-multicloud-edge**, pero lograrlo puede ser algo más abrumador.

Por ello, os sugerimos algunos puntos funcionales, que como decimos todos los años: **NO**, no hace falta que hagáis todos los puntos (es una hackathon), y sois libres darle vuestro propio enfoque original a la plataforma, nosotros solo sugerimos ideas ;) Y si queréis seguir las ideas, tampoco hace falta que las hagáis en este orden... Si algo no os sale, intentad pasar a lo siguiente.

Y sino.. ¡Preguntad!
<h4 align="center">

![](https://camo.githubusercontent.com/abee1b0ea2fb94ffd75986431a093a0f22aeb534a70d11b3fa493f2eda877355/68747470733a2f2f6d656469612e74656e6f722e636f6d2f616556383058443443536741414141642f677569646c696e65732d706972617465732d6f662d7468652d63617269626265616e2e676966)

_El Código es más bien lo que llamarías "directrices" que reglas de verdad._
</h4>

### Gestión de dispositivos
**000 - ¿Hola? ¡Soy yo!**

Conseguir conectar con la API de GCP y AWS a partir de las credenciales que os facilitaremos, e incluso permitir múltiples cuentas registradas.

**001 - ¿Cloud? ¡Eso es solo el ordenador de otro!**

Además del cloud, también es interesante poder contar con dispositivos _edge_, como vuestro propio ordenador (o una VM), raspberries, etc. Tener una lista de estos dispositivos y poder darlos de alta-baja también puede ser interesante. 
Dar de alta y baja nodos Edge 
> Si queréis conectaros por SSH a raspberries u ordenadores de compañeros, a parte de cuidado con los firewalls, usad red desde el movil, ya que Eduroam suele tener la mala costumbre de bloquear conexiones de este tipo.

**010 - ¿Qué hay en el cloud?**

Poder ver que nodos pueden crearse en los proveedores cloud: tipos de máquina, recursos, costes, etc. Además, es interesante poder filtrar o buscar tipos de máquinas que cumplan ciertos requistios de HW y CPU.

### Creación del cluster

**011 - El cluster habrá que crear**

A partir de una necesidad de X máquinas con Y recursos cada máquina, habrá que elegir en que proveedor cloud y que instancias desplegar, o que dispositivos edge utilizar.

> Es totalmente válido permitir al usuario elegir manualmente que instancias utilizar, aunque también podéis intentar elegirlo "automáticamente" a partir de métricas que consideréis vosotros (¿precio? ¿ping? ¿ubicación?)

**100 - ¡EMBUSTERO! Esto no es un cluster**

Una vez elegidos los nodos _edge_ y/o creadas las máquinas cloud, se deberia instalar y configurar (automaticamente) en ellas el software necesario para que actuen como cluster.

> Algunas opciones, de menos a mas complejas, son  Nomad, Docker Swarm, K3s o Kubernetes (pero podéis usar lo que queráis, como si queréis desarrollar algo propio)

### Monitorización y despliegue

**101 - Todo va bien, muy bien, regular... ¡mal!**

Permitir al usuario revisar el estado del/los clusters y el consumo de los recursos de los nodos.

**110 - ¿Y esto de que sirve?**

Permitir al usuario desplegar una aplicación en el cluster.

## ¿Qué os damos? 
A los equipos interesados en participar, os dejaremos:
- Una Service Account para poder crear y gestionar máquinas en `Google Cloud` (Cloud Engine)
- Una API Key para poder crear y gestionar máquinas en `Amazon Web Services` (EC2)
- Acceso a una API de LLM para que podáis generar y procesar texto natural 

## Consideraciones
Queda totalmente prohibido compartir la clave que se os asigne con otros grupos.

Procurad crear todas las máquinas en regiones europeas.

Por seguridad, no se permite crear VMs con gráficas asociadas.

Para evitaros problemas, en Google Cloud Platform, se permite conexion desde fuera desde cualquier IP hacia todos los puertos de las máquinas que creéis.


### MUY, MUCHO, MUCHÍSIMO IMPORTANTE
Por favor, aseguraros de EXCLUIR las credenciales del repositorio publico de GitHub. Podéis crear un archivo `.gitignore` en la base de vuestro proyecto y añadir:
```.gitignore
**.json
```
Todo aviso muy importante tiene una historia detrás

![](https://i.imgflip.com/aaq9wn.jpg)

# Documentación e información
Podéis conectaros a una máquina vía [**SSH**](https://www.cloudflare.com/es-es/learning/access-management/what-is-ssh/). Además de conectaros por "usuario y contraseña", también podéis registrar una clave SSH que podéis generar con:

```sh
ssh-keygen -t rsa -b 4096 -C "username"
```

Esto os da una clave privada (con el nombre que indiquéis) y una pública (el nombre que indiquéis + `.pub`). Al crear un equipo tanto en AWS como en GCP podéis indicarle la clave pública para que podáis conectaros con SSH luego:
```sh
ssh -i <archivo> username@IP-DE-LA-MÁQUINA
```

## Clusters
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

## GCP
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/1280px-Google_Cloud_logo.svg.png" width="300"/>

En Google Cloud Platform podeis utilizar linea de comandos, y necesitareis instalar y configurar [`gcloud`](https://docs.cloud.google.com/sdk/docs/install).
También tenéis librerías específicas para casi cada lenguaje de programacion:
- [Go](https://docs.cloud.google.com/go/docs)
- [JavaScript](https://docs.cloud.google.com/nodejs/docs)
- [Python](https://docs.cloud.google.com/python/docs)
- [Java](https://docs.cloud.google.com/java/docs)
- [C++](https://docs.cloud.google.com/cpp/docs)
- [C#](https://docs.cloud.google.com/dotnet/docs)

Tenéis ejemplos de como usar las librerias en [la cuenta de Google Cloud Platform de Github](https://github.com/GoogleCloudPlatform).
En concreto, el _producto_ que se utiliza es [Compute Engine](https://cloud.google.com/products/compute?hl=es)

Se recomienda que pongáis el idioma de la documentación en inglés, ya que las versiones al castellano son bastante deficientes.

Además, tenéis unos ejemplos ChatGPT made para que podáis probar sin volveros locos en este mismo repositorio, en `examples\google-cloud-platform`. Revisad el README asociado al lenguaje que queráis probar.

- [Python](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/tree/main/examples/google-cloud-platform/python)
- [Java](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/tree/main/examples/google-cloud-platform/java)

## AWS
<img src="https://miro.medium.com/v2/resize:fit:1200/1*neG4D9C8UcJvNn6bverfIA.png" width="300"/>


# Ganadores 🏅
En esta ocasión, se nombrán dos equipos ganadores:
- **Ganadores:** Un premio al equipo que logre una solución más equilibrada entre calidad, ejecución e idea
- **Jóvenes promesas:** Premio destinado a equipos cuyos miembros no tengan conocimientos previos, que presenten una solución bien ideada y demuestren su capacidad de aprendizaje.

### ¿Qué se valorará? 
Se valorará tanto la demo presentada durante la exposición final como toda la información incluida en la publicación de Devpost (recordad que podéis actualizarla incluso después del cierre). A partir de ello evaluaremos, **principalmente**:

**Para el primer premio**
- **Ideas implementadas:** Se tendrá en cuenta el nivel de originalidad, las propuestas que vayan más allá de lo básico, los flujos planteados y cualquier funcionalidad novedosa que resulte útil o práctica.

- **Funcionalidad:** Cómo de bien funciona el proyecto en su conjunto, el estado de cada parte, y la calidad de la integración entre ellas.

- **Arquitectura:** Valoraremos si la arquitectura propuesta tendría sentido en un entorno real, si es escalable y si está bien planteada.

- **Tecnologías:** No importa el lenguaje en sí, sino las tecnologías complementarias usadas: frameworks web (React, Angular, Vue…), bases de datos (Mongo, Postgres, MariaDB…), contenedores (Docker), etc.

- **Calidad del código:** Aun siendo una hackathon, se tendrá en cuenta evitar abusar de hardcoding, mantener unas mínimas buenas prácticas (indentación, tipado en lenguajes no estrictamente tipados, organización del proyecto…).

**Para jóvenes promesas**
- **Ideas implementadas:** Igual que en la categoría general, se valorará la originalidad y la aportación de funcionalidades útiles más allá de lo básico.

- **Aprendizaje:** Si había o no experiencia previa, qué habéis aprendido en estas 24 horas, los principales retos encontrados y cómo los habéis solucionado.

- **Trabajo en equipo:** Cómo os habéis organizado, reparto de tareas y dinámica de colaboración.

- **Calidad del código:** Mismos criterios que en la categoría principal: evitar hardcoding innecesario y mantener un mínimo de orden y coherencia.

- **Presentación de la idea:** Claridad al explicar la propuesta, su enfoque y su objetivo.


## El premio 🤑

- Cheque Amazon por valor de 1000€ para el **primer premio**
- Cheque Amazon por valor de 200€ para el premio de **jóvenes promesas**
