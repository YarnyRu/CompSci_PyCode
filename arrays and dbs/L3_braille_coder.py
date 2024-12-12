# Turn a word into Braille binary representation, or decode a binary-encoded Braille message
#Read in data from file
line_num = 0
code_array = [""] * 26
with open('braillecodes.txt') as f:
  for line in f:
    temp_input = line.strip()
    code_array[line_num] = temp_input.split()
    line_num += 1
# End of 'for line in f' loop  
# Choose whether to code or decode
operation = input("Would you like to code or decode a word? ")
if operation == "code":
  codeword = ""
  word = input("Please enter word to convert: ")
  word = word.upper()
  for letter in word:
    for alphabet in range (0, 26):
      if letter == code_array[alphabet][0]:
        codeword += code_array[alphabet][1] + " "
    if letter == " ":
      codeword += " / "
  print(codeword[:-1])
elif operation == "decode":
  #Ask for binary-encoded Braille
  codeword = ""
  Braille = input("Please enter Braille binary code to decode using spaces to delimit: ")
  Braille_input = Braille.split()
  for letter in Braille_input:
    for code in range (0, 26):
      if letter == code_array[code][1]:
        codeword += code_array[code][0]
  print(codeword)
