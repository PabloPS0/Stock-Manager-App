import os
import sqlite3
from dotenv import load_dotenv
from service.product_service import ProductValidator, ProductFoundError

load_dotenv()

DATABASE_PATH = os.getenv('DATABASE_PATH')

DB_FOLDER = 'database'
DB_PATH = os.path.join(DB_FOLDER, 'inventory.db')

conn = sqlite3.connect(database=DB_PATH)
cursor = conn.cursor()

class ProductRepository:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.product_validator = ProductValidator()
    
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
        return 
    
    def list_all(self):
        self.cursor.execute("SELECT * FROM inventory")  # Executa uma consulta de seleção
        results = self.cursor.fetchall()  # Busca todos os resultados
        return results

    def remove(self, id):
        select_item = self.cursor.execute("SELECT * FROM inventory WHERE id = ?", (id,)).fetchone()
        if select_item:
            self.cursor.execute("DELETE FROM inventory WHERE id = ?", (id,))
            self.conn.commit()
        else:
            raise ProductFoundError(f"Product with id {id} not found.")
        
    def search_existings_ids(self):
        self.cursor.execute("SELECT id FROM inventory")
        existing_ids = [product[0] for product in self.cursor.fetchall()]
        return existing_ids
        
    def exit(self):
        if self.conn:
            self.conn.close()