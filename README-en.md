<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">English</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

🚀 From 0 to Data Scientist 🔬

</h1>

-----
# The Challenge 👨‍🌾👩‍🌾

This year, we're betting on a much broader problem that includes not only the data scientist aspect of the Applied Artificial Intelligence unit but also requires experimenting in other fields, such as EVERYTHING.

## The Missions 🍅
To familiarize ourselves with plants for when we have to go plant tomatoes, we have founded the Vegetable Department of AAI and defined an execution plan consisting of six missions:

- 🌼 **Daisy Mission**
- 🌷 **Tulip Mission**
- 🎋 **Bamboo Mission**
- 🥦 **Broccoli Mission**
- 🥑 **Avocado Mission**
- 🍑 **Peach Mission**

Except for the `🌼 DAISY MISSION`, these missions are not necessarily sequential: you can carry them out in parallel among colleagues, or jump from one to another as inspired... You can even skip those that don't seem interesting to you and invent others.

Do not hesitate to come to the embassy of the AAI Vegetable Department (known as the tables in the hallway) to validate your ideas if you have any doubts about whether an idea fits within the general idea of the challenge.

### 🌼 DAISY MISSION
Before starting any task, data must be obtained.

In our facilities, we have a first plant sending data to a Eurecat server using the MQTT protocol in real-time. On this server, there is a Mosquitto broker. Request at the Eurecat desk for a username and password to make the connection and listen to the messages transmitted by the plant on the topic `hackeps/eurecat`.

The Vegetable Department needs to be able to store the data in some way for later visualization and analysis.

### 🌷 TULIP MISSION
With the system for storing real-time data ready, request from the AAI Vegetable Department of Eurecat the _Ultimate SensorPlanta Kit 2023_.

This kit contains the necessary materials to connect a new plant to the digital garden and send the plant data to the topic `/hackeps/{id assigned to the team}`.

Send the available data of the new plant to the server and record it along with the rest of the data from the previous plant.

### 🎋 BAMBOO MISSION
Due to some intern's mistake >:(, the data we recorded have some errors, as the sensors were not working correctly. Identify which 2 variables have errors in our dataset! They are likely related. There are two types of reading errors, one associated with a sensor and another associated with two. To not lose all this progress, the gossip and disaster unit saved these data in a dataset data/train.csv. You will find few errors, so it's not necessary to implement any machine learning model. But be careful! In the broccoli mission 🥦, you may find it useful to use these corrected data.

To complete this mission, you must give us the corrected CSV file with the corrected data, so we will have our agronomists happy for future plant monitoring conferences. Leave it in your repository data/<team>-anomaly.csv.

### 🥦 BROCCOLI MISSION

The vegetable department are visionaries, and we want to know what the soil moisture, air humidity, and ambient temperature of our plant will be in the fourteen days following the time horizon of the dataset. This means you must forecast what these data will be like in 14 days! You can use external data to help, but always considering that you will not have these external data after the end of the dataset either. It's not always sunshine and rainbows!

To complete this mission, you must provide us with the CSV file with the soil moisture, air humidity, and ambient temperature in the same date format as the data/train.csv dataset. Leave the CSV in your repository data/<team>-forecast.csv.

### 🥑 AVOCADO MISSION
The obsession with programming worries the Vegetable Department; the plants will die of thirst if this dynamic continues! Since grabbing a watering can and watering them regularly does not seem to be an option, a mini water pump has been provided so you can automate it.

Add the water pump to the system and enable some mechanism to water the plant.

### 🍑 PEACH MISSION
Interacting with data is almost as important as having it. The department of developing attractive interfaces, regular collaborators of the AAI vegetable department, has been subcontracted to devise a way to exploit this data, but they are drier of ideas than a walnut tree in January.

Conceive, design, and develop tools related to the care of the digital garden, which ideally make use of the data collected in any of the other missions.

## How to Start?

### Resources 📦
Initially, you will have access to an MQTT Broker:
> IP: 84.88.76.18
>
> Port: 1883
>
> Username and password: _Come and ask!_

MQTT Topics:
> `hort/plantes`
>
> `hort/team/{Name assigned to the team}`

Once you have advanced in the Daisy mission, you can request the _Ultimate SensorPlanta Kit 2023_ at our table, which will consist of:
|    **ESP3288**    |      **MicroUSB Cable**       |           **Plant**            |
|:----------------: |:-----------------------------:|:-----------------------------: |
|    **Diodes**     |        **Protoboard**         |       **Water Pump**           |
| **Resistors**     | **Voltage Converter**         | **Various Sensors and Cables** |

### Recommendations
We recommend that you use the programming language you are most comfortable with. To program the microcontroller, you can use C, C++, Micro-Python, Lua, or JavaScript. For data visualization, you can use Python, along with [notebooks](https://jupyter.org/).

These are some libraries and tools you might use to carry out the tasks presented in the missions:

For connecting to the MQTT broker:
- [MQTTX](https://mqttx.app/)
- [Eclipse PAHO (MQTT library for many popular languages)](https://eclipse.dev/paho/)

For Microcontroller development:
- [Arduino IDE](https://www.arduino.cc/en/software)
- [ESP8266 Datasheet (Summary)](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/documentation/NodeMCU%20Documentation.pdf)
- [ESP8266 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf)

For data processing:
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [statsmodels](https://www.statsmodels.org/)
- [matplotlib](https://pypi.org/project/matplotlib/)

AI:
- [scikit-learn](https://scikit-learn.org/stable/index.html)
- [xgboost](https://xgboost.readthedocs.io/en/stable/)
- [pytorch](https://pytorch.org/)


## Scoring 👀

We will consider the originality of the solutions and presentation, the percentage of missions completed,
the effectiveness, efficiency, excellence, and success of the solutions, teamwork, communication, and we want to know why you should be the winning team.

### The Prize 🏆
- €800 for the 1st Prize
- €200 for the 2nd Prize

Good luck!
