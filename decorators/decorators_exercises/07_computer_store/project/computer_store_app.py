from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    VALID_TYPES: dict[str, type[Computer]] = {
        'Desktop Computer': DesktopComputer,
        'Laptop': Laptop
    }

    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f'{type_computer} is not a valid type computer!')

        computer = self.VALID_TYPES[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        computer = next((c for c in self.warehouse
                         if c.price <= client_budget
                         and c.processor == wanted_processor
                         and c.ram >= wanted_ram), None)

        if computer is None:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f'{repr(computer)} sold for {client_budget}$.'