from flask import Flask, render_template, url_for, redirect, session, request, jsonify
from wtforms import Form, validators, StringField, TextAreaField, DateField, IntegerField, SelectField, SubmitField
import mysql.connector as mariadb
from datetime import datetime
import pymysql  #Downloaded and imported
from flask_mysqldb import MySQL

app = Flask(__name__)
#==============================================================================
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kuditracker'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
#==============================================================================
#Create function to change date to a date object
def date_format(date_string):
    """Function to return date object"""
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Incorrect date format, should be in yyyy-mm-dd format")
#==============================================================================
#Define the Form class
class ExpenseForm(Form):
    expense_date = DateField('Date: yyyy-mm-dd', [validators.DataRequired()])
    expense_descr = StringField('Description', [validators.length(max=20), validators.DataRequired()])
    expense_amt = IntegerField('Amount', [validators.DataRequired()])
    expense_cat = StringField('Category: business Or personal', [validators.DataRequired()])

#ADD NEW EXPENSE
@app.route('/', methods=['GET', 'POST'])
def home():
    form = ExpenseForm(request.form)
    #Triggered if form is filled and submitted
    if request.method == 'POST':
        expense_date = date_format(request.form['expense_date'])
        #Escape characters that may cause an error when inserted into the db e.g, apostrophe
        expense_descr =  pymysql.escape_string(request.form['expense_descr'])
        expense_amt = pymysql.escape_string(request.form['expense_amt'])
        expense_cat = request.form['expense_cat'].lower()

        if expense_cat == 'personal' or expense_cat == 'business':
            #Create Cursor
            cursor = mysql.connection.cursor()
            #Insert data into the db
            query = "INSERT INTO expenses (ExpenseDate, Description, Amount, Category) VALUES ('{}', '{}', '{}', '{}')".format(expense_date, expense_descr, expense_amt, expense_cat)
            cursor.execute(query)
            mysql.connection.commit()
            #Close connection
            cursor.close()
            return redirect(url_for("home"))    #Putting return, the form data was cleared from the form after submission
    #Default page to render without the form filling
    return render_template("home.html", form=form)

@app.route('/addExpense', methods=['GET', 'POST'])
def addExpense():
    expense_date = date_format(request.form['expense_date'])
    expense_descr =  pymysql.escape_string(request.form['expense_descr'])
    expense_amt = pymysql.escape_string(request.form['expense_amt'])
    expense_cat = request.form['expense_cat']

    #Capture query data using json
    body = {
        "status": "success",
        "expense_date": expense_date,
        "expense_descr": expense_descr,
        "expense_amt": expense_amt,
        "expense_cat": expense_cat
        }
    return jsonify(body)

#SHOW BUSINESS
@app.route("/business")
def business():
    #Create Cursor
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, ExpenseDate, Amount, Description FROM expenses WHERE Category='business'")
    #Fetch The Data from the Database(READ)
    rows = cursor.fetchall()
    return render_template("business.html", rows=rows)

@app.route("/personal")
def personal():
    #Create Cursor
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, ExpenseDate, Amount, Description FROM expenses WHERE Category='personal'")
    #Fetch The Data from the Database(READ)
    rows = cursor.fetchall()
    return render_template("personal.html", rows=rows)

@app.route("/personal/<id>")
def deletePersonal(id):
    #Create Cursor
    cursor = mysql.connection.cursor()
    deleteQuery = "DELETE FROM expenses WHERE id = %s"
    id = (id, )
    cursor.execute(deleteQuery, id)
    mysql.connection.commit()
    return redirect(url_for("personal"))

@app.route("/business/<id>")
def deleteBusiness(id):
    #Create Cursor
    cursor = mysql.connection.cursor()
    deleteQuery = "DELETE FROM expenses WHERE id = %s"
    id = (id, )
    cursor.execute(deleteQuery, id)
    mysql.connection.commit()
    return redirect(url_for("business"))

@app.route("/personal/<id>/edit")
def editPersonal(id):
    #Create Cursor
    cursor = mysql.connection.cursor()
    selectQuery = "SELECT * FROM expenses WHERE id = %s"
    id = (id, )
    cursor.execute(selectQuery, id)
    #Fetch The Data from the Database(READ)
    row = cursor.fetchone()
    return render_template("editPersonal.html", row=row)

@app.route("/business/<id>/edit")
def editBusiness(id):
    #Create Cursor
    cursor = mysql.connection.cursor()
    selectQuery = "SELECT * FROM expenses WHERE id = %s"
    id = (id, )
    cursor.execute(selectQuery, id)
    #Fetch The Data from the Database(READ)
    row = cursor.fetchone()
    return render_template("editBusiness.html", row=row)

@app.route("/personal/<id>", methods=['GET', 'POST'])
def updatePersonal(id):
    form = ExpenseForm(request.form)
    #Triggered if edited form is filled and submitted
    if request.method == 'POST':
        expense_date = date_format(request.form['expense_date'])
        #Escape characters that may cause an error when inserted into the db e.g, apostrophe
        expense_descr =  pymysql.escape_string(request.form['expense_descr'])
        expense_amt = pymysql.escape_string(request.form['expense_amt'])
        expense_cat = request.form['expense_cat']
        #Create Cursor
        cursor = mysql.connection.cursor()
        #Update row in db
        updateQuery = "UPDATE expenses SET ExpenseDate='%s', Description='%s', Amount='%s', Category='%s' WHERE id='%s'" % (expense_date, expense_descr, expense_amt, expense_cat, id)
        cursor.execute(updateQuery)
        mysql.connection.commit()
        #Close connection
        cursor.close()
        return redirect(url_for("personal"))

@app.route("/business/<id>", methods=['GET', 'POST'])
def updateBusiness(id):
    form = ExpenseForm(request.form)
    #Triggered if edited form is filled and submitted
    if request.method == 'POST':
        expense_date = date_format(request.form['expense_date'])
        #Escape characters that may cause an error when inserted into the db e.g, apostrophe
        expense_descr =  pymysql.escape_string(request.form['expense_descr'])
        expense_amt = pymysql.escape_string(request.form['expense_amt'])
        expense_cat = request.form['expense_cat']
        #Create Cursor
        cursor = mysql.connection.cursor()
        #Update row in db
        updateQuery = "UPDATE expenses SET ExpenseDate='%s', Description='%s', Amount='%s', Category='%s' WHERE id='%s'" % (expense_date, expense_descr, expense_amt, expense_cat, id)
        cursor.execute(updateQuery)
        mysql.connection.commit()
        #Close connection
        cursor.close()
        return redirect(url_for("business"))

#==============================================================
if __name__ == '__main__':
    app.run(debug = True)
