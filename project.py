import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

mycursor = mydb.cursor()  # mydb.cursor() creates a cursor object that is used to execute SQL queries.

mycursor.execute("CREATE DATABASE mydatabase") # mycursor.execute() runs the SQL query "CREATE DATABASE mydatabase", which creates a new database named mydatabase in MySQL.