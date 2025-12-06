from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    OXYGEN_LEVEL = None
    PENALTY_PERCENTAGE = None

    @abstractmethod
    def __init__(self, name: str, oxygen_level: float):
        self.name: str = name
        self.oxygen_level: float = oxygen_level
        self.catch: list[BaseFish] = []
        self.competition_points: float = 0.0
        self.has_health_issue: bool = False
        self.missed_fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError('Diver name cannot be null or empty!')
        
        self.__name = value
        
    @property
    def oxygen_level(self):
        return self.__oxygen_level
    
    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError('Cannot create diver with negative oxygen level!')

        self.__oxygen_level = value

    @property
    def competition_points(self):
        return round(self.__competition_points, 1)

    @competition_points.setter
    def competition_points(self, value: float):
        self.__competition_points = value

    def miss(self, time_to_catch: int):
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
            return

        penalty = round(time_to_catch * self.PENALTY_PERCENTAGE)
        self.oxygen_level = max(0, self.oxygen_level - penalty)

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL

    def hit(self, fish: BaseFish):
        if (self.oxygen_level - fish.time_to_catch) < 0:
            self.oxygen_level = 0
            self.missed_fish.append(fish)
            return

        self.oxygen_level -= fish.time_to_catch
        self.catch.append(fish)
        self.competition_points += fish.points

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f"{self.__class__.__name__}: "
                f"[Name: {self.name}, Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]")
