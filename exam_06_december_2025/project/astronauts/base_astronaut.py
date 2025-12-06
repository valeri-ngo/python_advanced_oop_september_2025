from abc import ABC


class BaseAstronaut(ABC):
    STAMINA_PER_CALL = None
    MAX_STAMINA = None

    def __init__(self, id_number: str, salary: float, specialization: str, stamina: int):
        self.id_number: str = id_number
        self.salary: float = salary
        self.specialization: str = specialization
        self.stamina: int = stamina

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, value):
        if not value.strip().isdigit():
            raise ValueError('ID can contain only digits!')

        self.__id_number = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0.0:
            raise ValueError('Salary must be a positive number!')

        self.__salary = value

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        if value.strip() == "":
            raise ValueError('Specialization cannot be empty!')

        self.__specialization = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError('Stamina is out of range!')

        self.__stamina = value

    def train(self):
        self.stamina = min(self.stamina + self.STAMINA_PER_CALL, self.MAX_STAMINA)