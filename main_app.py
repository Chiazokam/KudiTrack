from flask import Flask, render_template, url_for, flash, redirect, session, logging, request
from wtforms import Form, validators, StringField, TextAreaField, DateField, IntegerField, SelectField, SubmitField
import mysql.connector as mariadb
from datetime import datetime
import pymysql  #Downloaded and imported

app = Flask(__name__)

#==============================================================================
#Define the Form class
class ExpenseForm(Form):
    expense_date = DateField('Date: dd-mm-yyyy', [validators.DataRequired()])
    expense_descr = StringField('Description', [validators.Length(min=4, max=68)])
    expense_amt = IntegerField('Amount', [validators.DataRequired()])
    expense_cat = StringField('Category: Business Or Personal', [validators.DataRequired()])

def date_format(date_string):
    """Function to return date object"""
    return datetime.strptime(date_string, "%d-%m-%Y").date()

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ExpenseForm(request.form)
    #Triggered if form is filled and submitted
    if request.method == 'POST':
        expense_date = date_format(request.form['expense_date'])
        #Escape characters that may cause an error when inserted into the db e.g, apostrophe
        expense_descr =  pymysql.escape_string(request.form['expense_descr'])
        expense_amt = request.form['expense_amt']
        expense_cat = request.form['expense_cat']

        #Connect to mariaDB
        db_conn = mariadb.connect(user='root',
                                  password='root',
                                  database='kuditracker')
        cursor = db_conn.cursor()
        #Insert data into the db
        query = "INSERT INTO expenses (ExpenseDate, Description, Amount, Category) VALUES ('{}', '{}', '{}', '{}')".format(expense_date, expense_descr, expense_amt, expense_cat)
        cursor.execute(query)
        db_conn.commit()
        #Close connection
        cursor.close()
        return redirect(url_for("home"))    #Putting return, the form data was cleared from the form after submission
    #Default page to render without the form filling
    return render_template("home.html", form=form)

@app.route("/business")
def business():
    #Connect to mariaDB
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
    cursor.execute("SELECT ExpenseDate, Description FROM expenses WHERE Category='Business'")
    #Fetch The Data from the Database(READ)
    rows = cursor.fetchall()
    return render_template("business.html", rows=rows)

@app.route("/personal")
def personal():
    #Connect to mariaDB
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
    cursor.execute("SELECT ExpenseDate, Description FROM expenses WHERE Category='Personal'")
    #Fetch The Data from the Database(READ)
    rows = cursor.fetchall()
    return render_template("personal.html", rows=rows)

#==============================================================
if __name__ == '__main__':
    app.run(debug = True)
