# Print Highest
# INPUT num1, num2, num3
# highest <- num1
# IF num2 > highest THEN
#   highest <- num2
# ENDIF
# IF num3 > highest THEN
#   highest <- num3
# ENDIF
# PRINT highest

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
if num1 > num2:
  #This code happens if the first number is larger than the second
  print(num2, num1)
else:
  #This code happens in all other cases, so the first number is NOT larger than the second
  print(num1, num2)