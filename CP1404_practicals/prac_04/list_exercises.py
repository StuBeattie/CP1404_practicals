"""more practice with lists"""

# 1. Basic list operations
numbers = []
print("Please enter 5 numbers.")

# Get 5 random numbers from user and display various information.
for n in range(5):
    number = int(input("Number {}: ".format(n + 1)))
    numbers.append(number)
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))
print()


# 2. Woefully inadequate security checker.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
