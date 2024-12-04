# Start program to convert denary to binary
print("Welcome to my number converter!")
print('''Please enter your conversion option
      Option 1: Denary to Binary
      Option 2: Binary to Denary''')
# INPUT conversion option
conversion = int(input("Option: "))

# Denary to Binary
if conversion == 1:
  denary_number = int(input("Please enter denary number (1 to 255): "))
  binary_digits = [128, 64, 32, 16, 8, 4, 2, 1]
  binary_number = ""
  if denary_number < 1 or denary_number > 255:
      print("Out of range")
  else:
    for b in binary_digits:
      if denary_number >= b:
          binary_number += "1"
          denary_number -= b
      else:
          binary_number += "0"
    print(binary_number)
    
# Binary to Denary
elif conversion == 2:
  binary_number = input("Please enter binary number: ")
  # Reverse binary digits
  binary_number = binary_number[::-1]
  decimal_number = 0  
  for i in range(len(binary_number)):    
    digit = int(binary_number[i])  
    power = 2 ** i  
    result = digit * power  
    decimal_number += result
  print(decimal_number)
  
else:
  print("That was not one of the options!")