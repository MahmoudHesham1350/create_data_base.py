import mysql.connector

my_db = mysql.connector.connect(
    host="sql11.freesqldatabase.com",
    user="sql11684204",
    passwd="Unwsg3ZCrp",
    database="sql11684204"
)
cursor = my_db.cursor()

cursor.execute("DROP TABLE IF EXIST students_data")
my_db.commit()
cursor.execute("DROP TABLE IF EXIST courses_data")
my_db.commit()

cursor.execute("CREATE TABLE students_data "
               "(id INT(15) NOT NULL,"
               "name VARCHAR(75) NOT NULL,"
               "password VARCHAR(45) NOT NULL,"
               "gp VARCHAR(1))")

cursor.execute("CREATE TABLE courses_data "
               "(courses VARCHAR(20),"
               "code VARCHAR(6))")

