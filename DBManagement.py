import mysql.connector

class DBManagement:
    def __init__(self, cursor):
        self.cursor = cursor

    def show_db(self):
        self.cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in self.cursor.fetchall()]
        print("===== Databases =====")
        for index, db in enumerate(databases):
            print(f'{index}. {db}')

    def create_db(self, db):
        try:
            self.cursor.execute(f'CREATE DATABASE {db}')
        except mysql.connector.Error as e:
            print(f'ERR: Failed to Create the Database: {e}')

    def drop_db(self, db):
        try:
            self.cursor.execute("SHOW DATABASES")
            databases = [db[0] for db in self.cursor.fetchall()]
            if db not in databases:
                print("ERR: Database is not Exist.")
            else:
                self.cursor.execute(f'DROP DATABASE {db}')
        except mysql.connector.Error as e:
            print(f'ERR: Failed to Drop the Database: {e}')

    def use_db(self, db):
        try:
            self.cursor.execute("SHOW DATABASES")
            databases = [db[0] for db in self.cursor.fetchall()]
            if db not in databases:
                print("ERR: Database is not Exist.")
                return False
            else:
                self.cursor.execute(f'USE {db}')
                return True
        except mysql.connector.Error as e:
            print(f'ERR: Failed to Use the Database: {e}')