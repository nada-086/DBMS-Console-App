import mysql.connector

class DBMS:
    def __init__(self):
        self.__db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        self.__cursor = self.__db.cursor()

    def show_db(self):
        self.__cursor.execute("SHOW DATABASES")

        print("===== Databases =====")
        for index, db in enumerate(self.__cursor):
            print(f'{index}. {db}')

    def check_table(self):
        pass

    def create_db(self, db):
        self.__cursor.execute(f'CREATE DATABASE {db}')