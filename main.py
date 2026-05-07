from src.product import Product, Smartphone, LawnGrass
from src.category import Category

if __name__ == '__main__':
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание смартфонов
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    # Создание травы
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    # Вывод информации
    print("\n=== Смартфоны ===")
    print(smartphone1)
    print(smartphone2)
    print(smartphone3)

    print("\n=== Газонная трава ===")
    print(grass1)
    print(grass2)

    # Сложение
    print("\n=== Сложение товаров одного класса ===")
    print(f"Сумма смартфонов: {smartphone1 + smartphone2} руб.")
    print(f"Сумма травы: {grass1 + grass2} руб.")

    # Попытка сложить разные классы
    print("\n=== Попытка сложить смартфон и траву ===")
    try:
        result = smartphone1 + grass1
        print(f"Результат: {result}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Категории
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    # Добавление продукта в категорию
    category_smartphones.add_product(smartphone3)

    print("\n=== Все смартфоны в категории ===")
    print(category_smartphones.products)

    print(f"\nОбщее количество продуктов: {Category.product_count}")
