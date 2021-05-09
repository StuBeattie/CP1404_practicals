"""
Create specified directories for
each extension type found in directory.
"""

import os
import shutil


def main():
    """Organise files into new folders based on their extension type."""
    # Change to desired directory
    os.chdir('FilesToSort')

    # Loop through each file in the (current) directory
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        # split and get extension type from list
        extension = filename.split(".")[1]

        # Conduct error checking for directories that already exist.
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        # Move file types to their correct directory.
        shutil.move(filename, "{}/{}".format(extension, filename))
        print("{}/{}".format(extension, filename))


main()
