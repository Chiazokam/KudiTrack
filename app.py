from flask import Flask, render_template
import datetime
import pymongo
from pymongo import MongoClient # Database connector

app = Flask(__name__)

#Create and connect to DB
client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.kuditracker    #Select the database
collection = db.kuditracker_coll #Select the collection

expense = {
           "date": datetime.datetime.now(),
           "Description": "For vehicle purchase",
           "amount": "N5000000",
           "category": "Personal"
           }

db.collection.insert_one(expense)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/business")
def business():
    return render_template("business.html")

@app.route("/personal")
def personal():
    return render_template("personal.html")

#==============================================================
if __name__ == '__main__':
    app.run(debug = True)
