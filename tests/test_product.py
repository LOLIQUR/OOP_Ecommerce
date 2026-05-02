"""
Тесты для класса Product.
"""
from src.product import Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_creation(self):
        product = Product("Ноутбук", "Мощный ноутбук", 50000, 10)
        assert product.name == "Ноутбук"
        assert product.description == "Мощный ноутбук"
        assert product._Product__price == 50000
        assert product.quantity == 10

    def test_product_price_type(self):
        product = Product("Ноутбук", "Мощный", 50000.5, 10)
        assert isinstance(product._Product__price, float)

    def test_product_quantity_type(self):
        product = Product("Ноутбук", "Мощный", 50000, 10)
        assert isinstance(product.quantity, int)

    def test_new_product_classmethod(self):
        data = {
            "name": "Смартфон",
            "description": "Современный смартфон",
            "price": 30000,
            "quantity": 5
        }
        product = Product.new_product(data)
        assert product.name == "Смартфон"
        assert product.description == "Современный смартфон"
        assert product._Product__price == 30000
        assert product.quantity == 5

    def test_price_getter(self):
        product = Product("Ноутбук", "Мощный", 50000, 10)
        assert product.price == 50000

    def test_price_setter_positive(self):
        product = Product("Ноутбук", "Мощный", 50000, 10)
        product.price = 60000
        assert product.price == 60000

    def test_price_setter_invalid(self, capsys):
        product = Product("Ноутбук", "Мощный", 50000, 10)
        product.price = -1000
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 50000

    def test_product_str(self):
        product = Product("Ноутбук", "Мощный ноутбук", 50000, 10)
        expected = "Ноутбук, 50000 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_add(self):
        product1 = Product("Ноутбук", "Мощный", 50000, 10)
        product2 = Product("Мышь", "Беспроводная", 1500, 25)
        total = product1 + product2
        assert total == 50000 * 10 + 1500 * 25
