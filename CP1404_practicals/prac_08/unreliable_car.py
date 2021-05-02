"""
Unreliable car class
"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Create an unreliable car class"""
    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel,)
        self.reliability = reliability



