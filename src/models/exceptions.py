class SFMShopException(Exception):
    #Базовое исключение для проекта SFMShop
    pass

class ValidationError(SFMShopException):
    # для ошибок валидации
    pass

class BusinessLogicError(SFMShopException):
    # для ошибок бизнес-логики
    pass

class DatabaseError(SFMShopException):
    # для ошибок базы данных
    pass

class NegativePriceError(ValidationError):
    # отрицательная цена
    pass

class InsufficientStockError(BusinessLogicError):
    # недостаточно товара
    pass

class InvalidOrderError(BusinessLogicError):
    # невалидный заказ
    pass
