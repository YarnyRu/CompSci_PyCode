number1 = int(input("What is your first number?: "))
number2 = int(input("What is your second number?: "))
print ("What operation would you like to perform?")
operation = input("Please type A for add, M for multiply: ")
if operation == "A":
  result = number1 + number2
  print("Your result is", result)
elif operation == "M":
  result = number1 * number2
  print("Your result is", result)
else:
  print("I'm sorry, that wasn't a valid input")