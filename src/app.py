import sys, os
# Inserting the project root directory into the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from controllers.menu import StockManagerApp

# Starting the program's graphical interface
if __name__ == "__main__":
    app = StockManagerApp().mainloop()  # Instanciando a classe StockManagerApp
    app.mainloop()            