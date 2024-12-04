# Car Park Spaces
# Oct/Nov 2022 Pre-Release Coding Challenge
# This time, we are creating one 2-dimensional array for all the CarRegs and Visitor Names for each 
# day (1 to 14) for holding the values for the 20 car park spaces. 

# TASK 1 ONLY
spaces = 21
days = 15

Visitor = [["" for i in range (spaces)] for j in range(days)]
Car = [["" for i in range (spaces)] for j in range(days)]

# These arrays hold 14 numbers, one number for each day, the range of free spaces should be between 0 and 20
# Default is 20 free spaces
# For task 2, store how many general spaces and how many accessible spaces have been booked
# FreeSpaces should equal the sum of these, and could be dispensed with ultimately

FreeSpaces = [20] * days
 
carryon = True
# While loop allows multiple bookings
while carryon == True:
  # Getting input from the user
  ThisDay = int(input("Which day would you like to park? (Day 1-14): "))
  # Validation check for ThisDay
  if FreeSpaces[ThisDay] == 0:
    print("There are no more spaces available on day", ThisDay)
  else:
    print("There are", FreeSpaces[ThisDay], "spaces available on day", ThisDay)
    ThisSpace = 21 - FreeSpaces[ThisDay]
    ThisName = input("Please enter your name: ")
    #Add validation check for ThisName here
    ThisCar = input("Please enter your car registration: ")
    #Add validation check for ThisCar here
    Visitor[ThisDay][ThisSpace] = ThisName
    Car[ThisDay][ThisSpace] = ThisCar
    FreeSpaces[ThisDay] = FreeSpaces[ThisDay] - 1
    print(Visitor[ThisDay][ThisSpace], "- your car registration -", Car[ThisDay][ThisSpace], "has been booked in space", ThisSpace, "on day", ThisDay ) 
  # Part 3 of the while loop - deciding whether to repeat    
  usercontinue = input("Would you like to make another booking? (Y/N): ")
  if usercontinue == 'Y':
    carryon = True
  else:
    carryon = False

print("Visitor arrays as follows:")
for i in range(0, days):
  print(Visitor[i])
print("Car arrays as follows:")
for i in range(0, days):
  print(Car[i])
