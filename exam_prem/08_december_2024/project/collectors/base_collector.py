# python
import re
from abc import ABC, abstractmethod

class BaseCollector(ABC):
    NAME_PATTERN = re.compile(r'^[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$')

    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip() or not self.NAME_PATTERN.match(value):
            raise ValueError('Collector name must contain letters, numbers, and optional white spaces between them!')
        self._name = value


    @property
    def available_money(self):
        return self._available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0.0:
            raise ValueError('A collector cannot have a negative amount of money!')
        self._available_money = float(value)

    @property
    def available_space(self):
        return self._available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError('A collector cannot have a negative space available for exhibitions!')
        self._available_space = int(value)

    @abstractmethod
    def increase_money(self) -> None:
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        return (self.available_money >= artifact_price) and (self.available_space >= artifact_space_required)

    def __str__(self):
        names = [a.name if hasattr(a, "name") else a for a in self.purchased_artifacts]
        names = sorted(names, reverse=True)
        artifacts = ", ".join(names) if names else 'none'

        return (f'Collector name: {self.name}; '
                f'Money available: {self.available_money:.2f}; '
                f'Space available: {self.available_space}; '
                f'Artifacts: {artifacts}')