"""Quick pick lottery ticket generator."""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    """Choose random numbers."""
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("Error, must be positive integer!")
        quick_picks = int(input("How many quick picks? "))
    # Loop through random numbers in ranges specified above.
    # Sort numbers in ascending order
    for i in range(quick_picks):
        quick_pick = []
        for n in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
