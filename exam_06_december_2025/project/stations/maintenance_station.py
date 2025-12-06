from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    INITIAL_CAPACITY = 3
    INCREASE_SALARY = 3000.0
    TARGET_SPEC = 'EngineerAstronaut'

    def __init__(self, name):
        super().__init__(name, self.INITIAL_CAPACITY)
