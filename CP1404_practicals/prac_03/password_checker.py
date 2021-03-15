""" Password with error-checking """

MIN_LENGTH = 3
MAX_LENGTH = 6

# Get users password
print("Please enter a valid password")
print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH)
password = input("> ")

while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
    print("Invalid password!")
    password = input("> ")

for i, password in enumerate(password):
    print('*', end=' ')