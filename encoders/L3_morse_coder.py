# Turn a word into Morse code, or decode a Morse coded message
#Read in data from file
line_num = 0
code_array = [""] * 26
with open('codes.txt') as f:
  for line in f:
    temp_input = line.strip()
    code_array[line_num] = temp_input.split()
    line_num += 1
# End of 'for line in f' loop  
# Choose whether to code or decode
operation = input("Would you like to code or decode a word? ")
if operation == "code":
  Morse_code = ""
  word = input("Please enter word to convert: ")
  for letter in word:
    for alphabet in range (0, 26):
      if letter == code_array[alphabet][0]:
        Morse_code += code_array[alphabet][1] + " "
    if letter == " ":
      Morse_code += " / "
  print(Morse_code[:-1])
elif operation == "decode":
  #Ask for Morse code
  word = ""
  Morse = input("Please enter Morse code to decode using spaces to delimit: ")
  Morse_input = Morse.split()
  for letter in Morse_input:
    for code in range (0, 26):
      if letter == code_array[code][1]:
        word += code_array[code][0]
  print(word)
