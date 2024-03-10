import mysql.connector

password = ""
database_name = "college"

my_sql = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password
)
cursor = my_sql.cursor()
cursor.execute(f"DROP DATABASE {database_name}")
my_sql.commit()
