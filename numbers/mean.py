# This is an algorithm, written in Python, that reads in 5 positive numbers, then stops.

Counter = 0
Running_Total = 0
CarryOn = True
while CarryOn == True:
    Number = int(input("Please enter a number: "))
    if Number > 0:
        Running_Total = Running_Total + Number
        Counter = Counter + 1
        if Counter >= 5:
            CarryOn = False
# The following code occurs after the while loop has exited
print("You have entered", Counter, "numbers")
print("The value in Number is", Number)