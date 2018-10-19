import mysql.connector as mariadb
from datetime import datetime

db_connection = mariadb.connect(host="localhost",
                                user="root",
                                passwd="root")

cursor = db_connection.cursor()

#Create DB
#db_create = 'CREATE SCHEMA kuditracker'
#cursor.execute(db_create)
cursor.execute('USE kuditracker')

#Create TABLE
#cursor.execute("CREATE TABLE expenses (id MEDIUMINT NOT NULL AUTO_INCREMENT, Expense_date DATE NOT NULL, Description CHAR(255) NOT NULL, Amount INT NOT NULL, Category CHAR(15) NOT NULL, PRIMARY KEY (id))")

#INSERT into TABLE
insert_data = "INSERT INTO expenses (ExpenseDate, Description, Amount, Category) VALUES (%s, %s, %s, %s)"

def date_format(date_string):
    """Function to return date object"""
    return datetime.strptime(date_string, "%d-%m-%Y").date()

data = [
        (date_format("24-05-2018"), "Gas filling", "50000", "Business"),
        (date_format("02-06-2018"), "Roof repair", "10000", "Personal"),
        (date_format("11-07-2018"), "Money paid to Felix", "1500000", "Business"),
        (date_format("19-03-2017"), "Visual Identity creation", "300000", "Business")
        ]
#Execute insert statement
cursor.executemany(insert_data, data)

#To make the changes to the table
db_connection.commit()
