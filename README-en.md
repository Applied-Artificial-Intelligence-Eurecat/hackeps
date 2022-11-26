<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">English</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🚀 From 0 to Data Scientist 🔬

</h1>

-----

## The challenge 👨‍🔬👩‍🔬

We want you to experience what a Researcher can do in the Applied Artificial Intelligence unit in his day in day. 💼 For
this reason, we propose to solve a few missions that are related to the world of science of the data 🔎, more
specifically we want you to work with images! 🖼️

Each mission 🚀 has a certain difficulty however, don't suffer! 🥴 We know you only have 24 hours... The important thing
It is not solving all the missions, but learning from the challenge and being able to be analytical enough to contribute
a solution and a point of view to the problems raised. If at any time you see that you do not get a mission you can skip
to the next or... you can create your own quests related to the theme! ✨

Here are some examples:

* Labeling tool to be able to label images.
* A platform to analyze the images and determine patterns, errors...
* ....

In this way, you can link this challenge together with other challenges that are proposed to you. 😄

## The missions 🎨

Since we are talking about images, we have related each mission with a color 🎨 As we have already mentioned above, each
mission has a different difficulty. In addition, each mission requires at least some resources to be used, so stay
tuned!

### How to start?

We recommend that you come to the talks given by the ex-LleidaHackers even if you don't participate in our challenge.
You we recommend python as a programming language and use [notebooks](https://jupyter.org/) to view the data. These are
the libraries that we recommend to process the data:

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [matplotlib](https://pypi.org/project/matplotlib/)

Knowledge of Machine Learning (ML) and Deep Learning (DL) will be useful in the last missions. We enumerate here some
libraries.

- [scikit-learn](https://scikit-learn.org/stable/install.html)
- [tensorflow](https://www.tensorflow.org/)
- [pytorch](https://pytorch.org/)

Regarding the display of the models:

- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://seaborn.pydata.org/)
- [plotly](https://plotly.com/)
- [tensorboard](https://www.tensorflow.org/tensorboard)
- [streamlit](https://streamlit.io/)

### Resources 📦

You will have a few datasets, **A1**, **A2**, **A3** and **B**. Although the images of the datasets are related, you
will see that they have different characteristics that will lead to a change in difficulty when fulfilling them missions
You can start downloading the datasets
by [here](https://eurecatcloud-my.sharepoint.com/:f:/g/personal/oriol_alas_eurecat_org/EuSA9ovRMklJidz69WmJpgwBQ2d1A-eddvg7EUukUTpnQA?e=D39Ppz)
or you can ask for a USB with the data to Paula Gallucci 👩‍🔬 or Oriol Alàs 👨‍🔬.

In case you use Deep Learning models, we understand that resources at a hackathon are rather limited. However, you can
count on free resources like [Kaggle notebooks](https://www.kaggle.com/docs/notebooks)
, [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
or [Gradient](https://medium.com/@krantirk/run-deep-learning-notebooks-on-free-gpus-798eb0d71d65); most incorporate a
free GPU service.

### ☀️ Yellow mission

The idea of this mission is to label the data. Part of a data scientist's job is to have data with as much information
as possible to detect patterns, problems, statistics... With the **A1** dataset, we want you to look at the fabrics and
perform an algorithm to label the data you have according to the pattern 📁 that follows. All the fabrics you have below
have a different pattern:

<img src="imgs\A\c1r1e0n1.png" height="100px"/><img src="imgs\A\c1r3e0n1.png" height="100px"/><img src="imgs\A\c2r3e0n1 .png" height="100px"/><img src="imgs\A\c3r1e0n1.png" height="100px"/><img src="imgs\A\c3r3e0n1.png" height="100px"/>

What do you have to give us? A **document** (in Markdown, pdf, docx...) listing the different types of fabric and a **
csv**
with the file name of the image and the type of pattern in question.

### 🍓 Red mission

The idea of this mission is to label the data. Part of a data scientist's job is to have data with as much information
as possible to detect patterns, problems, statistics... With dataset **A1** we want you to observe the fabrics and
perform an algorithm to label the data according to the error. You can use the *.csv* that is there inside the folder,
where you will find a category that explains in natural language a little what the error is. will be wanted ignore if
the image error is due to the camera, i.e. these images will not be considered.

Here are some examples of errors:

<img src="imgs\BAD\A\c1r1e2n3.png" height="100px"/><img src="imgs\BAD\A\c1r1e4n1.png" height="100px"/><img src="imgs \BAD\A\c1r3e3n4.png" height="100px"/><img src="imgs\BAD\A\c2r2e2n1.png" height="100px"/>

The algorithm that can correctly label the most images will win.

We would like to classify the errors as follows:

- Holes
- Vertical marks
- Horizontal marks
- Oil stains
- Folds
- Color strip
- Other irregularities

What do you have to give us? A **document** (in Markdown, pdf, docx...) listing the different errors and a **csv**
with the name of the image file and the type of error in question.

### 🍊 Orange mission

We want you to implement a model or algorithm that allows you to classify the **A2** dataset if that image has an error
or no. We would like you to show some graph of the model training (if doing ML) or qualitative metrics (
accuracy, recall, f1...) and quantitative (confusion matrices, ROC curve...).

### 🍆 Purple mission

We want you to implement a model or algorithm that allows to classify the detected patterns of the yellow mission ️☀️ in
the dataset **A1**. We would like you to show some graphs of the model training (if doing ML) or metrics qualitative (
accuracy, recall, f1...) and quantitative (confusion matrices, ROC curve...).

### 🍏 Green mission

We want you to implement a model or algorithm that allows to classify the errors of dataset **B**. We would like that
show some graph of the model training (in case of doing ML) or qualitative metrics (accuracy, recall, f1...) and
quantitative (confusion matrices, ROC curve...).

### 🏴 Black mission

It is popular to say that we do not know the behavior of neural networks... Is this true? Apply techniques of
*eXplainable Artificial Intelligence* to a model you have [here](http://84.88.176.103:10003/docs)... Use images from
dataset **B**. With 2 or 3 images explaining what happens we have enough 👌

Here are some resources 📦 that will surely be very useful!

- [SHAP](https://shap.readthedocs.io/en/latest/index.html)
- [Captum](https://captum.ai/)
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)

### 🌺 Pink mission

OMG! Our cameras are failing a lot lately and we're not getting the pictures right. We could repair the images and
return to have them the closest to what we expect? To test your generative model, we have left you the dataset **A3**
, however, for training you can use the other datasets.

<img src="imgs\generative.PNG" height="300px"/>

Don't know which models might go well? Come and ask us!

## The score 👀

We will take into account the originality of the solutions and the presentation, the percentage of missions completed,
effectiveness, efficiency, excellence and success in solutions, teamwork, communication and we want to know the why you
must be the winning team.

Good Luck!