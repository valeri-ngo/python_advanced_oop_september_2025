from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    INITIAL_CAPACITY = 5
    INCREASE_SALARY = 5000.0
    TARGET_SPEC = 'ScientistAstronaut'

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)
