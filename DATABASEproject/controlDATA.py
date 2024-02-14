import mysql.connector


class DataBase:
    def __init__(self):
        self.my_db = None
        self.cursor = None
        self.host = "sql11.freesqldatabase.com"
        self.user = "sql11684204"
        self.password = "Unwsg3ZCrp"
        self.data_base = "sql11684204"
        self.students_table = "students_data"
        self.courses_table = "courses_data"
        self.id_col = "id"
        self.name_col = "name"
        self.pass_col = "password"
        self.group_col = "gp"
        self.courses_col = "courses"
        self.code_col = "code"

    def connect_database(self):
        try:
            self.my_db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.data_base
            )
            print("connected to database")
            self.cursor = self.my_db.cursor()
            return True
        except Exception as e:
            print(e)
            print("Failed to connect to database")

    def add_student(self, st_id, name, password):
        query = (f"INSERT INTO {self.students_table} ({self.id_col},"
                 f" {self.name_col}, {self.pass_col}) VALUES (%s, %s, %s)")
        data = (f"{st_id}", f"{name}", f"{password}")
        self.cursor.execute(query, data)
        self.my_db.commit()
        print("Student Added")
        self.cursor.execute(f"ALTER TABLE {self.courses_table} ADD COLUMN ID_{st_id} BOOLEAN NULL DEFAULT 0")

    def get_data(self, data_wanted, table_from, where=""):
        self.cursor.execute(f"SELECT {data_wanted} FROM {table_from} {where}")
        res = self.cursor.fetchall()
        return res

    def get_students_data(self, data_wanted="default"):
        if data_wanted == "default":
            data_wanted = f"{self.id_col}, {self.name_col}, {self.group_col}"
        return self.get_data(data_wanted, self.students_table)

    def get_student_by_id(self, st_id, data_wanted="default"):
        if data_wanted == "default":
            data_wanted = f"{self.id_col}, {self.name_col}, {self.group_col}"
        student = self.get_data(data_wanted, self.students_table, f"WHERE {self.id_col} = {st_id}")
        if student:
            return student[0]

    def get_students_name_start(self, start_with, data_wanted="default"):
        if data_wanted == "default":
            data_wanted = f"{self.id_col}, {self.name_col}, {self.group_col}"
            return self.get_data(data_wanted, self.students_table,
                                 f"WHERE {self.name_col} LIKE '{start_with}%' ")

    def delete_student_by_id(self, st_id):
        self.cursor.execute(f"DELETE FROM {self.students_table} WHERE {self.id_col}={st_id}")
        self.cursor.execute(f"ALTER TABLE {self.courses_table} DROP COLUMN ID_{st_id} ")
        self.my_db.commit()

    def edit_student(self, st_id, column, new_info):
        self.cursor.execute(f"UPDATE {self.students_table} SET {column} = '{new_info}' WHERE {self.id_col} = {st_id}")
        self.my_db.commit()

    def look_id_exist(self, st_id):
        return bool(self.get_data("*", self.students_table, f"WHERE {self.id_col} = {st_id}"))

    def add_course(self, name, code):
        query = f"INSERT INTO {self.courses_table} ({self.courses_col}, {self.code_col}) VALUES (%s, %s)"
        data = (f"{name}", f"{code}")
        self.cursor.execute(query, data)
        self.my_db.commit()
        print("course added")

    def delete_courses(self, name_code):
        self.cursor.execute(f"DELETE FROM {self.courses_table} "
                            f"WHERE {self.courses_col}='{name_code}' OR {self.code_col}='{name_code}'")
        self.my_db.commit()

    def st_course_remove(self, st_id, name_code):
        self.st_course_change(st_id, name_code, "FALSE")

    def st_course_add(self, st_id, name_code):
        self.st_course_change(st_id, name_code, "TRUE")

    def st_course_change(self, st_id, name_code, add_remove):
        self.cursor.execute(f"UPDATE {self.courses_table} SET ID_{st_id} = {add_remove} "
                            f"WHERE {self.courses_col} = '{name_code}' OR {self.code_col} = '{name_code}' ")
        self.my_db.commit()

    def get_st_courses(self, st_id):
        data_wanted = f"{self.courses_col}, {self.code_col}"
        return self.get_data(data_wanted, self.courses_table,
                             f" WHERE ID_{st_id} = TRUE")



