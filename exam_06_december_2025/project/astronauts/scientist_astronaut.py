from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    SPECIALIZATION = 'ScientistAstronaut'
    STAMINA = 70
    STAMINA_PER_CALL = 3
    MAX_STAMINA = 100

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.STAMINA)