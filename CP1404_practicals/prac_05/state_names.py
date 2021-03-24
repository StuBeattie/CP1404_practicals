"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

# Display states code and names neatly lined up
for code in CODE_TO_NAME:
    print(code, "is", CODE_TO_NAME[code])
print()

# use while loop to iterate through CODE_TO_NAME and change any lower case inputs to upper case
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state!")
    state_code = input("Enter short state: ").upper()
