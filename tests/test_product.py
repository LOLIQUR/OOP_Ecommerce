"""
Тесты для класса Product.
"""
import pytest

from src.product import Product


class TestProduct:
    """Тесты для товаров."""

    def test_product_creation(self):
        """Тест создания товара."""
        product = Product("Смартфон", "Современный смартфон", 50000.0, 10)
        assert product.name == "Смартфон"
        assert product.description == "Современный смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_price_type(self):
        """Тест типа цены (float)."""
        product = Product("Ноутбук", "Мощный ноутбук", 75000.50, 5)
        assert isinstance(product.price, float)

    def test_product_quantity_type(self):
        """Тест типа количества (int)."""
        product = Product("Наушники", "Беспроводные наушники", 5000.0, 15)
        assert isinstance(product.quantity, int)

    def test_log_mixin_output(self, capsys):
        """Тест вывода миксина в консоль."""
        Product("Телевизор", "4K", 50000, 10)  # убрали "product ="
        captured = capsys.readouterr()
        assert "Создан объект Product с параметрами:" in captured.out

    def test_base_product_abstract(self):
        """Тест что нельзя создать экземпляр BaseProduct."""
        from src.base_product import BaseProduct
        with pytest.raises(TypeError):
            BaseProduct()  # абстрактный класс нельзя инстанциировать
