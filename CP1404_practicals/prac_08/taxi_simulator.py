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

    taxi_types = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Lets drive!")
    print(MENU)

    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            taxis_available(taxi_types)
            taxi_choice = int(input("choose taxi: "))
            taxi_chosen = taxi_types[taxi_choice]
            taxis_available(taxi_types)
        elif menu_choice == "d":
            print("lets drive taxi")


def taxis_available(taxi_types):
    """Display taxis available with index for users to choose from"""
    for number, taxi in enumerate(taxi_types):
        print("{} - {}".format(number + 1, taxi))


main()
