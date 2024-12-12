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
print(code_array)