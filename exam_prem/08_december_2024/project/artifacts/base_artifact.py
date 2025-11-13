from abc import ABC, abstractmethod


class BaseArtifact(ABC):

    def __init__(self, name: str, price: float, space_required: int):
        self.name: str = name
        self.price: float = price
        self.space_required: int = space_required


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.strip() == '':
            raise ValueError('Artifact name cannot be null or empty!')
        self._name = value


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError('Artifact price should be more than 0.0!')
        self._price = value


    @property
    def space_required(self):
        return self._space_required

    @space_required.setter
    def space_required(self, value):
        if value < 1 or value > 1000:
            raise ValueError('Space required for the artifact exhibition must be between 1 and 1000!')
        self._space_required = value


    @abstractmethod
    def artifact_information(self):
        pass