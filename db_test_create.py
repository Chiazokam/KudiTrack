from flask import Flask, render_template
import datetime
import pymongo
from pymongo import MongoClient # Database connector

app = Flask(__name__)

#==============================================================================
#Create and connect to DB
#==============================================================================
client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.testdb    #Creates the database kudiTracker


#==============================================================
if __name__ == '__main__':
    app.run(debug = True)
