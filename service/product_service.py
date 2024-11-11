class ProductFoundError(Exception):
    """Exceção levantada quando um produto com ID já existente é encontrado."""
    pass

class ProductValidator:
    @staticmethod
    def validate_non_empty_value(fields):
        # Verifica se os campos não estão vazios
        return bool(fields)
    
    @staticmethod
    def validate_unique_id(id, existing_ids):
        # Verifica se o ID é único
        return id not in existing_ids
    
    @staticmethod
    def validate_numeric_id(id):
        # Verifica se o ID contém apenas números e é positivo
        return id.isdigit() and int(id) > 0
    
    @staticmethod
    def validate_positive_price(price):
        # Verifica se o preço é um número positivo
        try:
            price = float(price)
            return price > 0
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def validate_positive_quantity(quantity):
        try:
            quantity = int(quantity)
            return quantity > 0
        except (ValueError, TypeError):
            return False
        