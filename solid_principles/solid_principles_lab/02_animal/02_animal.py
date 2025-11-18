from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'

class Snake(Animal):
    def make_sound(self):
        return 'hiss-hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Snake()]
animal_sound(animals)
