"""
Test new taxi class.
"""

from prac_08.taxi import Taxi


def main():
    """ test taxi class by displaying information."""
    # enter name of taxi and units of fuel: Taxi("name", fuel)
    taxi_cab = Taxi("Prius 1", 100)
    # enter distance in km
    taxi_cab.drive(40)
    print(taxi_cab)
    taxi_cab.start_fare()
    taxi_cab.drive(100)
    print(taxi_cab)


main()
