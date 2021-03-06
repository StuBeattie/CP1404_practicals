"""Users email information"""


def main():
    """Store email and names in dictionary."""
    email_information = {}
    user_email = input("Please enter your email: ")
    # Check name in users email is correct. if not enter their name.
    while user_email != "":
        name = get_name_from_email(user_email)
        confirm_name = input(" Is your name {}? (Y/N): ".format(name)).upper()
        if confirm_name not in ("Y", ""):
            name = input("Please enter your name: ")
        email_information[user_email] = name
        user_email = input("Please enter your email: ")
    print(nice_display(email_information))


def get_name_from_email(user_email):
    """Split email and get users name."""
    split_email = user_email.split("@")[0]
    split_email_at_decimal = split_email.split(".")
    # Find users name in email address
    name = " ".join(split_email_at_decimal).title()
    return name


# align the emails so they are in one nice column
def nice_display(email_information):
    email_length = max(len(name) for name in email_information)
    for user_email, name in email_information.items():
        print("{:{}}{}".format(name, email_length, user_email))


main()
