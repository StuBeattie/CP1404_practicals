"""
Test the unreliable car class.
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test unreliable cars."""
    old_car = UnreliableCar("Old school", 100, 50)

    # Test drive car multiple times over a specified distance and compare the old_car distance
    for kilometers in range(1, 11):
        print("Tried driving {}km, but the {} car actually drove {}km."
              .format(kilometers, old_car.name, old_car.drive(kilometers)))


main()
