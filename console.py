from DBMS import DBMS

def menu():
    print(""" ============ Database Management System ============
        1) Show Databases
        2) Create New Database
        3) Drop Database
        4) Create New Table
        5) Drop Table
        6) Insert New Row
        7) Alter a Row
        8) Exit
    """)

def main():
    while True:
        menu()
        try:
            operation = int(input("Enter Operation Number: "))
            match operation:
                case 1:
                    dbms.show_db()
                case 2:
                    db = input("Enter Database Name: ")
                    dbms.create_db(db)
                case 3:
                    table_name = input("Enter Table Name: ")

                case _:
                    print("ERR: Invalid Operation Number")
        except ValueError:
            print("Value Error: Invalid Number. Please Enter a Valid Integer Input.")

dbms = DBMS()
main()