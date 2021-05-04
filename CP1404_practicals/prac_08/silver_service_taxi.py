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
