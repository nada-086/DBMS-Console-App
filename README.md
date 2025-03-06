# DBMS Console Application

## Description
This is a simple Database Management System (DBMS) console application using MySQL. It allows users to manage databases and tables, perform CRUD operations, and interact with MySQL databases through a command-line interface.

## Features
- **Database Operations:**
  - Show available databases
  - Create a new database
  - Drop an existing database
  - Use a selected database
- **Table Operations:**
  - Show available tables in the selected database
  - Create new tables with user-defined columns
  - Drop an existing table
  - Insert new rows into a table
  - Display rows from a table

## Requirements
- Python 3.x
- MySQL Server
- Required Python Libraries:
  - `mysql-connector-python`
  - `tabulate`

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/nada-086/DBMS-Console-App.git
   cd dbms-console-application
   ```
2. **Install Dependencies**
   ```sh
   pip install mysql-connector-python tabulate
   ```
3. **Configure MySQL Connection**
   - Ensure MySQL is running.
   - Update `Controller` class with appropriate `host`, `user`, and `password`.

## Usage
1. **Run the Application**
   ```sh
   python main.py
   ```
2. **Follow the On-Screen Menu:**
   - Choose database operations (create, drop, use databases).
   - If using a database, proceed to table operations.
   - Perform table actions (create, insert, view, delete tables).

## Project Structure
```
/dbms-console-application
├── DBManagement.py        # Handles database operations
├── TableManagement.py     # Handles table operations
├── Controller.py          # Manages user interaction and operations
├── main.py                # Entry point of the application
└── README.md              # Documentation
```

## Error Handling
- The application checks for invalid operations and handles MySQL errors gracefully.
- If an error occurs, an appropriate message is displayed to guide the user.
