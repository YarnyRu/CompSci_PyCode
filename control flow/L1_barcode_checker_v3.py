barcode = input("Please enter a barcode in its binary form: ")
side = input ("Please enter R or L for right- or left-hand side code: ")
if side == "L":
  if barcode[0] == "0":
    print("LHS barcode starting digit correct")
  else:
    print("LHS barcode starting digit ERROR")
elif side == "R":
  if barcode[0] == "1":
    print("RHS barcode starting digit correct")
  else:
    print("RHS barcode starting digit ERROR")
else:
  print("You did not enter either L or R")
