"""Identify which programming languages are dynamic."""


class ProgrammingLanguage:
    """Represent a programing language."""

    def __init__(self, field="", typing="", reflection="", year=0):
        """Initialise table instance."""

        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year
