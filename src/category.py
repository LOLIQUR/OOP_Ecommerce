"""
Модуль для класса Category (Категория).
"""
from typing import List
from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self._products = products  # Приватный атрибут

        # Увеличиваем счётчик категорий
        Category.category_count += 1

        # Увеличиваем счётчик товаров
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.

        Args:
            product: Объект класса Product
        """
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для получения строки всех продуктов в категории.
        """
        result = ""
        for product in self._products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result.rstrip("\n")
