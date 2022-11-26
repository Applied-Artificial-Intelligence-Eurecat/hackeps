<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🚀 From 0 to Data Scientist 🔬

</h1>

-----

## El repte 👨‍🔬👩‍🔬

Volem que sentiu i aprengueu què pot fer un Investigador a la unitat de Applied Artificial Intelligence en el seu dia a
dia. 💼 Per aquest motiu, us proposem resoldre unes quantes missions que tenen relació en el món de la ciència de les
dades 🔎, més concretament volem que treballeu amb imatges! 🖼️

Cada missió 🚀 té una certa dificultat però, no patiu! 🥴 Sabem que només teniu 24 h... L'important no és resoldre-les
totes sinó aprendre del repte i ser capaços de ser suficientment analítics per aportar una solució i un punt de vista
als problemes plantejats. Si en algun moment veieu que no us surt una missió podeu passar a la següent o... podeu crear
les vostres pròpies missions relacionades amb el tema! ✨

Aquí teniu uns quants exemples:

* Eina de labelling per poder etiquetar imatges.
* Una plataforma per poder fer anàlisis de les imatges i determinar patrons, errors...
* ....

D'aquesta manera, podeu vincular aquest repte juntament amb altres reptes que us proposin. 😄

## Les missions 🎨

Com que estem parlant d'imatges, hem relacionat cada missió amb un color 🎨 Com ja hem mencionat anteriorment, cada
missió té una dificultat diferent. A més a més, cada missió requereix com a mínim utilitzar uns recursos, així que,
estigueu atents!

### Com començar?

Us recomanem que vingueu a les xerrades que fan els ex-LleidaHackers encara que no participeu al nostre repte. Us
recomanem python com a llenguatge de programació i fer l'ús de [notebooks](https://jupyter.org/) per visualitzar les
dades. Aquestes són les llibreries que us recomanem per tractar les dades:

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [matplotlib](https://pypi.org/project/matplotlib/)

Coneixements de Machine Learning (ML) i Deep Learning (DL) seran útils en les últimes missions. Us deixem aquí unes
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

Comptareu amb uns quants datasets, **A1**, **A2**, **A3** i  **B**. Encara que les imatges dels datasets estàn
relacionades, veureu que tenen diferents característiques que comportarà un canvi de dificultat a l'hora de complir les
misisons. Us podeu començar a descarregar els datasets
per [aquí](https://eurecatcloud-my.sharepoint.com/:f:/g/personal/oriol_alas_eurecat_org/EuSA9ovRMklJidz69WmJpgwBQ2d1A-eddvg7EUukUTpnQA?e=D39Ppz)
o podeu demanar un USB amb les dades a Paula Gallucci 👩‍🔬 o Oriol Alàs 👨‍🔬.

En el cas que feu models de Deep Learning, entenem que els recursos a una hackathon són més aviat limitats. Igualment,
compteu amb recursos gratuïts com les [notebooks de Kaggle](https://www.kaggle.com/docs/notebooks)
, [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
o [Gradient](https://medium.com/@krantirk/run-deep-learning-notebooks-on-free-gpus-798eb0d71d65); la majoria incorporen
un servei gratuït de GPUs.

### ☀️ Missió groga

La idea d'aquesta missió es orientar-la amb l'etiquetatge de dades. Part de la feina d'un data scientist és tenir dades
amb la major informació possible per detectar patrons, problemes, estadístiques... Amb el dataset **A1**, volem que
observeu les teles i realitzeu un algoritme per etiquetar les dades que teniu segons el patró 📁 que segueixen. Totes
les teles que teniu a continuació tenen un patró diferent:

<img src="imgs\A\c1r1e0n1.png" height="100px"/><img src="imgs\A\c1r3e0n1.png" height="100px"/><img src="imgs\A\c2r3e0n1.png" height="100px"/><img src="imgs\A\c3r1e0n1.png" height="100px"/><img src="imgs\A\c3r3e0n1.png" height="100px"/>

Què ens heu de donar? Un **document** (en Markdown, pdf, docx...) enumerant els diferents tipus de tela i un  **csv**
amb el nom del fitxer de la imatge i el tipus de patró en qüestió.

### 🍓 Missió vermella

La idea d'aquesta missió es orientar-la amb l'etiquetatge de dades. Part de la feina d'un data scientist és tenir dades
amb la major informació possible per detectar patrons, problemes, estadístiques... Amb el dataset **A1** volem que
observeu les teles i realitzeu un algoritme per etiquetar les dades segons l'error. Podeu fer servir el *.csv* que hi ha
dins de la carpeta, on trobareu una categoria que explica amb llenguatge natural una mica quin error és. Es voldrà
obviar si l'error de l'imatge és a causa de la càmara, és a dir, no es tindran en compte aquestes imatges.

Aquí teniu alguns exemples d'errors:

<img src="imgs\BAD\A\c1r1e2n3.png" height="100px"/><img src="imgs\BAD\A\c1r1e4n1.png" height="100px"/><img src="imgs\BAD\A\c1r3e3n4.png" height="100px"/><img src="imgs\BAD\A\c2r2e2n1.png" height="100px"/>

Guanyarà l'algoritme que més imatges pugui etiquetar correctament.

Voldrem classificar els errors de la següent manera:

- Forats
- Marques verticals
- Marques horitzontals
- Taques d'oli
- Plegaments
- Franja de colors
- Altres irregularitats

Què ens heu de donar? Un **document** (en Markdown, pdf, docx...) enumerant els diferents errors i un  **csv**
amb el nom del fitxer de la imatge i el tipus d'error en qüestió.

### 🍊 Missió taronja

Volem que implementeu un model o algoritme que permeti classificar del dataset **A2** si aquella imatge hi ha error o
no. Ens agradaria que mostressiu alguna gràfica de l'entrenament del model (en cas de fer ML) o mètriques qualitatives (
accuracy, recall, f1...) i quantitatives (matrius de confusió, ROC curve...).

### 🍆 Missió lila

Volem que implementeu un model o algoritme que permeti classificar els patrons detectats de la missió groga ️☀️ en el
dataset **A1**. Ens agradaria que mostressiu alguna gràfica de l'entrenament del model (en cas de fer ML) o mètriques
qualitatives (accuracy, recall, f1...) i quantitatives (matrius de confusió, ROC curve...).

### 🍏 Missió verda

Volem que implementeu un model o algoritme que permeti classificar els errors del dataset **B**. Ens agradaria que
mostressiu alguna gràfica de l'entrenament del model (en cas de fer ML) o mètriques qualitatives (accuracy, recall,
f1...) i quantitatives (matrius de confusió, ROC curve...).

### 🏴 Missió negra

Està popularitzat dir que no sabem el comportament de les xarxes neuronals... És això cert? Apliqueu tècniques de
*eXplainable Artificial Intelligence* a un model que teniu [aquí](http://84.88.176.103:10003/docs)... Utilitzeu imatges
del dataset **B**. Amb 2 o 3 imatges explicant el que passa en tenim suficient 👌

Us deixem aquí uns recursos 📦 que de segur us seran ben útils!

- [SHAP](https://shap.readthedocs.io/en/latest/index.html)
- [Captum](https://captum.ai/)
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)

### 🌺 Missió rosa

Ostres! Les nostres càmares estàn fallant molt últimament i no rebem bé les imatges. Podriem reparar les imatges i
tornar a tenir-les lo més semblant al que esperem? Per provar el vostre model generatiu, us hem deixat el dataset **A3**
, no obstant això, pel seu entrenament podeu utilitzar els altres datasets.

<img src="imgs\generative.PNG" height="300px"/>

No saps quins models podrien anar bé? Vine a preguntar-nos!

## La puntuació 👀

Tindrem en compte l'originalitat de les sol·lucions i de la presentació, el percentatge de missions complertes,
l'eficàcia, l'eficiència, l'excelència i l'èxit en les sol·lucions, el treball en equip, la comunicació i volem saber el
per què heu de ser l'equip guanyador.

Molta sort!
