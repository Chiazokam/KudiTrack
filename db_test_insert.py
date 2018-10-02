from flask import Flask, render_template
import datetime
#import pymongo
from pymongo import MongoClient # Database connector

app = Flask(__name__)

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.testdb    #Creates the database kudiTracker
#==============================================================================
#Insert Test Data
#==============================================================================
expense = {
           "Date": datetime.datetime.now().strftime('%m/%d/%Y'),
           "Description": "For children's fees",
           "Amount(NGN)": 500000,
           "Category": "Personal"
           }

#expenses serves as the Collection
db.expenses.insert_one(expense)
#db.expenses.remove({})

#==============================================================
if __name__ == '__main__':
    app.run(debug = True)
