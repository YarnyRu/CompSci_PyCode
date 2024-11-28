#Barcode checker - REQUIRES BARCODES.TXT
# Barcodes on left hand side should have an odd number of dark bars (1s) and
#  should start with a light bar (0), they should be 7 digits long
# Numbers on the right hand side should have an even number of dark bars and
#  should start with a dark bar (1), they should be 7 digits long
option = input("Would you like to check a barcode or make one? (check/make): ")
option = option.lower()
if option == "check":
  barcode = input("Please enter a barcode in its binary form: ")
  side = input ("Please enter R or L for right- or left-hand side code: ")
  side = side.upper()
  if side == "L":
    #barcode needs to start with a 0
    if barcode[0] == "0":
      print("LHS barcode starting digit correct")
    else:
      print("LHS barcode starting digit ERROR")
  elif side == "R":
      #barcode needs to start with a 1
    if barcode[0] == "1":
      print("RHS barcode starting digit correct")
    else:
      print("RHS barcode starting digit ERROR")
  else:
    print("You did not enter either L or R")
  #length should be 7 bits
  if len(barcode) ==7:
    print("Barcode is the correct length")
  else:
    print("Barcode length ERROR")
  darks = 0
  for digit in barcode:
    if digit == "1":
      darks +=1
  if side == "L":
    if darks%2 == 1:
      #odd number of dark bars is correct
      print("LHS = odd number of darks OK")
    else:
      print("LHS ERROR - even number of darks")
  if side == "R":
    if darks%2 == 0:
      #even number of dark bars is correct
      print("RHS = even number of darks OK")
    else:
      print("RHS ERROR - odd number of darks")
# OPTION 2 - Make a barcode from an entered digit
elif option == "make":
  number = input("Please enter a number to turn into a barcode: ")
  side = input ("Please enter R or L for right- or left-hand side code: ")
  side = side.upper()
  code_array = [""] * 26
  line_num = 0
  barcode = ""
  with open('barcodes.txt') as f:
    for line in f:
      temp_input = line.strip()
      code_array[line_num] = temp_input.split()
      line_num += 1
    # End of 'for line in f' loop  
  for digit in number:
    for nums in range (0, 10):
      if digit == code_array[nums][0]:
        if side == "L":
          barcode += code_array[nums][1] + " "
        elif side == "R":
          barcode += code_array[nums][2] + " "
  print(barcode)