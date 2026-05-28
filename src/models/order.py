from models.product import Product
from models.exceptions import InvalidOrderError,BusinessLogicError
class Order:
    def __init__(self, order_id, user, products):
        self.order_id = order_id
        self.user = user
        if not products:
            raise BusinessLogicError("Заказ невалиден: пустой список товаров")
        self.products = products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise InvalidOrderError("Можно добавить только объект Product")

        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.get_total_price()

        return total

    def __str__(self):
        return f"Заказ пользователя {self.user.name} на сумму {self.calculate_total()} руб."