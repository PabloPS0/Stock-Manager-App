import tkinter as tk
from tkinter import messagebox
from repositories.product_database import ProductFoundError, ProductRepository
from service.product_service import ProductValidator

class StockManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.product_database = ProductRepository()
        self.title("StockManager")
        self.protocol("WM_DELETE_WINDOW", self.close_window) # Configure the closing protocol
        self.create_containers()
        self.create_widgets()

    def create_containers(self):
        # Top Frame (por exemplo, pode conter entradas e botões principais)
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(fill=tk.X)
        
        # Mid Frame (pode conter listboxes, labels, etc.)
        self.mid_frame = tk.Frame(self)
        self.mid_frame.pack(fill=tk.BOTH, expand=True)
        
        # Bottom Frame (pode conter botões de ações)
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(fill=tk.X)

    def create_widgets(self):
        # Botões do menu
        add_button = tk.Button(self.bottom_frame, text="Add Item", command=self.add_item)
        add_button.pack(pady=10)

        search_button = tk.Button(self.bottom_frame, text="Search Item", command=self.search_item)
        search_button.pack(pady=10)

        update_button = tk.Button(self.bottom_frame, text="Update Item", command=self.update_item)
        update_button.pack(pady=10)

        list_button = tk.Button(self.bottom_frame, text="List Item", command=self.update_item)
        list_button.pack(pady=10)

        remove_button = tk.Button(self.bottom_frame, text="Remove Item", command=self.remove_item)
        remove_button.pack(pady=10)

        exit_button = tk.Button(self.bottom_frame, text="Exit", command=self.close_window)
        exit_button.pack(pady=20)

    def add_item(self):
        # Lógica para adicionar item
        # Criar uma sub-janela
        window_add = tk.Toplevel(self)
        window_add.title("Add Item")
        # Labels e Entradas
        tk.Label(window_add, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(window_add, width=30)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(window_add, text="Price:").grid(row=1, column=0, padx=5, pady=5)
        price_entry = tk.Entry(window_add, width=30)
        price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window_add, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        quantity_entry = tk.Entry(window_add, width=30)
        quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        # Captura dados de entrada
        def confirm_add():
            name = name_entry.get()
            price = price_entry.get()
            quantity = quantity_entry.get()

            # Adiciona o produto ao repositório e banco de dados
            self.product_database.add(name, price, quantity)
            messagebox.showinfo("Success", "Item added successfully!")
            window_add.destroy()

        
        # Botão de Confirmação
        confirm_button = tk.Button(window_add, text="Confirm", command=confirm_add)
        confirm_button.grid(row=3, columnspan=2, pady=5, sticky="e")
    
    def search_item(self):
        # Lógica para pesquisar item
        window_search = tk.Toplevel(self)

    def update_item(self):
        # Lógica para atualizar item
        window_update = tk.Toplevel(self)
    
    def list_items(self):
        # Lógica para listar itens
        window_list = tk.Toplevel(self)

    def remove_item(self):
        # Lógica para remover item
        window_remove = tk.Toplevel(self)

    def close_window(self):
        self.destroy()  # Fechar a janela principal e encerrar o programa
