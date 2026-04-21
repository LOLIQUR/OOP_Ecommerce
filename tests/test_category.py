"""
Тесты для класса Category.
"""
from src.product import Product
from src.category import Category


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
        assert len(category.products) == 2

    def test_category_count_increment(self):
        """Тест увеличения счётчика категорий."""
        Category.category_count = 0  # Сброс для чистоты теста
        Category("Книги", "Художественная литература", [])
        Category("Игрушки", "Детские игрушки", [])
        assert Category.category_count == 2

    def test_product_count_increment(self):
        """Тест увеличения счётчика продуктов."""
        Category.category_count = 0
        Category.product_count = 0

        p1 = Product("Книга", "Приключения", 500.0, 10)
        p2 = Product("Ручка", "Шариковая", 50.0, 100)
        Category("Канцелярия", "Товары для офиса", [p1, p2])

        assert Category.product_count == 2

    def test_empty_products_list(self):
        """Тест категории без товаров."""
        category = Category(
            "Пустая", "Без товаров", []
        )
        assert len(category.products) == 0
