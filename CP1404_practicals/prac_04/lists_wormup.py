"""Change and get elements in list"""

# numbers = [3, 1, 4, 1, 5, 9, 2]
# What values do the following expressions have?
# (solutions not provided; figure it out, then run with print or in console to test)
# numbers[0]    = 3
# numbers[-1]   = 2
# numbers[3]    = 1
# numbers[:-1]  = would remove last element
# numbers[3:4]  = 1
# 5 in numbers  = True
# 7 in numbers  = False
# "3" in numbers = False
# numbers + [6, 5, 3] = ads these elements on to numbers



numbers = [3, 1, 4, 1, 5, 9, 2]
# Change the first element to the string "ten".
numbers[0] = "ten"
print(numbers)
print()

# Change last element to 1
numbers[-1] = 1
print(numbers)
print()

# get all elements except first two
numbers[-1] = 2  # Change back to original number
print(numbers[2:])
print()

# Check if 9 is an element of numbers
print(9 in numbers)
