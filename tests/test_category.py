"""
Тесты для класса Category.
"""
from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для класса Category."""

    def test_category_creation(self):
        product = Product("Ноутбук", "Мощный ноутбук", 50000, 10)
        category = Category("Электроника", "Вся электроника", [product])
        assert category.name == "Электроника"
        assert category.description == "Вся электроника"
        assert category._Category__products == [product]

    def test_category_count_increment(self):
        Category.category_count = 0
        Category.product_count = 0
        category1 = Category("Электроника", "Вся электроника", [])
        category2 = Category("Одежда", "Вся одежда", [])
        assert category1.name == "Электроника"
        assert category2.name == "Одежда"
        assert Category.category_count == 2

    def test_product_count_increment(self):
        Category.category_count = 0
        Category.product_count = 0
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        category = Category("Электроника", "Вся электроника", [product1, product2])
        assert category.name == "Электроника"
        assert Category.product_count == 2

    def test_empty_products_list(self):
        category = Category("Пустая", "Пустая категория", [])
        assert category._Category__products == []

    def test_add_product(self):
        Category.category_count = 0
        Category.product_count = 0
        category = Category("Электроника", "Вся электроника", [])
        product = Product("Ноутбук", "Мощный ноутбук", 50000, 10)
        category.add_product(product)
        assert product in category._Category__products
        assert Category.product_count == 1

    def test_products_property(self):
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        category = Category("Электроника", "Вся электроника", [product1, product2])
        expected = "Ноутбук, 50000 руб. Остаток: 10 шт.\nМышь, 1500 руб. Остаток: 25 шт."
        assert category.products == expected

    def test_category_str(self):
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        category = Category("Электроника", "Вся электроника", [product1, product2])
        expected = "Электроника, количество продуктов: 35 шт."
        assert str(category) == expected
