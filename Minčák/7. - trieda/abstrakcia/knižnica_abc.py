from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Šoféruješ auto")

class Motocycle(Vehicle):
    def go(self):
        print("Šoféruješ motorku")

vehicle = Vehicle()
car = Car()
