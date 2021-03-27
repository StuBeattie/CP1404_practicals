"""Hexadecimal colour coder program"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

# print a list of colour names
for name in COLOUR_CODES:
    print(name)
print()

# ask the user to input a colour then display colour and code
colour = input("Please enter a colour: ")
while colour != "":
    if colour in COLOUR_CODES:
        print("The code for {} is: {}".format(colour, COLOUR_CODES[colour]))
    else:
        print("Invalid colour name!")
    colour = input("Please enter a colour: ")
