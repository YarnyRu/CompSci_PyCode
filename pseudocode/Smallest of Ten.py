# Allows the user to enter a number 10 times, it finds the smallest value input, and prints it at the end
# Pseudocode version
Small <- 99999
Counter <- 0
REPEAT
   INPUT Num
   IF Num < Small
     THEN
     Small <- Num
   ENDIF
   Counter <- Counter + 1
UNTIL Counter = 10
OUTPUT "Smallest number is ", Small

















# Python version
small = 99999
counter = 0
while counter < 10:
    num = int(input("Please enter a number: "))
    if num < small:
        small = num
    counter += 1
print("Smallest number is", small)