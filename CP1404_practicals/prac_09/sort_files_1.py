"""
Create specified directories for
each extension type found in directory.
"""

import os


def main():
    """Organise files into new folders based on their extension type."""
    # Change to desired directory
    os.chdir('FilesToSort')

    # Loop through each file in the (current) directory
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        extension = filename.split(".")
        print(extension)


main()
