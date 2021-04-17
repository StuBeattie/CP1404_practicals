"""Crate a class for guitars."""

import datetime
CURRENT_YEAR = datetime.date.today().year
VINTAGE = 50


class GuitarInformation:
    """Represent guitar information gathered from the user."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def display_guitar_info(self):
        """Display guitar information gathered from the user."""

        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Find the age of the guitar."""

        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Identify if the guitar is >= 50 years old."""

        return self.get_age() >= VINTAGE

    def __str__(self):
        """Display programing language in string format."""
        return "{:>13} ({}), worth ${:10,.2f}".format(self.name, self.year, self.cost)
