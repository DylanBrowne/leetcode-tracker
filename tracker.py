 # I need to import sqlite3, establish a connection to the database.db, and print a message to prove it was successful.
# SQLite is good for keeping track of data within a database

import sqlite3

# define connection and cursor. 

# Connections are used to connect to a database (database.db)
try:
    connection = sqlite3.connect("database.db")
    print("Established baseline SQLite connection pipeline")

    # Create a cursor to execute SQL statements and fetch results from SQL queries
    cursor = connection.cursor()


    # Create a database table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            pattern TEXT NOT NULL,
            confidence INTEGER NOT NULL
        )
    """)

    connection.commit()
    print("Database table successfully verified/created.")
except Exception as e:
    print(f"Something went wrong: {e}")

finally:
    if 'connection' in locals():
        connection.close()

def add_problem():
    title = input("Enter title of problem:")
    title_lower = title.lower()
    difficulty = input(f"Enter difficulty of {title_lower}: ")
    pattern = input(f"Enter pattern of {title_lower}: ")
    confidence = int(f"Enter confidence level for {title_lower}: ")