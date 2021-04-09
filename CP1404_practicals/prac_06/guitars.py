"""List and store all the users guitars."""


from prac_06.guitar_type import GuitarInformation


def main():
    """Get, store, and display guitar information."""

    guitars = []

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

        guitars.append(GuitarInformation("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(GuitarInformation("Line 6 JTV-59", 2010, 1512.9))


if __name__ == "__main__":
    main()
