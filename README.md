# Disaster Project Pipeline 
This repository is for the project related to the Data Engineering
Module in the Data Scientist Nanodegree course. The README file will be divided as follows: - 
- Motivation behind the Project 
- Repository Breakdown 
- Methodologies 
- Dependencies 
- Obstacles 
- Acknowledgements 
## Motivation behind the Project 
The dataset is obtained from [Figure8](https://appen.com/). The dataset is obtained from tweets originated during crisis. 
The aim of this projects is to analyze the data and come up with an ML model that can predicts the context of the message,
so that during crisis it can be forwarded to the designated party/authority, without wasting valuable time
during such a critical time. 
## Repository Breakdown 
In this section, I'm going to breakdown the content of this repo, so that it'll be easy to follow:
- ### jupyter_notebooks 
  This contains both jupyter notebooks for the the ETL & ML pipelines. It's worth noting that both 
  notebooks are documented 
- ### machine_learning 
  In the **prediction_handler**, resides the code that requests the ML model. 
- ### node_modules
  In **node_modules**, reside all modules downloaded via npm, such as ChartJS (more on that later)
- ### static 
  In **static**, reside all static files, such as html, js, and CSS. 
- ### app.py 
  The start of the execution 
- ### core_db.db 
  The database generated at the end of the ETL pipeline
- ### DisasterResponse.db
  The database downloaded from the jupyter notebook of the project in Udacity
## Methodologies 
The framework Flask was used to accomplish this project. Also, in order to avoid 
reloading of the same page while contacting the ML model, I used Ajax in js, to communicate between
the js file and the python scripts. 
In order to display the charts, I read the data from the database when the page first loads (from Python), then the result is
forwarded to the js file, to be displayed with the help of ChartJs. When the button is pressed, the model is 
used to generate the prediction in a user-friendly manner.
Finally, due to the large size of the model, I uploaded into my Google Drive account. You can check it from [here](https://drive.google.com/drive/folders/1wQcFUY4-M4zaeKu7JQdSHhSpBQK6o0ay?usp=sharing)
## Dependencies 
- Flask Python web framework 
- Ajax
- Chart JS
- HTML, CSS, and JS. 
- Python 
- SQLite 
## Obstacles 
- It's my first time using Flask :) 
- Preparing the model to serve predictions in Flask
## Acknowledgments 
- Special thanks [Tashfeen](https://codepen.io/tashfene). I used his code for the loading effect. 
- Special thanks to Mr. Rajat and all Udacity mentors, who were always available to help us whenever we get stuck.  
 
