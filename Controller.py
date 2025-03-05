import mysql.connector
from DBManagement import DBManagement
from TableManagement import TableManagement

class Controller:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        self.cursor = self.db.cursor()

        self.db_management = DBManagement(self.cursor)
        self.table_management = TableManagement(self.cursor, self.db)
        self.db_in_use = False
        self.current_db = None

    def db_menu(self):
        print(""" ============ Database Operations ============
            1) Show Databases
            2) Create New Database
            3) Drop Database
            4) Use Database
            5) Exit
        """)

    def table_menu(self):
        print("""============ Table Operations ============
            1) Show Table
            2) Create New Table
            3) Drop Table
            4) Insert New Row
            5) Show Rows
            6) Delete Row
            7) Update Row
            8) Return to DB Management
        """)

    def db_operations(self):
        while True:
            self.db_menu()
            try:
                operation = int(input("Enter Operation Number: "))
                match operation:
                    case 1:
                        self.db_management.show_db()
                    case 2:
                        db = input("Enter Database Name: ")
                        self.db_management.create_db(db)
                    case 3:
                        db = input("Enter Database Name: ")
                        self.db_management.drop_db(db)
                    case 4:
                        state = False
                        db = input("Enter Database Name: ")
                        state = self.db_management.use_db(db)
                        if state:
                            self.db_in_use = True
                            self.current_db = db
                            self.table_operations()
                    case 5:
                        break
                    case _:
                        print("ERR: Invalid Operation Number")
            except ValueError:
                print("Value Error: Invalid Number. Please Enter a Valid Integer Input.")

    def table_operations(self):
        while True:
            self.table_menu()
            try:
                operation = int(input("Enter Operation Number: "))
                match operation:
                    case 1:
                        self.table_management.show_table()
                    case 2:  # create table
                        table_name = input("Enter Table Name: ")
                        columns = []
                        num_columns = int(input("Enter the Number of Columns: "))

                        for i in range(num_columns):
                            col_name = input(f"Enter name of column {i + 1}: ")
                            col_type = input(f"Enter Datatype of Column {i + 1} (e.g., VARCHAR(255), INT, DOUBLE, DATE): ")
                            columns.append(f"{col_name} {col_type}")
                        self.table_management.create_table(table_name, columns)
                    case 3:
                        table = input("Enter Table Name: ")
                        self.table_management.drop_table(table)
                    case 4: # insert 
                        table = input("Enter Table Name: ")  
                        if  not self.table_management.check_table(table):
                            print ("Table not found")
                            continue
                        columns = self.table_management.get_columns(table)
                        print(columns)
                        values = []
                        for i in range(len(columns)):
                            value = input(f"Enter value for {columns[i].split()[0]}: ")
                            values.append(value)
                        self.table_management.insert(table, columns, values)
                    case 5:
                        table = input("Enter Table Name: ")
                        self.table_management.show_rows(table)
                    case 6:
                        table = input("Enter Table Name: ")
                        if  not self.table_management.check_table(table):
                            print ("Table not found")
                            continue
                        row_id = int(input("Enter Row ID: "))
                        if  not self.table_management.check_id(table,row_id):
                            print ("ID not found")
                            continue

                        self.table_management.delete_row(table,row_id)

                    case 7:
                        table = input("Enter Table Name: ")
                        if  not self.table_management.check_table(table):
                            print ("Table not found")
                            continue
                        row_id = int(input("Enter Row ID: "))
                        if  not self.table_management.check_id(table,row_id):
                            print ("ID not found")
                            continue
                        columns = self.table_management.get_columns(table)
                        values = []
                        for column in columns:
                            value = input(f"Enter The new value {column}: ")
                            values.append(value)
                        self.table_management.update_row(table,row_id,values)
                    
                    case 8:
                        break

                    case _:
                        print("ERR: Invalid Operation")
            except Exception as e:
                print(e)
                print("Value Error: Invalid Number. Please Enter a Valid Integer Input.")
