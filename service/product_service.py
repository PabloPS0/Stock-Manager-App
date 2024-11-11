import os, sys
import customtkinter as ctk
from controllers import menu
from repositories.product_database import ProductRepository

class ProductValidator:
    def __init__(self, fields):
        def validate_non_empty_value(self):
            
            # Valida se todos os valores estão preenchidos
            for fields in self.fields:
                if not fields.get():
                    return False
            return True
        
        def validate_positive_price(self, price):
            # Valida se o preço é um número decimal positivo
            try:
                price = float(price)
                if price <= 0:
                    return False
            except ValueError:
                return False
            return True
        
        def validate_positive_quantity(self, quantity):
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    return False
            except ValueError:
                return False
            return True
        