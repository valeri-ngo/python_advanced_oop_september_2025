from abc import ABC, abstractmethod


class BaseBattleship(ABC):

    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name: str = name
        self.health: int = health
        self.hit_strength: int = hit_strength
        self.ammunition: int = ammunition
        self.is_attacking = False
        self.is_available = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError('Ship name must contain only letters!')
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, value)

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, enemy_battleship: 'BaseBattleship'):
        self.health -= enemy_battleship.hit_strength
