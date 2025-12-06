from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    SPECIALIZATION = 'EngineerAstronaut'
    STAMINA = 80
    STAMINA_PER_CALL = 5
    MAX_STAMINA = 100

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.STAMINA)

