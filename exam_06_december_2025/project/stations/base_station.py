from abc import ABC

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    INCREASE_SALARY = None
    TARGET_SPEC = None

    def __init__(self, name: str, capacity: int):
        self.name: str = name
        self.capacity: int = capacity
        self.astronauts: list[BaseAstronaut] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        is_valid = all(ch.isalnum() or ch == '-' for ch in value)
        if not is_valid:
            raise ValueError('Station names can contain only letters, numbers, and hyphens!')

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not 0 <= value:
            raise ValueError('A station cannot have a negative capacity!')

        self.__capacity = value

    def calculate_total_salaries(self):
        total_salaries = sum(a.salary for a in self.astronauts)
        return f"{total_salaries:.2f}"

    def status(self):
        sorted_astronauts = sorted(a.id_number for a in self.astronauts)
        astro_str = " #".join(sorted_astronauts) if sorted_astronauts else "N/A"
        total_salaries = self.calculate_total_salaries()

        return (
            f"Station name: {self.name}; "
            f"Astronauts: {astro_str}; "
            f"Total salaries: {total_salaries}"
        )

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if a.specialization == self.TARGET_SPEC and a.salary <= min_value:
                a.salary += self.INCREASE_SALARY



