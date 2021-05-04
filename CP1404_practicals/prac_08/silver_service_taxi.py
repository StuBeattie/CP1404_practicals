"""
Silver service taxi class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Create a silver service taxi class."""
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise the silver service taxi class."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string for silver service taxi."""
        return "{} plus flag_fall of ${:.2f}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Add flag_fall to get_fare"""
        return self.flag_fall + super().get_fare()
