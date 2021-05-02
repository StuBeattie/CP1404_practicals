"""
Unreliable car class
"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Create an unreliable car class."""
    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel,)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only when it is reliable."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
