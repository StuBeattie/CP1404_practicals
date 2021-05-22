"""
Create directory based on file extension type
and allow user to choose where the file is moved.
"""

import os
import shutil


def main():
    """Organise files into new folders based on their extension type."""
    category_type = {}

    # Change to desired folder
    os.chdir('FilesToSort')

    # Loop through each file in the (current) folder
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        # split and get extension type from list
        extension = filename.split(".")[-1]

        # Get users input of where they would like the file stored.
        if extension not in category_type:
            category = input("What category would you like to sort {} files into? ".format(extension))
            category_type[extension] = category

            # Conduct error checking to prevent crashing if folder already exist.
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        # Move file types to their correct folder.
        shutil.move(filename, "{}/{}".format(category_type[extension], filename))
        print("{}/{}".format(category_type[extension], filename))


main()
