import mysql.connector

password = ""
database_name = "college"

my_sql = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password
)
cursor = my_sql.cursor()
cursor.execute("CREATE DATABASE college")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password,
    database=database_name
)
cursor = my_db.cursor()

cursor.execute("CREATE TABLE students_data "
               "(id INT(15) NOT NULL,"
               "name VARCHAR(75) NOT NULL,"
               "password VARCHAR(45) NOT NULL,"
               "gp VARCHAR(1))")

cursor.execute("CREATE TABLE courses_data "
               "(courses VARCHAR(20),"
               "code VARCHAR(6))")
