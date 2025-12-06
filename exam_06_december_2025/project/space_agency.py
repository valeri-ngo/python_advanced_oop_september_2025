from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    ASTRONAUT_TYPES = {
        'EngineerAstronaut': EngineerAstronaut,
        'ScientistAstronaut': ScientistAstronaut
    }

    STATION_TYPES = {
        'ResearchStation': ResearchStation,
        'MaintenanceStation': MaintenanceStation
    }

    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        astronaut = next((a for a in self.astronauts if a.id_number == astronaut_id_number), None)

        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise ValueError('Invalid astronaut type!')

        if astronaut:
            raise ValueError(f'{astronaut_id_number} has been already added!')

        new_astronaut = self.ASTRONAUT_TYPES[astronaut_type](astronaut_id_number, astronaut_salary)
        self.astronauts.append(new_astronaut)

        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        station = next((s for s in self.stations if s.name == station_name), None)

        if station_type not in self.STATION_TYPES:
            raise ValueError('Invalid station type!')

        if station:
            raise ValueError(f'{station_name} has been already added!')

        new_station = self.STATION_TYPES[station_type](station_name)
        self.stations.append(new_station)

        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self,station_name: str, astronaut_type: str):
        station = next((s for s in self.stations if s.name == station_name), None)
        astronaut = next((a for a in self.astronauts if a.specialization == astronaut_type), None)

        if not station:
            raise ValueError(f'Station {station_name} does not exist!')

        if not astronaut:
            raise ValueError('No available astronauts of the type!')

        if station.capacity <= 0:
            return 'This station has no available capacity.'

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()

        astronaut_stamina = sum(a.stamina for a in station.astronauts)

        return (f"{station.name} astronauts have {astronaut_stamina} total stamina after"
                f" {sessions_number} "
                f"training "
                f"session/s.")

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)

        if astronaut is None or astronaut.stamina == astronaut.MAX_STAMINA:
            return 'The retirement process was canceled.'

        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        available_astros = len(self.astronauts)
        station_count = len(self.stations)
        total_available_capacity = sum(s.capacity for s in self.stations)

        sorted_stations = sorted(self.stations, key= lambda s: (-len(s.astronauts), s.name))

        result = ['*Space Agency Up-to-Date Report*']
        result.append(f"Total number of available astronauts: {available_astros}")
        result.append(f"**Stations count: {station_count}; Total available capacity: {total_available_capacity}**")

        for station in sorted_stations:
            result.append(station.status())

        return "\n".join(result)
