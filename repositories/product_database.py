import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv('DATABASE_PATH')

DB_FOLDER = 'repositories'
DB_PATH = os.path.join(DB_FOLDER, 'inventory.db')

conn = sqlite3.connect(database=DB_PATH)
cursor = conn.cursor()

class ProductFoundError(Exception):
    pass

class ProductRepository:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
    
    def add(self, name, price, quantity):
        self.cursor.execute("INSERT INTO inventory (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
        self.conn.commit()

    def search(self, id):
        search_results = self.cursor.execute("SELECT * FROM inventory WHERE id = ?", (id,)).fetchone()
        if search_results is None:
            raise ProductFoundError(f"Product with id {id} not found.")
        return search_results
    
    def update(self, name, price, quantity, id):
        search_product = self.cursor.execute("UPDATE inventory SET name = ?, price = ?, quantity = ? WHERE id = ?", (name, price, quantity, id))
        self.conn.commit()
        if search_product.rowcount == 0:
            raise ProductFoundError(f"Product with id {id} not found.")
        return True
    def list_all(self):
        results = self.cursor.fetchall()
        return results

    def remove(self, id):
        select_item = self.cursor.execute("SELECT * FROM inventory WHERE id = ?", (id,)).fetchone()
        if select_item:
            self.cursor.execute("DELETE FROM inventory WHERE id = ?", (id,))
            self.conn.commit()
        else:
            raise ProductFoundError(f"Product with id {id} not found.")
        
    def exit(self):
        if self.conn:
            self.conn.close()