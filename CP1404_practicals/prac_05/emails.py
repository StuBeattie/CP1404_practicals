"""Users email information"""

email_information = {}
# Get email address and split into parts
user_email = input("Please enter your email: ")
while user_email != "":
    get_name_from_email = user_email.split("@")[0]
    split_email = get_name_from_email.split(".")

    # Find users name in email address
    name = "".join(split_email).title()
    print(" Is your name", name, "(Y/N)")

    # confirm users name is correct. If not, enter their name
    confirm_name = input("-->: ").upper()
    if confirm_name != "Y" and confirm_name != "":
        name = input("Please enter your name: ")

    # store name in directory(email_information) then display information neatly
    email_information[user_email] = name
    user_email = input("Please enter your email: ")

# Display users names and email address neatly
for user_email, name in email_information.items():
    print("{} --> ({})".format(name, user_email))
