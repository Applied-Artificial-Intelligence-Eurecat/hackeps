<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🚀 From 0 to Data Scientist 🔬

</h1>

-----

## El reto 👨‍🔬👩‍🔬

Queremos que experimentéis qué puede hacer un Investigador en la unidad de Applied Artificial Intelligence en su día en
día. 💼 Por este motivo, proponemos resolver unas cuantas misiones que tienen relación en el mundo de la ciencia de los
datos 🔎, más concretamente queremos que trabajéis con imágenes! 🖼️

Cada misión 🚀 tiene una cierta dificultad sin embargo, no padezcáis! 🥴 Sabemos que sólo tenéis 24 h... Lo importante
no es resolverlas todas las misiones sinó aprender del reto y ser capaces de ser suficientemente analíticos para aportar
una solución y un punto de vista a los problemas planteados. Si en algún momento veis que no os sale una misión podéis
pasar a la siguiente o... podéis crear vuestras propias misiones relacionadas con el tema! ✨

Aquí tenéis algunos ejemplos:

* Herramienta de labelling para poder etiquetar imágenes.
* Una plataforma para poder hacer análisis de las imágenes y determinar patrones, errores...
* ....

De esta forma, podéis vincular este reto junto con otros retos que os propongan. 😄

## Las misiones 🎨

Puesto que estamos hablando de imágenes, hemos relacionado cada misión con un color 🎨 Como ya hemos mencionado
anteriormente, cada misión tiene una dificultad distinta. Además, cada misión requiere al menos utilizar unos recursos,
así que, ¡esté atentos!

### ¿Cómo empezar?

Os recomendamos que vengáis a las charlas que hacen los ex-LleidaHackers aunque no participéis en nuestro reto. Os
recomendamos python como lenguaje de programación y hacer uso de [notebooks](https://jupyter.org/) para visualizar las
datos. Estas son las librerías que le recomendamos para tratar los datos:

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [matplotlib](https://pypi.org/project/matplotlib/)

Conocimientos de Machine Learning (ML) y Deep Learning (DL) serán útiles en las últimas misiones. Os dejamos aquí unas
librerías.

- [scikit-learn](https://scikit-learn.org/stable/install.html)
- [tensorflow](https://www.tensorflow.org/)
- [pytorch](https://pytorch.org/)

En cuanto a la visualización de los modelos:

- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://seaborn.pydata.org/)
- [plotly](https://plotly.com/)
- [tensorboard](https://www.tensorflow.org/tensorboard)
- [streamlit](https://streamlit.io/)

### Recursos 📦

Tendrás a tu disposición algunos datasets, **A1**, **A2**, **A3** y **B**. Aunque las imágenes de los conjuntos de datos
están relacionadas, verás que tienen diferentes características que darán lugar a un cambio de dificultad a la hora de
cumplir las misiones. Puedes comenzar a descargar los conjuntos de datos [aquí](README.md) o puedes solicitar un USB con
los datos a Paula Gallucci 👩‍🔬 o Oriol Alàs 👨‍🔬.

En caso de que utilices modelos de aprendizaje profundo, entendemos que los recursos en un hackatón son bastante
limitados. Sin embargo, puedes contar con recursos gratuitos
como [cuadernos Kaggle](https://www.kaggle.com/docs/notebooks)
, [Google Colaborador](https://colab.research.google.com/notebooks/intro.ipynb)
o [Gradiente](https://medium.com/@krantirk/run-deep-learning-notebooks-on-free-gpus-798eb0d71d65); la mayoría incorpora
un Servicio gratuito de GPU.

### ☀️ Misión amarilla

La idea de esta misión es etiquetar los datos. Parte del trabajo de un científico de datos es tener datos con tanta
información posible para detectar patrones, problemas, estadísticas... Con el conjunto de datos **A1**, queremos que
observes los tejidos y realizes un algoritmo para etiquetar los datos que tienes según el patrón 📁 que sigue. Todas las
telas que tienes abajo tienen un patrón diferente:

<img src="imgs\A\c1r1e0n1.png" height="100px"/><img src="imgs\A\c1r3e0n1.png" height="100px"/><img src="imgs\A\c2r3e0n1 .png" altura="100px"/><img src="imgs\A\c3r1e0n1.png" altura="100px"/><img src="imgs\A\c3r3e0n1.png" altura="100px"/>

¿Qué tienes para darnos? Un **documento** (en Markdown, pdf, docx...) enumerando los diferentes tipos de tejido y un
**CSV** con el nombre del archivo de la imagen y el tipo de patrón en cuestión.

### 🍓 Misión roja

La idea de esta misión es etiquetar los datos. Parte del trabajo de un científico de datos es tener datos con tanta
información posible para detectar patrones, problemas, estadísticas... Con el conjunto de datos **A1** queremos que
observes los tejidos y realizar un algoritmo para etiquetar los datos de acuerdo con el error. Puedes usar el *.csv* que
está dentro de la carpeta, donde encontrarás una categoria que explica en lenguaje natural un poco cual es el error. Se
querrá ignorar si el error de imagen se debe a la cámara, es decir, estas imágenes no serán consideradas.

Estos son algunos ejemplos de errores:

<img src="imgs\BAD\A\c1r1e2n3.png" height="100px"/><img src="imgs\BAD\A\c1r1e4n1.png" height="100px"/><img src="imgs \BAD\A\c1r3e3n4.png" height="100px"/><img src="imgs\BAD\A\c2r2e2n1.png" height="100px"/>

Ganará el algoritmo que pueda etiquetar correctamente la mayor cantidad de imágenes.

Nos gustaría clasificar los errores de la siguiente manera:

- Agujeros
- Marcas verticales
- Marcas horizontales
- Manchas de aceite
- Pliegues
- Tira de color
- Otras irregularidades

¿Qué tienes para darnos? Un **documento** (en Markdown, pdf, docx...) enumerando los diferentes errores y un **csv**
con el nombre del archivo de imagen y el tipo de error en cuestión.

### 🍊 Misión naranja

Queremos que implementes un modelo o algoritmo que te permita clasificar el conjunto de datos **A2** si esa imagen tiene
un error o no. Nos gustaría que mostraras algún gráfico del entrenamiento del modelo (si estás haciendo ML) o métricas
cualitativas (
precisión, recuperación, f1...) y cuantitativos (matrices de confusión, curva ROC...).

### 🍆 Misión morada

Queremos que implementes un modelo o algoritmo que permita clasificar los patrones detectados de la misión amarilla ️☀️ en el
conjunto de datos **A1**. Nos gustaría que muestre algunos gráficos del entrenamiento del modelo (si está haciendo ML) o métricas
cualitativos (precisión, recuperación, f1...) y cuantitativos (matrices de confusión, curva ROC...).

### 🍏 Misión verde

Queremos que implementes un modelo o algoritmo que permita clasificar los errores del conjunto de datos **B**. nos gustaria eso
mostrar algún gráfico del entrenamiento del modelo (en caso de hacer ML) o métricas cualitativas (precisión, recuperación,
f1...) y cuantitativos (matrices de confusión, curva ROC...).

### 🏴 Misión negra

Es popular decir que no conocemos el comportamiento de las redes neuronales... ¿Es esto cierto? Aplica técnicas de
*Inteligencia artificial explicable* a un modelo que hemos subido al Sharepoint... Utiliza imágenes del conjunto de datos **B**.
Con 2 o 3 imágenes explicando lo que pasa ya tenemos suficiente 👌

¡Aquí tienes algunos recursos 📦 que seguro te serán de mucha utilidad!

- [SHAP](https://shap.readthedocs.io/en/latest/index.html)
- [Captum](https://captum.ai/)
- [Aprendizaje automático interpretable](https://christophm.github.io/interpretable-ml-book/)

### 🌺 Misión rosa

¡DIOS MÍO! Nuestras cámaras están fallando mucho últimamente y no estamos sacando las fotos bien. Podríamos reparar las imágenes y
volver a tenerlos lo más parecido a lo que esperamos? Para probar tu modelo generativo, te hemos dejado el dataset **A3**
, sin embargo, para el entrenamiento puede usar los otros conjuntos de datos.

<img src="imgs\generativo.PNG" height="300px"/>

¿No sabes qué modelos podrían ir bien? ¡Ven y pregúntanos!

## La puntuación 👀

Tendremos en cuenta la originalidad de las soluciones y la presentación, el porcentaje de misiones completadas,
eficacia, eficiencia, excelencia y éxito en las soluciones, trabajo en equipo, comunicación y queremos conocer las
por qué usted debe ser el equipo ganador.

¡Buena suerte!