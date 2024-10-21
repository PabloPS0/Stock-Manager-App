import tkinter as tk
import tkinter.messagebox as messagebox

class StockManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
    
        # Configurações da janela principal
        self.title('Stock Manager')
        self.geometry('800x400')

        # Criando containers para organizar os widgets
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

    # Criando widgets na janela principal
    def create_widgets(self):
        # Adicionando widgets no Top Frame
        self.label_name = tk.Label(self.top_frame, text="Product Name")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(self.top_frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        # Botão para confirmar o nome do produto
        self.btn_confirm_name = tk.Button(self.top_frame, text="Confirmar", command=self.get_name)
        self.btn_confirm_name.grid(row=0, column=2, padx=5, pady=5)

        self.label_price = tk.Label(self.top_frame, text="Price")
        self.label_price.grid(row=1, column=0, padx=5, pady=5)

        self.entry_price = tk.Entry(self.top_frame)
        self.entry_price.grid(row=1, column=1, padx=5, pady=5)

        # Botão para confirmar o preço
        self.btn_confirm_price = tk.Button(self.top_frame, text="Confirmar", command=self.get_price)
        self.btn_confirm_price.grid(row=1, column=2, padx=5, pady=5)

        self.label_quantity = tk.Label(self.top_frame, text="Quantity")
        self.label_quantity.grid(row=2, column=0, padx=5, pady=5)

        self.entry_quantity = tk.Entry(self.top_frame)
        self.entry_quantity.grid(row=2, column=1, padx=5, pady=5)

        # Botão para confirmar a quantidade
        self.btn_confirm_quantity = tk.Button(self.top_frame, text="Confirmar", command=self.get_quantity)
        self.btn_confirm_quantity.grid(row=2, column=2, padx=5, pady=5)

        # Adicionando uma área de lista no Mid Frame (pode ser uma lista de produtos)
        self.listbox_products = tk.Listbox(self.mid_frame)
        self.listbox_products.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Adicionando um Label de status no Bottom Frame
        self.status_label = tk.Label(self.bottom_frame, text="", fg="green")
        self.status_label.grid(row=0, column=0, sticky="ew")

    def get_name(self):
        product_name = self.entry_name.get()
        if product_name:
            messagebox.showinfo('Product Name', f'The product name is: {product_name}')
        else:
            messagebox.showwarning('Warning', 'Please enter a product name!')            

    def get_price(self):
        price = self.entry_price.get()
        if price:
            messagebox.showinfo('Price', f'The price is: {price}')
        else:
            messagebox.showwarning('Warning', 'Please enter a price!')

    def get_quantity(self):
        quantity = self.entry_quantity.get()
        if quantity:
            messagebox.showinfo('Quantity', f'The quantity is: {quantity}')
        else:
            messagebox.showwarning('Warning', 'Please enter a quantity!')

if __name__ == "__main__":
    app = StockManagerApp()
    app.mainloop()
