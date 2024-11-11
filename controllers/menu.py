from cProfile import label
import customtkinter as ctk
from tkinter import messagebox
from repositories.product_database import ProductRepository
from service.product_service import ProductValidator, ProductFoundError

class StockManagerApp(ctk.CTk):   # Change: Using CTk as base
    def __init__(self):
        super().__init__()
        self.product_service = ProductValidator()
        self.product_database = ProductRepository()
        self.title("StockManager")
        self.protocol("WM_DELETE_WINDOW", self.close_window) # Configure the closing protocol
        self.configure(bg='black')
        self.minsize(600, 400) # width, height
        self.maxsize(800, 600)
        self.geometry("600x400+50+50") # width x height + x + y

        # Theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_containers()
        self.create_widgets()

    def create_containers(self):
        # Top Frame (por exemplo, pode conter entradas e botões principais)
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill=ctk.X, pady=5, padx=5)
        
        # Mid Frame (pode conter listboxes, labels, etc.)
        self.mid_frame = ctk.CTkFrame(self)
        self.mid_frame.pack(fill=ctk.BOTH, expand=True)
        
        # Bottom Frame (pode conter botões de ações)
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(fill=ctk.X, pady=5, padx=5)

    def create_widgets(self):
        name_app = ctk.CTkLabel(self.top_frame, text="StockManager", font=("Arial", 24))
        name_app.pack(pady=20)
        # Botões do menu
        add_button = ctk.CTkButton(self.mid_frame, text="Add Item", command=self.add_item)
        add_button.pack(pady=10)

        search_button = ctk.CTkButton(self.mid_frame, text="Search Item", command=self.search_item)
        search_button.pack(pady=10)

        update_button = ctk.CTkButton(self.mid_frame, text="Update Item", command=self.update_item)
        update_button.pack(pady=10)

        list_button = ctk.CTkButton(self.mid_frame, text="List Item", command=self.list_items)
        list_button.pack(pady=10)

        remove_button = ctk.CTkButton(self.mid_frame, text="Remove Item", command=self.remove_item)
        remove_button.pack(pady=10)

        exit_button = ctk.CTkButton(self.bottom_frame, text="Exit", command=self.close_window)
        exit_button.pack(pady=10)

    def add_item(self):
        # Lógica para adicionar item
        # Criar uma sub-janela
        window_add = ctk.CTkToplevel(self)
        window_add.title("Add Item")
        # Labels e Entradas
        ctk.CTkLabel(window_add, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ctk.CTkEntry(window_add, width=30)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(window_add, text="Price:").grid(row=1, column=0, padx=5, pady=5)
        price_entry = ctk.CTkEntry(window_add, width=30)
        price_entry.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(window_add, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        quantity_entry = ctk.CTkEntry(window_add, width=30)
        quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        # Captura dados de entrada
        def confirm_add():
            name = name_entry.get()
            price = price_entry.get()
            quantity = quantity_entry.get()

            if not ProductValidator.validate_non_empty_value(name):
                messagebox.showerror("Error", "Name cannot be empty.")
                return
            if not ProductValidator.validate_positive_price(price):
                messagebox.showerror("Error", "Price must be a positive number.")
                return
            if not ProductValidator.validate_positive_quantity(quantity):
                messagebox.showerror("Error", "Quantity must be a positive number.")
                return

            # Caso não haja erros os dados serão enviados para a camada de repositórios
            try:
                self.product_service.add(name, price, quantity)
                messagebox.showinfo("Success", "Item added successfully!")
            except ProductFoundError as e:
                messagebox.showerror("Error", str(e))
            window_add.destroy()

        # Botão de Confirmação
        confirm_button = ctk.CTkButton(window_add, text="Confirm", command=confirm_add)
        confirm_button.grid(row=3, columnspan=2, pady=5, sticky="e")
    
    def search_item(self):
        # Lógica para pesquisar item
        window_search = ctk.CTkToplevel(self)
        window_search.title("Search Item")

        # Labels e Entradas
        ctk.CTkLabel(window_search, text="Id:").grid(row=1, column=0, padx=5, pady=5)
        id_entry = ctk.CTkEntry(window_search, width=30)
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Captura dados de entrada
        def confirm_search():
            id = id_entry.get()

            if not ProductValidator.validate_non_empty_value(id):
                messagebox.showerror("Error", "Id cannot be empty.")
                return
            if not ProductValidator.validate_numeric_id(id):
                messagebox.showerror("Error", "Id must be a numeric value.")
                return
            if not ProductValidator.validate_unique_id(id):
                messagebox.showerror("Error", "Id must be unique.")
                return
            
            # Caso não haja erros os dados serão enviados para a camada de repositórios
            try:
                product = self.product_database.search(id)
                messagebox.showinfo("Success", f"Product found: {product}")
            except ProductFoundError as e:
                messagebox.showerror("Error", str(e))
            window_search.destroy()
        
        # Botão de Confirmação
        confirm_button = ctk.CTkButton(window_search, text="Confirm", command=confirm_search)
        confirm_button.grid(row=3, columnspan=2, pady=5, sticky="e")

    def update_item(self):
        # Lógica para atualizar item
        window_update = ctk.CTkToplevel(self)
        window_update.title("Update Item")

        # Labels e Entradas
        ctk.CTkLabel(window_update, text="Id:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ctk.CTkEntry(window_update, width=30)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Implementar a lógica de atualização do item
        def confirm_update():
            id = id_entry.get()
            try:
                # Verifique se o produto existe antes de capturar os novos valores
                product = self.product_database.search(id)

                # Desabilitar o campo ID
                id_entry.config(state='disabled')  # Desabilitar o campo do ID
                    
                ctk.CTkLabel(window_update, text="Name:").grid(row=1, column=0, padx=5, pady=5)
                name_entry = ctk.CTkEntry(window_update, width=30)
                name_entry.grid(row=1, column=1, padx=5, pady=5)
                name_entry.insert(0, product[1])  # Presumindo que o nome é o segundo elemento

                ctk.CTkLabel(window_update, text="Price:").grid(row=2, column=0, padx=5, pady=5)
                price_entry = ctk.CTkEntry(window_update, width=30)
                price_entry.grid(row=2, column=1, padx=5, pady=5)
                price_entry.insert(0, product[2])  # Presumindo que o preço é o terceiro elemento
                    
                ctk.CTkLabel(window_update, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
                quantity_entry = ctk.CTkEntry(window_update, width=30)
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
                confirm_button = ctk.CTkButton(window_update, text="Confirm", command=update_product)
                confirm_button.grid(row=4, columnspan=2, pady=5, sticky="e")

            except ProductFoundError as e:
                messagebox.showerror("Error", str(e))
        
        # Botão para buscar o produto ao abrir a janela
        confirm_button = ctk.CTkButton(window_update, text="Search", command=confirm_update)
        confirm_button.grid(row=4, columnspan=2, pady=5, sticky="e")

    
    def list_items(self):
        # Lógica para listar itens
        window_list = ctk.CTkToplevel(self)
        window_list.title("List All Items")
        
        listbox = ctk.CTkListbox(window_list, width=50, height=15)
        listbox.pack(pady=10, padx=10)

        # Implementar a lógica de listagem dos itens
        try:
            items = self.product_database.list_all()
            if items: 
                for item in items:
                    listbox.insert(ctk.CTkEND, item)
            else:
                messagebox.showinfo("Info", "No items found!")
                window_list.destroy()
        except ProductFoundError as e:
            messagebox.showerror("Error", f"Error listing items {str(e)}")

        # Botão para Fechar 
        if window_list.winfo_exists(): # Verifica se a janela ainda existe
            button_exit = ctk.CTkButton(window_list, text="Exit", command=window_list.destroy)
            button_exit.pack(pady=10)
        
    def remove_item(self):
        # Lógica para remover item
        window_remove = ctk.CTkToplevel(self)
        window_remove.title("Remove Item")

        # Labels e Entradas
        ctk.CTkLabel(window_remove, text="Id:").grid(row=1, column=0, padx=5, pady=5)
        id_entry = ctk.CTkEntry(window_remove, width=30)
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
        confirm_button = ctk.CTkButton(window_remove, text="Confirm", command=confirm_remove)
        confirm_button.grid(row=3, columnspan=2, pady=5, sticky="e")

    def close_window(self):
        self.destroy()  # Fechar a janela principal e encerrar o programa
