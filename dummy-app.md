**DUMMY APP**

Os traemos una aplicación de pruebas que puede ser muy útil en vuestra travesía por el cloud-edge continuum! 

<img width="1900" height="923" alt="image" src="https://github.com/user-attachments/assets/a04c8577-d7e4-4f93-8dff-3c61507ef745" />


Esta aplicación consta de un controlador que recibesolicitudes de “work” y de un número variable de workers que procesan dichassolicitudes.

**Controller**

El _controller_ es un componente que ofrece una APIREST con un único endpoint:

*   **POST /** Recibe un parámetro en la URL, **t**, que debe ser un número entero positivo. Cuando se invoca este endpoint, el controlador añade una nueva solicitud a la cola de peticiones pendientes.
    

El componente también publica periódicamente en el EMS laantigüedad, en segundos, de la petición más antigua de la cola (métrica **max\_age**).

Además, el controlador ofrece una API REST interna destinadaa ser consumida por el componente _worker_. Esta API incluye:

*   **POST /accept** Extrae el primer elemento de la lista de solicitudes pendientes (la más antigua) y lo devuelve como respuesta. Si la lista está vacía, devuelve _null_.
    

*   **GET /** Devuelve la lista de solicitudes pendientes y su antigüedad en segundos.
    

El controlador también incorpora una **interfaz gráfica(UI)** disponible en el puerto **8000** dentro de la red Docker y en elpuerto **30008** desde el exterior.La UI permite visualizar detalles de las solicitudes en cola, los workersconectados y las solicitudes completadas.Mediante los botones de la parte superior, es posible enviar nuevas solicitudessin necesidad de utilizar directamente la API.

**Worker**

El _worker_ es un componente que, al iniciarse:

2.  Llama al endpoint **POST /accept** del _controller_.
    

4.  Si la respuesta contiene un valor numérico, el _worker_ duerme durante el número de segundos especificado.
    

Aquí tenéis el Docker-compose:

```
version: "3.9"

services:
  dummy-app-controller:
    image: rsprat/dummy-rest-app-controller:v1
    ports:
      - "30008:8000"
    environment:
      report_metrics_to_ems: "False"
    deploy:
      replicas: 1
      resources:
        limits:
          cpus: "1.0"
          memory: "1024M"

  dummy-app-worker:
    image: rsprat/dummy-rest-app-worker:v1
    environment:
      API_ADDRESS: "http://dummy-app-controller:8000"
    depends_on:
      - dummy-app-controller
    deploy:
      replicas: 1
      resources:
        limits:
          cpus: "1.0"
          memory: "1024M"

```


Algunos detalles importantes:

*   En el _controller_ se especifica el **puerto externo** que se expone al host. El puerto interno es fijo y **no debe modificarse**.
    

*   En el _worker_ se indica la **URL a través de la cual puede localizar al controller**, de modo que los workers sepan dónde enviar sus solicitudes.
    

Esta aplicación puede serviros como un ejemplo práctico deuna arquitectura **distribuida y escalable**, perfectamente adecuada paraser desplegada con vuestro sistema.

¿Quién será el primero en desplegar la aplicación en **dosmáquinas virtuales**?Un _controller_ en una VM y uno o varios _workers_ en otra… ¡oincluso en varias!
