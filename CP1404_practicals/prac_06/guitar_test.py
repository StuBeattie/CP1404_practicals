"""Testing of guitar program."""


from prac_06.guitar_type import GuitarInformation


def test():
    """Run test on guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = GuitarInformation(name, year, cost)
    other = GuitarInformation("Another Guitar", 2013, 1999.99)
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 99, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 8, other.get_age()))


if __name__ == "__main__":
    test()
