"""
Тесты для класса Product и его наследников.
"""
import pytest

from src.product import LawnGrass, Product, Smartphone


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

    def test_product_zero_quantity(self):
        """Тест создания продукта с нулевым количеством."""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Пустой", "Описание", 100, 0)

    def test_smartphone_creation(self):
        """Тест создания смартфона."""
        phone = Smartphone("Samsung", "Флагман", 180000, 5, "Высокая", "S23 Ultra", 256, "Серый")
        assert phone.name == "Samsung"
        assert phone.efficiency == "Высокая"
        assert phone.model == "S23 Ultra"
        assert phone.memory == 256
        assert phone.color == "Серый"

    def test_lawn_grass_creation(self):
        """Тест создания травы."""
        grass = LawnGrass("Газон", "Быстрый рост", 1500, 100, "Россия", "7-10 дней", "Зелёный")
        assert grass.name == "Газон"
        assert grass.country == "Россия"
        assert grass.germination_period == "7-10 дней"
        assert grass.color == "Зелёный"

    def test_add_different_types_error(self):
        """Тест сложения разных классов (должна быть ошибка)."""
        phone = Smartphone("Samsung", "Флагман", 180000, 5, "Высокая", "S23 Ultra", 256, "Серый")
        grass = LawnGrass("Газон", "Быстрый рост", 1500, 100, "Россия", "7-10 дней", "Зелёный")
        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            _ = phone + grass

    def test_log_mixin_output(self, capsys):
        """Тест вывода миксина в консоль."""
        Product("Телевизор", "4K", 50000, 10)
        captured = capsys.readouterr()
        assert "Создан объект Product с параметрами:" in captured.out

    def test_base_product_abstract(self):
        """Тест что нельзя создать экземпляр BaseProduct."""
        from src.product import BaseProduct
        with pytest.raises(TypeError):
            BaseProduct()
