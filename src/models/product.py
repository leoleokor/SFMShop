from models.exceptions import NegativePriceError,InsufficientStockError,ValidationError
class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise NegativePriceError("Цена не может быть отрицательной")

        self.name = name
        self.price = price
        self.quantity = quantity

    def set_price(self, price):
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        self.price = price


    def check_product_availability(self,amount):
        if amount > self.quantity:
            raise InsufficientStockError(f"Товара недостаточно. На складе: {self.quantity}, требуется: {amount}")
        return True



    def get_total_price(self):
        return self.price * self.quantity
    # комментарий для конфликта №2
    # коммент для конфликта №1
    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.price < other.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False

        return self.price == other.price and self.name == other.name

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб., Количество: {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100

    def check_stock(self):
        return self.quantity > 0

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.quantity = quantity

    def get_category(self):
        pass