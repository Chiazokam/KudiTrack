import mysql.connector as mariadb

db_connection = mariadb.connect(host="localhost",
                                user="root",
                                passwd="root")

cursor = db_connection.cursor()

#Create DB
db_create = 'CREATE SCHEMA kuditracker'
cursor.execute(db_create)
cursor.execute('USE kuditracker')

#Create TABLE
cursor.execute("CREATE TABLE expenses (id MEDIUMINT NOT NULL AUTO_INCREMENT, ExpenseDate DATE NOT NULL, Description CHAR(255) NOT NULL, Amount INT NOT NULL, Category CHAR(15) NOT NULL, PRIMARY KEY (id))")
