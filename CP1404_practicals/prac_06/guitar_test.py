"""Testing of guitar program."""


from prac_06.guitar_type import GuitarInformation


def test():
    """Run test on guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    # Test to find out if the get_age function is displaying the correct information.
    guitar = GuitarInformation(name, year, cost)
    other = GuitarInformation("Another Guitar", 2013, 1999.99)
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 99, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 8, other.get_age()))

    # Test to find out if the is_vintage function is displaying the correct information.
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, "True", guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, "False", other.is_vintage()))


if __name__ != "__main__":
    test()
