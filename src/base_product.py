"""
Модуль с абстрактным базовым классом BaseProduct.
"""
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение продуктов."""
        pass
