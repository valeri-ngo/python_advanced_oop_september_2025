from project.tiger import Tiger
from project.lion import Lion
from project.cheetah import Cheetah
from project.vet import Vet
from project.caretaker import Caretaker
from project.keeper import Keeper


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return f"Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if worker_name == w.name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salary = sum(w.salary for w in self.workers)
        if self.__budget >= sum_salary:
            self.__budget -= sum_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_money_care = sum(a.money_for_care for a in self.animals)
        if self.__budget >= sum_money_care:
            self.__budget -= sum_money_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount
        return self.__budget

    def animals_status(self):
        lions = [l for l in self.animals if isinstance(l, Lion)]
        tigers = [t for t in self.animals if isinstance(t, Tiger)]
        cheetahs = [ch for ch in self.animals if isinstance(ch, Cheetah)]

        result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        result.extend(repr(l) for l in lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(repr(t) for t in tigers)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(repr(ch) for ch in cheetahs)
        return "\n".join(result)

    def workers_status(self):
        keepers = [k for k in self.workers if isinstance(k, Keeper)]
        caretakers = [ct for ct in self.workers if isinstance(ct, Caretaker)]
        vets = [v for v in self.workers if isinstance(v, Vet)]

        result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        result.extend(repr(k) for k in keepers)
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(repr(ct) for ct in caretakers)
        result.append(f"----- {len(vets)} Vets:")
        result.extend(repr(v) for v in vets)
        return "\n".join(result)
