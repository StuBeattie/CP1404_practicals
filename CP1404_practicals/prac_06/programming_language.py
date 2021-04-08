"""Identify which programming languages are dynamic."""


class ProgrammingLanguage:
    """Represent a programing language."""

    def __init__(self, language_name, typing, reflection, year):
        """Initialise table instance."""

        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Confirm which language is dynamically typed."""

        return self.typing == "Dynamic"

    def __str__(self):
        """Display programing language in string format."""

        return "{}, {} Typing, Reflection={}," \
               " First appeared in {}".format(self.language_name, self.typing, self.reflection, self.year)
