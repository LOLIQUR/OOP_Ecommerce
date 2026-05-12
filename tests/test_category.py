"""
Тесты для класса Category.
"""

from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для категорий."""

    def test_category_creation(self):
        """Тест создания категории."""
        product1 = Product("Телевизор", "4K телевизор", 45000.0, 3)
        product2 = Product("Плеер", "Blu-ray плеер", 10000.0, 7)
        category = Category(
            "Электроника", "Бытовая техника", [product1, product2]
        )

        assert category.name == "Электроника"
        assert category.description == "Бытовая техника"
        assert len(category._Category__products) == 2

    def test_category_count_increment(self):
        """Тест увеличения счётчика категорий."""
        Category.category_count = 0
        Category.product_count = 0
        category1 = Category("Электроника", "Вся электроника", [])
        category2 = Category("Одежда", "Вся одежда", [])
        assert category1.name == "Электроника"
        assert category2.name == "Одежда"
        assert Category.category_count == 2

    def test_product_count_increment(self):
        """Тест увеличения счётчика продуктов."""
        Category.category_count = 0
        Category.product_count = 0
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        category = Category("Электроника", "Вся электроника", [product1, product2])
        assert category.name == "Электроника"
        assert Category.product_count == 2

    def test_empty_products_list(self):
        """Тест категории с пустым списком товаров."""
        category = Category("Пустая", "Пустая категория", [])
        assert category._Category__products == []

    def test_add_product(self):
        """Тест метода add_product."""
        Category.category_count = 0
        Category.product_count = 0
        category = Category("Электроника", "Вся электроника", [])
        product = Product("Ноутбук", "Мощный ноутбук", 50000, 10)
        category.add_product(product)
        assert product in category._Category__products
        assert Category.product_count == 1

    def test_products_property(self):
        """Тест геттера products."""
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        category = Category("Электроника", "Вся электроника", [product1, product2])
        expected = "Ноутбук, 50000 руб. Остаток: 10 шт.\nМышь, 1500 руб. Остаток: 25 шт."
        assert category.products == expected

    def test_category_str(self):
        """Тест строкового представления категории."""
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        category = Category("Электроника", "Вся электроника", [product1, product2])
        expected = "Электроника, количество продуктов: 35 шт."
        assert str(category) == expected

    def test_average_price(self):
        """Тест среднего ценника категории."""
        product1 = Product("Товар1", "Описание", 100, 10)
        product2 = Product("Товар2", "Описание", 200, 5)
        category = Category("Категория", "Описание", [product1, product2])
        assert category.average_price() == 150.0

    def test_average_price_empty_category(self):
        """Тест среднего ценника пустой категории."""
        category = Category("Пустая", "Описание", [])
        assert category.average_price() == 0.0
