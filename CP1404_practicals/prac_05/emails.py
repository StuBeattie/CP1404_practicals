"""Users email information"""

email_information = {}
user_email = input("Please enter your email: ")
get_name_from_email = user_email.split("@")[0]
split_email = get_name_from_email.split(".")

# Split email and find users name
name = "".join(split_email).title()
print(" Is your name", name, "(Y/N)")

# confirm users name is correct. If not enter their real name
confirm_name = input("-->: ").upper()

