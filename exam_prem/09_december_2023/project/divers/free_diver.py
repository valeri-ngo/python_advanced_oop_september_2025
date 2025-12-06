from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120
    PENALTY_PERCENTAGE = 0.6

    def __init__(self, name: str):
        super().__init__(name, self.OXYGEN_LEVEL)
