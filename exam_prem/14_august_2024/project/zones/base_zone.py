from abc import ABC, abstractmethod
from typing import List

from battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code: str = code
        self.volume: int = volume
        self.ships: List[BaseBattleship] = []


    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not isinstance(value, str) or not value.isdigit():
            raise ValueError('Zone code must contain digits only!')
        self._code = value


    @abstractmethod
    def zone_info(self):
        pass


    def get_ships(self):
        battleships_sorted = sorted(self.ships, key= lambda x: (-x.hit_strength, x.name))
        return battleships_sorted