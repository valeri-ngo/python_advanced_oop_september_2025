from abc import ABC, abstractmethod

class BaseBattleship(ABC):
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name: str = name
        self.health: int = health
        self.hit_strength: int = hit_strength
        self.ammunition: int = ammunition
        self.is_attacking: bool = False
        self.is_available: bool = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Ship name must contain only letters!')
        self._name = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        value = int(value)

        if value < 0:
            self._health = 0
        else:
            self._health = value

    def take_damage(self, enemy_battleship: 'BaseBattleship'):
        damage = int(getattr(enemy_battleship, 'hit_strength', 0))
        self.health -= damage
        if self.health <= 0:
            self.is_available = False

    @abstractmethod
    def attack(self):
        pass

    def get_ships(self):
        pass