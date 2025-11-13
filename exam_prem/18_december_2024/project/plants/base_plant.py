from abc import ABC, abstractmethod


class BasePlant(ABC):
    def __init__(self, name: str, price: float, water_needed: int):
        self.name: str = name
        self.price: float = price
        self.water_needed: int = water_needed

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        if not value.strip():
            raise ValueError('Plant name cannot be null or empty!')
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        if value <= 0.0:
            raise ValueError('Price must be greater than zero!')
        self._price = value


    @property
    def water_needed(self) -> int:
        return self._water_needed

    @water_needed.setter
    def water_needed(self, value) -> None:
        if value < 1 or value > 2000:
            raise ValueError('Water needed must be between 1 and 2000 ml!')
        self._water_needed = value

    @abstractmethod
    def plant_details(self) -> str:
        pass