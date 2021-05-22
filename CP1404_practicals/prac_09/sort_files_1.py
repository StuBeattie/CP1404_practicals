"""
Create specified directories for
each extension type found in directory.
"""

import os
import shutil


def main():
    """Organise files into new folders based on their extension type."""
    # Change to desired folder
    os.chdir('FilesToSort')

    # Loop through each file in the (current) folder
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        # split and get extension type from list
        extension = filename.split(".")[1]

        # Conduct error checking to prevent crashing if folder already exist.
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        # Move file types to their correct folder.
        shutil.move(filename, "{}/{}".format(extension, filename))
        print("{}/{}".format(extension, filename))


main()
