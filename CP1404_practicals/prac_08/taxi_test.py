"""
Test new taxi class.
"""

from prac_08.taxi import Taxi


def main():
    """ test taxi class"""
    taxi_cab = Taxi("Prius 1", 100, 1.23)
    taxi_cab.drive(40)
    print(taxi_cab)
    taxi_cab.start_fare()
    taxi_cab.drive(100)
    print(taxi_cab)


main()
