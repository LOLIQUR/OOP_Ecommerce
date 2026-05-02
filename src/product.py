"""
Модуль для класса Product (Товар).
"""


class Product:
    """Класс для представления товара."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ):
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Сложение продуктов: общая стоимость товаров на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.price * self.quantity + other.price * other.quantity
