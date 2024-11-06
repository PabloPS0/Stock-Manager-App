"""
This module is responsible for the creation and initial configuration of the SQLite database and the necessary 
directories for data storage. It uses environment variables to determine the database path and automatically 
creates the folder for the database if it doesn't exist. 
"""
import os
import sqlite3
from dotenv import load_dotenv

# Load environment variables from.env file
load_dotenv()
DATABASE_PATH = os.getenv('DATABASE_PATH')

# Define database path and folder
DB_FOLDER = 'database'
DB_PATH = os.path.join(DB_FOLDER, 'inventory.db')

# Create folder if her not exist
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE inventory(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE NOT NULL,
price REAL,
quantity INTEGER)
''')

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
