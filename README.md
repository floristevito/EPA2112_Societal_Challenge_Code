Created by students from the TU Delft in regard to the EPA Master course EPA2112 Social Challenge Project:
|Authors|
|----|
|Floris Boendermaker|
|Bruno Hermans|
|Bram Boereboom|
|Hidde Bijaard|
|Jonathan Ambrose|

# Background
The aim of this project is to gain input from The Hague's citizens. The main idea is, that posters with unique QR codes can be scanned by citizens. If citizens do this, they will land on a webapp that has some questions about the location of the qr-code poster. 

# Contents
This repository contains all code of the webapp, as well as code that is needed to generate a large batch of all the posters. Besides, it also includes some exploratory data analysis of the city of The Hague. The webapp is located in the app folder, the rest is located elsewhere. The qr code generating scripts are also in the app folder. One can find them inside the server folder, which has a directory called 'qr'. 

The web app is hosted at the following URL:
https://challenges.social/#/
# How to run
One can run this application by using docker. Docker boots both the frontend and backend. 
To run the app, cd into the apropiate folder (app). Afterwards, run the following command:

`docker compose up --build`
