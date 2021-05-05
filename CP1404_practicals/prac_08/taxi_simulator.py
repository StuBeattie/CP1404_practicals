"""
Create taxi simulator that utilizes
 Taxi and SilverServiceTaxi classes.
"""

from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Create a taxi simulator program that utilizes Taxi and SilverServiceTaxi classes.
    This program will loop through until the user quites."""
    print("Lets drive!")
    print(MENU)


main()
