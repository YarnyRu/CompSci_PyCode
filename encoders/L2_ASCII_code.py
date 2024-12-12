# ASCII code converter
# This program can repeatedly convert an ASCII code (number) into its character symbol
# It is easily adapted to turn characters into their denary ASCII code using the ord() function instead of chr()

carry_on = True
while carry_on == True:
  # Everything that happens within this loop is indented like this
  ASCII_code = int(input("Please enter an ASCII code: "))
  if ASCII_code < 0:
    print("Error")
  else:
    print(chr(ASCII_code))
  # Now ask user if they would like to continue
  cont = input("Would you like to continue? Y/N ")
  if cont.upper() == 'Y':
    carry_on = True
  elif cont.upper() == 'N':
    carry_on = False
    print("Thanks for using my program")
  else:
    print("Error")