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

        list_button = tk.Button(self.bottom_frame, text="List Item", command=self.list_items)
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
            try:
                self.product_database.add(name, price, quantity)
                messagebox.showinfo("Success", "Item added successfully!")
            except ProductFoundError as e:
                messagebox.showerror("Error", str(e))
            window_add.destroy()

        # Botão de Confirmação
        confirm_button = tk.Button(window_add, text="Confirm", command=confirm_add)
        confirm_button.grid(row=3, columnspan=2, pady=5, sticky="e")
    
    def search_item(self):
        # Lógica para pesquisar item
        window_search = tk.Toplevel(self)
        window_search.title("Search Item")

        # Labels e Entradas
        tk.Label(window_search, text="Id:").grid(row=1, column=0, padx=5, pady=5)
        id_entry = tk.Entry(window_search, width=30)
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Captura dados de entrada
        def confirm_search():
            id = id_entry.get()
            try:
                product = self.product_database.search(id)
                messagebox.showinfo("Success", f"Product found: {product}")
            except ProductFoundError as e:
                messagebox.showerror("Error", str(e))
            window_search.destroy()
        
        # Botão de Confirmação
        confirm_button = tk.Button(window_search, text="Confirm", command=confirm_search)
        confirm_button.grid(row=3, columnspan=2, pady=5, sticky="e")

    def update_item(self):
        # Lógica para atualizar item
        window_update = tk.Toplevel(self)
        window_update.title("Update Item")

        # Labels e Entradas
        tk.Label(window_update, text="Id:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(window_update, width=30)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Implementar a lógica de atualização do item
        def confirm_update():
            id = id_entry.get()
            try:
                # Verifique se o produto existe antes de capturar os novos valores
                product = self.product_database.search(id)

                # Desabilitar o campo ID
                id_entry.config(state='disabled')  # Desabilitar o campo do ID
                    
                tk.Label(window_update, text="Name:").grid(row=1, column=0, padx=5, pady=5)
                name_entry = tk.Entry(window_update, width=30)
                name_entry.grid(row=1, column=1, padx=5, pady=5)
                name_entry.insert(0, product[1])  # Presumindo que o nome é o segundo elemento

                tk.Label(window_update, text="Price:").grid(row=2, column=0, padx=5, pady=5)
                price_entry = tk.Entry(window_update, width=30)
                price_entry.grid(row=2, column=1, padx=5, pady=5)
                price_entry.insert(0, product[2])  # Presumindo que o preço é o terceiro elemento
                    
                tk.Label(window_update, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
                quantity_entry = tk.Entry(window_update, width=30)
                quantity_entry.grid(row=3, column=1, padx=5, pady=5)
                quantity_entry.insert(0, product[3])  # Presumindo que a quantidade é o quarto elemento
                
                # Atualiza o produto com os novos valores
                def update_product():
                    name = name_entry.get()
                    price = price_entry.get()
                    quantity = quantity_entry.get()

                    self.product_database.update(name, price, quantity, id)
                    messagebox.showinfo("Success", "Item updated successfully!")
                    window_update.destroy()  # Fechar a janela após o sucesso
                
                # Botão de Confirmação
                confirm_button = tk.Button(window_update, text="Confirm", command=update_product)
                confirm_button.grid(row=4, columnspan=2, pady=5, sticky="e")

            except ProductFoundError as e:
                messagebox.showerror("Error", str(e))
        
        # Botão para buscar o produto ao abrir a janela
        confirm_button = tk.Button(window_update, text="Search", command=confirm_update)
        confirm_button.grid(row=4, columnspan=2, pady=5, sticky="e")

    
    def list_items(self):
        # Lógica para listar itens
        window_list = tk.Toplevel(self)
        window_list.title("List All Items")
        
        listbox = tk.Listbox(window_list, width=50, height=15)
        listbox.pack(pady=10, padx=10)

        # Implementar a lógica de listagem dos itens
        try:
            items = self.product_database.list_all()
            if items: 
                for item in items:
                    listbox.insert(tk.END, item)
            else:
                messagebox.showinfo("Info", "No items found!")
                window_list.destroy()
        except ProductFoundError as e:
            messagebox.showerror("Error", f"Error listing items {str(e)}")

        # Botão para Fechar 
        if window_list.winfo_exists(): # Verifica se a janela ainda existe
            button_exit = tk.Button(window_list, text="Exit", command=window_list.destroy)
            button_exit.pack(pady=10)
        
    def remove_item(self):
        # Lógica para remover item
        window_remove = tk.Toplevel(self)
        window_remove.title("Remove Item")

        # Labels e Entradas
        tk.Label(window_remove, text="Id:").grid(row=1, column=0, padx=5, pady=5)
        id_entry = tk.Entry(window_remove, width=30)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Implementar a lógica de remoção do item
        def confirm_remove():
            id = id_entry.get()
            try:
                self.product_database.remove(id)
                messagebox.showinfo("Success", "Item removed successfully!")
            except ProductFoundError as e:
                messagebox.showerror("Error", str(e))

        # Botão de Confirmação
        confirm_button = tk.Button(window_remove, text="Confirm", command=confirm_remove)
        confirm_button.grid(row=3, columnspan=2, pady=5, sticky="e")

    def close_window(self):
        self.destroy()  # Fechar a janela principal e encerrar o programa
