from tabulate import tabulate
class TableManagement:
    def __init__(self, cursor, db):
        self.cursor = cursor
        self.db = db

    def get_tables(self):
        self.cursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables

    def show_table(self):
        tables = self.get_tables()
        print("===== Tables =====")
        for index, table in enumerate(tables):
            print(f'{index}. {table}')

    def create_table(self, table, columns):

        if table is None:
            print("ERR: Table Don't Exist")
        else:

            columns_sql = "id INT AUTO_INCREMENT PRIMARY KEY," + ", ".join(columns)
            create_table_query = f"CREATE TABLE {table} ({columns_sql})"
            self.cursor.execute(create_table_query)
            print(f"INFO: Table '{table}' Created Successfully!")

    def drop_table(self, table):
        tables = self.get_tables()
        if table in tables:
            self.cursor.execute(f'DROP TABLE {table}')
            print(f"INFO: Table '{table}' Dropped Successfully!")
        else:
            raise Exception("ERR: Table Don't Exist")

    def get_num_columns(self, table):
        if table is None:
            raise Exception("ERR: Table Don't Exist.")
        self.cursor.execute(f"""SELECT COUNT(*) 
                            FROM INFORMATION_SCHEMA.COLUMNS 
                            WHERE TABLE_NAME = '{table}';
                            """)
        column_count = self.cursor.fetchone()[0]
        return column_count

    def get_columns(self, table):
        if table is None:
            raise Exception("ERR: Table Don't Exist")
        self.cursor.execute(f"""SELECT COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = '{table}'
        """)
        columns = [row[0] for row in self.cursor.fetchall()]
        columns.remove('id')
        return columns

    def insert(self, table, columns, values):
        tables = self.get_tables()
        if table in tables:
            #columns.remove('id')
            print(columns)
            num_columns = self.get_num_columns(table) - 1
            columns_names = ", ".join([col.split()[0] for col in columns])
            placeholders = ", ".join(["%s"] * num_columns)
            insert_query = f"INSERT INTO {table} ({columns_names}) VALUES ({placeholders})"
            self.cursor.execute(insert_query, tuple(values))
            self.db.commit()
            print("INFO: Data Inserted Successfully!")
        else:
            print("ERR: Table Don't Exist.")

    def show_rows(self, table):
        tables = self.get_tables()
        if table in tables:
            columns_names = self.get_columns(table)
            self.cursor.execute(f"SELECT * FROM {table}")
            rows = self.cursor.fetchall()
            print(tabulate(rows, headers=columns_names, tablefmt="grid"))
        else:
            print("ERR: Table Don't Exist")
    
    def delete_row(self,table,row_id):
        tables = self.get_tables()
        if table in tables:
           self.cursor.execute(f'SELECT * FROM {table} WHERE id = {row_id};')
           count=len(self.cursor.fetchall())
           if (count == 0 ):
            print("ID not found")
           else:  
            self.cursor.execute(f' DELETE FROM {table} WHERE id = {row_id};')
        else:
            print("ERR: Table Don't Exist")

    def update_row(self,table,row_id,values):
        tables = self.get_tables()
        if table in tables: 
            columns = self.get_columns(table)
            # columns.append("id")
            # values.append(row_id)
            # self.delete_row(table,row_id)
            # self.insert(table,columns,values)
            self.cursor.execute(f'SELECT * FROM {table} WHERE id = {row_id};')
            count=len(self.cursor.fetchall())
            if (count == 0 ):
               print("ID not found")
            else:  
                columns = self.get_columns(table)
                # set_query = "SET"
                # for i in range(len(columns)):
                #     set_query = set_query + columns[i] + '=' + values[i]  + ','
                # self.cursor.execute(f'UPDATE {table} {set_query[:len(set_query)-1]} WHERE id = {row_id};')
                set_query = ", ".join([f"{col} = %s" for col in columns])
                query = f'UPDATE {table} SET {set_query} WHERE id = %s;'
                self.cursor.execute(query, (*values, row_id))
                print("Row updated successfully")

            
        else:
            print("ERR: Table Don't Exist")

        
        


