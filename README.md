# KudiTracker

[![Build Status](https://travis-ci.org/Chiazokam/KudiTracker.svg?branch=master)](https://travis-ci.org/Chiazokam/KudiTracker)

### Link to trello project: https://trello.com/b/WJZERcNZ/kuditracker-project
KudiTracker is an expense tracker that helps the user to keep track of his daily expenses.

The following data are provided by the user:


a. The date of the expense

b. The description of the expense

c. The amount

d. Category of expense - Business or Personal

On submission, data are stored in the database and can be retrieved at any time based on categories.



## Getting Started With KudiTracker


a. Create a folder on your local machine and clone repo into it.
   This folder will act as the root folder for your virtual environment

b. Set up MariaDB on your local machine and keep it running in the background.

(Follow instructions in https://mariadb.com/kb/en/library/installing-mariadb-msi-packages-on-windows/ and

   https://mariadb.com/kb/en/library/a-mariadb-primer/ to set up mariaDB if not installed on your local machine)

c. From your command line, set up a virtual environment in the root folder and activate it.
  Check out https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/

  for how to set up a virtual environment.


Install the following in your virtual environment:
	i. Flask (pip install flask)
	ii. mysql-connector (pip install mysql-connector)
  iii. wtforms (pip install wtforms)

d. Move into the folder that was cloned

      i. cd into Flask_Maria and run the db_create.py file

        > python db_create.py

      ii. Go back to the parent folder and run the main_app.py file

        > python main_app.py

e. On your browser, go to:
    http://localhost:5000/

... and you have KudiTracker running!


## Getting Started with the Hello World App

a. Create a folder on your local machine

b. Run:

  git clone -b helloflask https://github.com/Chiazokam/KudiTracker

in the created folder.

c. Follow the instructions above to set up a virtual environment on your system

d. Follow instructions above to install flask in the app folder

e. On your browser, go to:
    http://localhost:5000/

...and the hello world app is set to run


## Wireframes
Home Page:

![](https://user-images.githubusercontent.com/26940294/46139831-766b2500-c247-11e8-96f5-e0b07c9414d4.png)

Personal Page:

![](https://user-images.githubusercontent.com/26940294/46139832-7703bb80-c247-11e8-89fb-480ab9a039f1.PNG)

Business Page:

![](https://user-images.githubusercontent.com/26940294/46139827-7539f800-c247-11e8-85df-9a74cb96999c.PNG)


### Technologies and Frameworks Used
i. Python/ flask

ii. mongodb

iii. Travis CI/ Unittesting

iv. HTML/ CSS

v. Semantic UI















#How to run the automated tests\
#Include link to Travis build
