from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        required_fuel = kilometers * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel