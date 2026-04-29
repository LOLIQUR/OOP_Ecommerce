"""
Тесты для класса Category.
"""
from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для класса Category."""

    def test_category_creation(self):
        """Тест создания категории."""
        product = Product("Ноутбук", "Мощный ноутбук", 50000, 10)
        category = Category("Электроника", "Вся электроника", [product])
        assert category.name == "Электроника"
        assert category.description == "Вся электроника"
        assert category._products == [product]

    def test_category_count_increment(self):
        """Тест увеличения счётчика категорий."""
        Category.category_count = 0
        Category.product_count = 0

        category1 = Category("Электроника", "Вся электроника", [])
        category2 = Category("Одежда", "Вся одежда", [])
        # используем переменные, чтобы не было ошибки F841
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
        assert category._products == []

    def test_add_product(self):
        """Тест метода add_product."""
        Category.category_count = 0
        Category.product_count = 0

        category = Category("Электроника", "Вся электроника", [])
        product = Product("Ноутбук", "Мощный ноутбук", 50000, 10)
        category.add_product(product)
        assert product in category._products
        assert Category.product_count == 1

    def test_products_property(self):
        """Тест геттера products."""
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        category = Category("Электроника", "Вся электроника", [product1, product2])
        expected = "Ноутбук, 50000 руб. Остаток: 10 шт.\nМышь, 1500 руб. Остаток: 25 шт."
        assert category.products == expected
