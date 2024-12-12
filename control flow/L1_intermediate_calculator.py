# Next step calculator
num1 = float(input("First number: "))
action = input("What would you like to do? add/subtract/multiply/divide ")
num2 = float(input("Second number: "))
if action == "add":
  print(num1 + num2)
elif action == "subtract":
  print(num1 - num2)
elif action == "multiply":
  print(num1 * num2)
elif action == "divide":
  print(num1 / num2)
else:
  print("Sorry, we do not support that function.")
