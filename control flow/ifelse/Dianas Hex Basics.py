#Denary to Hex Converter
# Python complexity - MEDIUM
# Maths complexity - HIGH
# Number of lines of Python code (without comments) - 12

# Set up data array
HexDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Ask for user input
user_number = int(input("Please enter a number between 0 and 255 to convert to hex: "))

# Validation, is the number input within the correct range?
if user_number < 0:
    # Ignore negative numbers
    print("I can't do negative numbers!")
elif user_number < 16:
    # This means user_number is between 0 and 15
    print("Your number is", HexDigits[user_number],"in hex")
elif user_number < 256:
    # This means user_number is between 16 and 255
    # First digit can be calculated using integer division. Divide by 16 to see how many times 16 goes into user_number
    first_digit = HexDigits[user_number // 16]
    # Second digit can be calculated by finding the remainder after integer division.
    # This is done using modulo arithmetic, which calculates the units column and ignores all other digits in larger columns
    second_digit = HexDigits[user_number % 16]
    # Turn the numbers into a string for printing
    print("Your number is", str(first_digit) + str(second_digit), "in hex")

else:
    # This means the number is bigger than 256 so we'd need 3 or more hex digits to represent it. Ignore this number.
    print("Too BIG!")
    
