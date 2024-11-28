#Barcode checker
# Numbers on left hand side should have an odd number of dark bars (1s) and
#  should start with a light bar (0)
# Numbers on the right hand side should have an even number of dark bars and
#  should start with a dark bar (1)

barcode = [0, 1, 1, 0, 0, 0, 1]
LHS_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', 
             '0101111', '0111011', '0110111', '0001011']

RHS_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110',
             '1010000', '1000100', '1001000', '1110100']

#LHS barcode needs to start with a 0
if barcode[0] == 0:
  print("LHS barcode starting digit correct")
elif barcode[0] == 1:
  print("RHS barcode starting digit correct")
else:
  print("Barcode starting digit ERROR")

#length should be 7 bits
if len(barcode) == 7:
  print("Barcode is the correct length")
else:
  print("Barcode length ERROR")
