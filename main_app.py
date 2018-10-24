from flask import Flask, render_template, url_for, redirect, session, request, jsonify
from wtforms import Form, validators, StringField, TextAreaField, DateField, IntegerField, SelectField, SubmitField
import mysql.connector as mariadb
from datetime import datetime
import pymysql  #Downloaded and imported

app = Flask(__name__)

#==============================================================================
def dbConnection():
    """Function to connect to the DB"""
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
#==============================================================================
#Create function to change date to a date object
def date_format(date_string):
    """Function to return date object"""
    return datetime.strptime(date_string, "%Y-%m-%d").date()
#==============================================================================
#Define the Form class
class ExpenseForm(Form):
    expense_date = DateField('Date: yyyy-mm-dd', [validators.DataRequired()])
    expense_descr = StringField('Description', [validators.length(max=20), validators.DataRequired()])
    expense_amt = IntegerField('Amount', [validators.DataRequired()])
    expense_cat = StringField('Category: Business Or Personal', [validators.DataRequired()])

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

@app.route('/addExpense', methods=['GET', 'POST'])
def addExpense():
    #form = ExpenseForm(request.form)
    expense_amt = pymysql.escape_string(request.form['expense_amt'])
    #Capture query data using json
    print(request.form, "request", request)
    body = {
        "status": "success",
        "expense_amt": expense_amt
        }
    print(body)
    return jsonify(body)

#SHOW BUSINESS
@app.route("/business")
def business():
    #Connect to mariaDB
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
    cursor.execute("SELECT id, ExpenseDate, Description FROM expenses WHERE Category='Business'")
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
    cursor.execute("SELECT id, ExpenseDate, Description FROM expenses WHERE Category='Personal'")
    #Fetch The Data from the Database(READ)
    rows = cursor.fetchall()
    return render_template("personal.html", rows=rows)

@app.route("/personal/<id>")
def deletePersonal(id):
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
    deleteQuery = "DELETE FROM expenses WHERE id = %s"
    id = (id, )
    cursor.execute(deleteQuery, id)
    db_conn.commit()
    return redirect(url_for("personal"))

@app.route("/business/<id>")
def deleteBusiness(id):
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
    deleteQuery = "DELETE FROM expenses WHERE id = %s"
    id = (id, )
    cursor.execute(deleteQuery, id)
    db_conn.commit()
    return redirect(url_for("business"))

@app.route("/personal/<id>/edit")
def editPersonal(id):
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
    selectQuery = "SELECT * FROM expenses WHERE id = %s"
    id = (id, )
    cursor.execute(selectQuery, id)
    #Fetch The Data from the Database(READ)
    row = cursor.fetchone()
    print(row)
    return render_template("editPersonal.html", row=row)

@app.route("/business/<id>/edit")
def editBusiness(id):
    db_conn = mariadb.connect(user='root',
                              password='root',
                              database='kuditracker')
    cursor = db_conn.cursor()
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
        print(request.form, "request", request)
        db_conn = mariadb.connect(user='root',
                                  password='root',
                                  database='kuditracker')
        cursor = db_conn.cursor()
        #Update row in db
        updateQuery = "UPDATE expenses SET ExpenseDate='%s', Description='%s', Amount='%s', Category='%s' WHERE id='%s'" % (expense_date, expense_descr, expense_amt, expense_cat, id)
        cursor.execute(updateQuery)
        db_conn.commit()
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
        print(request.form, "request", request)
        db_conn = mariadb.connect(user='root',
                                  password='root',
                                  database='kuditracker')
        cursor = db_conn.cursor()
        #Update row in db
        updateQuery = "UPDATE expenses SET ExpenseDate='%s', Description='%s', Amount='%s', Category='%s' WHERE id='%s'" % (expense_date, expense_descr, expense_amt, expense_cat, id)
        cursor.execute(updateQuery)
        db_conn.commit()
        #Close connection
        cursor.close()
        return redirect(url_for("business"))

#==============================================================
if __name__ == '__main__':
    app.run(debug = True)
