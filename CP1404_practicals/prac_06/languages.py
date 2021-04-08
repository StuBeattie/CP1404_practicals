"""Identify which languages are dynamic."""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """display which language is dynamic."""

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the object and see if the __str__ function is working.
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.language_name)


main()
