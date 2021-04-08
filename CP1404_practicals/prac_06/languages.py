"""Identify which languages are dynamic."""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """display which language is dynamic."""

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
