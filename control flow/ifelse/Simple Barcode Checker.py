#Barcode checker
# Numbers on left hand side should have an odd number of dark bars (1s) and
#  should start with a light bar (0)
# Numbers on the right hand side should have an even number of dark bars and
#  should start with a dark bar (1)
# Check that 7 bits have been entered
# Input should be in the format 0110010

barcode = input("Please enter a barcode in its binary form, for example 0110001: ")
# Length Check
length = len(barcode)
print(length)
if length == 7:
  # Length is OK
  print("Barcode passed the length check")
  # Now it needs to pass the FORMAT CHECK
  if barcode[0] == "0":
    # OK for LHS barcode
    print("Barcode is a valid left hand side code")
  else:
    # Not a valid LHS code
    print("Error - not a valid left hand side code")
else:
  # Length is not OK
  print("Error - barcode is the incorrect length")
