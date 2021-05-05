"""
Create taxi simulator that utilizes
 Taxi and SilverServiceTaxi classes.
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Create a taxi simulator program that utilizes Taxi and SilverServiceTaxi classes.
    This program will loop through until the user quites."""
    total_cost = 0
    taxi_types = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Lets drive!")
    print(MENU)

    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            taxis_available(taxi_types)
            taxi_choice = int(input("choose taxi: "))
            try:
                current_taxi = taxi_types[taxi_choice]
            except IndexError:
                print("Invalid choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                driving_distance = float(input("Drive how far? "))
                current_taxi.drive(driving_distance)
                cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost))
                total_cost += cost
            else:
                print("you need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Bill to date: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    taxis_available(taxi_types)


def taxis_available(taxi_types):
    """Display taxis available with index for users to choose from"""
    for number, taxi in enumerate(taxi_types):
        print("{} - {}".format(number, taxi))


main()
