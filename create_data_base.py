import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
cursor = my_db.cursor()

cursor.execute("CREATE DATABASE college")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="college"
)
cursor = my_db.cursor()


