from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        required_fuel = kilometers * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel