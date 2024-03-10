from data_control1 import DataBase

db = DataBase()
db.connect_database()
db.add_student(1234, "ma", "pass")
print(db.get_students_data())
