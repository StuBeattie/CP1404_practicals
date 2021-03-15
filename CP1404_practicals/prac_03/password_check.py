""" Get users password of a minimum length and print asterisks for each character """

# Set passwords minimum length
MINIMUM_LENGTH = 5


def version_1():
    """Get users password and print asterisks"""
    password = input("Please enter a valid password with a minimum of {}  characters: ".format(MINIMUM_LENGTH))
    # Error checking if password is out side the parameters
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password!")
        password = input("Please enter a valid password with a minimum of {}  characters: ".format(MINIMUM_LENGTH))

    print('*' * len(password))


def main():
    """Get users password using functions"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    # Ensure password meets the minimum requirements
    password = input("Please enter a valid password with a minimum of {}  characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Invalid password!")
        password = input("Please enter a valid password with a minimum of {}  characters: ".format(minimum_length))
    return password


def print_asterisks(characters):
    """Print asterisks for every character in the password"""
    print('*' * len(characters))


main()
