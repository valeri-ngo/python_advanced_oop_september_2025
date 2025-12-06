from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540
    PENALTY_PERCENTAGE = 0.3

    def __init__(self, name: str):
        super().__init__(name, self.OXYGEN_LEVEL)
