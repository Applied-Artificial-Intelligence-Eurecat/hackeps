<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🔬 La IA nos dejará sin trabajo y tendremos que plantar tomates y criar gallinas 🌱

</h1>

-----
# El reto 👨‍🌾👩‍🌾
 
Este año, apostamos por un problema mucho más amplio que incluya no solo la parte de data scientist de la unidad de Applied Artificial Intelligence, sino que también requiera experimentar en otros campos, como puede ser TODO.

## Las misiones 🍅
Para familiarizarnos con las plantas para cuando tengamos que ir a plantar tomates, hemos fundado el Departamento Vegetal de AAI y definido un plan de ejecución formado por cinco misiones:

- 🌼 **Misión Margarita**
- 🌷 **Misión Tulipa**
- 🎋 **Misión Bambú**
- 🥑 **Misión Aguacate**
- 🍑 **Misión Melocotón**

Excepto la `🌼 MISIÓN MARGARITA`, estas misiones no son necesariamente secuenciales: podréis hacerlas de manera paralela entre los compañeros, o saltar de una a otra según su inspiración... Incluso podéis no hacer las que no os parezcan interesantes e inventaros otras.

No dudéis en venir a la embajada del Departamento Vegetal de AAI (conocido como las mesas del pasillo) para validar sus ideas si tienen alguna duda sobre si alguna idea encaja dentro de la idea general del reto.

La `🌼 MISIÓN MARGARITA` **ES OBLIGATORIA**.

![](https://media.tenor.com/aeV80XD4CSgAAAAd/guidlines-pirates-of-the-caribbean.gif)

¡Tranquilidad! 🥴 Sabemos que solo hay 24 horas... No valoramos exclusivamente el número de misiones completadas, sino también que aprendáis, la originalidad, y que seáis lo suficientemente analíticos para aportar una solución y un punto de vista a los problemas que surjan.


### 🌼 MISIÓN MARGARITA 
Antes de poder empezar ninguna tarea, hay que obtener datos.

En nuestras instalaciones tenemos una primera planta enviando los datos a un servidor de Eurecat mediante el protocolo MQTT en tiempo real. En este servidor se encuentra un broker Mosquitto. Solicitad en la mesa de Eurecat que les dé un usuario y contraseña para poder hacer la conexión y escuchar los mensajes que transmite la planta en el topic `hackeps/eurecat`

El Departamento Vegetal necesita poder guardar los datos de alguna forma para la posterior visualización y análisis.

### 🌷 MISIÓN TULIPA
Con el sistema para guardar los datos en tiempo real listo, solicitad al Departamento Vegetal de AAI de Eurecat el _Ultimate SensorPlanta Kit 2023_.

Este kit contiene el material necesario para poder conectar una nueva planta al huerto digital y enviar los datos de la planta al topic `/hackeps/{id asignado al equipo}`

Enviad los datos disponibles de la nueva planta al servidor y registradlos junto con el resto de datos de la planta anterior.

### 🎋 MISIÓN BAMBÚ
Por culpa de algún becario >:(, los datos que registramos tienen algunos errores, ya que los sensores no funcionaban correctamente. Para no perder todo este progreso, la unidad de chismes guardó estos datos en un dataset que debería estar disponible en este repositorio.

El Departamento Vegetal quiere solucionar estos errores para poder disponer de este dataset para futuros congresos de monitorizacion de plantas.

### 🥑 MISIÓN AGUACATE
La obsesión por programar preocupa al Departamento Vegetal, ¡las plantas se morirán de sed si continúa esta dinámica! Como coger una regadera y regarlas regularmente no parece ser una opción, se ha entregado una mini bomba de agua para que podáis automatizarlo.

Agreguen la bomba de agua al sistema y habiliten algún mecanismo para regar la planta.

### 🍑 MISIÓN MELOCOTÓN
Interactuar con los datos es casi tan importante como tenerlos. El departamento de desarrollo de interfaces atractivas, colaboradores habituales del departamento vegetal de AAI, ha sido subcontratado para idear una manera de poder explotar estos datos, pero están más secos de ideas que un nogal en enero.

Idead, diseñad y desarrollad herramientas relacionadas con el cuidado del huerto digital, que idealmente hagan uso de los datos recogidos en cualquiera de las otras misiones.


## ¿Cómo comenzar?

### Recursos 📦
Inicialmente tendréis acceso a un Broker MQTT:
> IP: 84.88.76.18
>
> Puerto: 1883
>
> Usuario y contraseña: _¡Venid a preguntar!_

Temas MQTT:
> `hort/plantes`
>
> `hort/team/{Nombre asignado al equipo}`

Una vez avanzada la misión Margarita, podrán solicitar el _Ultimate SensorPlanta Kit 2023_ en nuestra mesa, que constará de:
|    **ESP3288**   	|      **Cable MicroUSB**     	|           **Planta**          	|
|:----------------:	|:---------------------------:	|:-----------------------------:	|
|    **Díodos**    	|        **Protoboard**       	|       **Bomba de agua**       	|
| **Resistencias** 	| **Convertidor de Voltaje** 	| **Varios sensores y cables** 	|

### Recomendaciones
Les recomendamos que utilicen el lenguaje de programación con el que se sientan más cómodos. Para programar el microcontrolador, pueden usar C, C++, Micro-Python, Lua o JavaScript. Para la visualización de datos, pueden utilizar Python, junto con el uso de [notebooks](https://jupyter.org/).

Estas son algunas bibliotecas (**LIBRARY != LLIBRERIA**) y herramientas que podrían utilizar para llevar a cabo las tareas que se presentan en las misiones:

Para la conexión al broker MQTT:
- [MQTTX](https://mqttx.app/)
- [Eclipse PAHO (biblioteca MQTT para muchos lenguajes populares)](https://eclipse.dev/paho/)

Para el desarrollo del Microcontrolador:
- [Arduino IDE](https://www.arduino.cc/en/software)
- [ESP8266 Datasheet (Resumen)](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/documentation/NodeMCU%20Documentation.pdf)
- [ESP8266 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf) 

Para el procesamiento de datos:
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [statsmodels](https://www.statsmodels.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [matplotlib](https://pypi.org/project/matplotlib/)

## La puntuación 👀

Tomaremos en cuenta la originalidad de las soluciones y de la presentación, el porcentaje de misiones completadas,
la eficacia, la eficiencia, la excelencia y el éxito en las soluciones, el trabajo en equipo, la comunicación y queremos saber por qué deberían ser el equipo ganador.

### El premio 🏆
- 800€ para el 1er Premio
- 200€ para el 2do Premio 

¡Buena suerte!
