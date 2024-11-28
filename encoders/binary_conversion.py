denary_number = int(input("Which number do you want to convert to binary? "))
binary_number = bin(denary_number)

reversed_binary = binary_number[:1:-1]
length = len(reversed_binary)
calculated_value = 0

for i in range(length):
    multiplier = pow(2, i)
    calculated_value += int(reversed_binary[i])*multiplier

print("The calculated value of", calculated_value, "should be the same as", binary_number)
