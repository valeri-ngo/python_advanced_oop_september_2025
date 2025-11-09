from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, liters: int) -> None:
        pass

class Car(Vehicle):
    CONSUMPTION_PER_KM = 0.9

    def drive(self, distance: int) -> None:
        fuel_needed = distance * (self.fuel_consumption + self.CONSUMPTION_PER_KM)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, liters: int) -> None:
        self.fuel_quantity += liters


class Truck(Vehicle):
    CONSUMPTION_PER_KM = 1.6
    TANK_CAPACITY = 0.95

    def drive(self, distance: int) -> None:
        fuel_needed = distance * (self.fuel_consumption + self.CONSUMPTION_PER_KM)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, liters: int) -> None:
        self.fuel_quantity += liters * self.TANK_CAPACITY


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print()
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)