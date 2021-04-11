"""List and store all the users guitars."""


from prac_06.guitar_type import GuitarInformation


def main():
    """Get, store, and display guitar information."""

    guitars = []

    # Get users to input guitar information and print to screen
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("cost: "))
        add_input_to_guitars = GuitarInformation(name, year, cost)
        guitars.append(add_input_to_guitars)
        print("{} ({}) : ${} added.".format(name, year, cost))
        print()
        name = input("Name: ")

    # Add extra guitars to guitars list for testing.
    guitars.append(GuitarInformation("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(GuitarInformation("Line 6 JTV-59", 2010, 1512.90))

    # Display all users guitars neatly.
    print()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}"
              .format(i, guitar.name, guitar.year, guitar.cost, vintage_string))


main()
