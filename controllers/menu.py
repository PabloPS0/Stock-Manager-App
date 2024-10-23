import tkinter as tk
from tkinter import messagebox

class StockManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controle de Estoque")
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

        update_button = tk.Button(master=self.bottom_frame, text="Update Item", command=self.update_item)
        update_button.pack(pady=10)

        list_button = tk.Button(master=self.bottom_frame, text="List Item", command=self.update_item)
        list_button.pack(pady=10)

        remove_button = tk.Button(self.bottom_frame, text="Remove Item", command=self.remove_item)
        remove_button.pack(pady=10)

        exit_button = tk.Button(master=self.bottom_frame, text="Exit", command=self.close_window)
        exit_button.pack(pady=10)

    def add_item(self):
        # Lógica para adicionar item
        # Criar uma sub-janela
        window_add = tk.Toplevel(self)
    
    def search_item(self):
        # Lógica para pesquisar item
        messagebox.showinfo("Pesquisar Item", "Abrir sub-janela de Pesquisar Item")

    def update_item(self):
        # Lógica para atualizar item
        messagebox.showinfo("Atualizar Item", "Abrir sub-janela de Atualizar Item")
    
    def list_items(self):
        # Lógica para listar itens
        messagebox.showinfo("Listar Itens", "Abrir sub-janela de Listar Itens")

    def remove_item(self):
        # Lógica para remover item
        messagebox.showinfo("Remover Item", "Abrir sub-janela de Remover Item")

    def close_window(self):
        self.destroy()  # Fechar a janela principal e encerrar o programa
