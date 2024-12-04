# Car Park Spaces
# Oct/Nov 2022 Pre-Release Coding Challenge
# This time, we are creating one 2-dimensional array for all the CarRegs and Visitor Names for each 
# day (1 to 14) for holding the values for the 20 car park spaces. 

spaces = 21
days = 15

Visitor = [["" for i in range (spaces)] for j in range(days)]
Car = [["" for i in range (spaces)] for j in range(days)]

# These arrays hold 14 numbers, one number for each day, the range of free spaces should be between 0 and 20
# Default is 20 free spaces
# For task 2, store how many general spaces and how many accessible spaces have been booked
# FreeSpaces should equal the sum of these, and could be dispensed with ultimately

FreeSpaces = [20] * days
# NextGeneralSpace starts at 20 and can go to 6, then it must stop after booking space 6
NextGeneralSpace = [20] * days
# NextAccessibleSpace starts at 1 and can go up to 20 or NextGeneralSpace, whichever is lower.
NextAccessibleSpace = [1] * days

#Fill up with dummy data
print("This 2D array uses the format Visitor[day#][space#]")
for space in range(1, spaces):
  for day in range(1, days):
    Visitor[day][space] = "Day"+ str(day) + "Name" + str(space)
    Car[day][space] = "Day"+ str(day) + "Reg" + str(space)
# Optional override fill from file
PreData = input("Would you like to use the pre-defined data? Y/N: ")
if PreData == "Y":
  count = 0
  with open('carparkdata.txt') as f:
    for line in f:
      FileDay, FileSpace, NameValue, RegValue = line.strip().split()
      PreDay = int(FileDay)
      PreSpace = int(FileSpace)
      Visitor[PreDay][PreSpace] = NameValue
      Car[PreDay][PreSpace] = RegValue
      FreeSpaces[PreDay] -= 1
      if PreSpace < 6:
        NextAccessibleSpace[PreDay] = PreSpace + 1
      elif PreDay >= 6:
        NextGeneralSpace[PreDay] = PreSpace - 1
      count += 1
    print("There were", count, "items of data stored")
  
carryon = True
# While loop allows multiple bookings
while carryon == True:
  # Getting input from the user
  ThisDay = int(input("Which day would you like to park? (Day 1-14): "))
  # Validation check for ThisDay
  while ThisDay < 1 or ThisDay > days-1:
    print (ThisDay, "is outside the required range, please try again.")
    ThisDay = int(input("Which day would you like to park? (Day 1-14): "))
  # Task 2 Accessibility  
  Accessibility_input = input("Do you need an accessible space? (Y/N): ")
  if Accessibility_input == "Y":
    Accessibility = True
  else:
    Accessibility = False
    
  if Accessibility == True:
    if FreeSpaces[ThisDay] == 0:
      print("There are no more spaces available on day", ThisDay)
    else:
      print("There are", FreeSpaces[ThisDay], "spaces available on day", ThisDay)
      ThisSpace = NextAccessibleSpace[ThisDay]
      ThisName = input("Please enter your name: ")
      #Add validation check for ThisName here
      ThisCar = input("Please enter your car registration: ")
      #Add validation check for ThisCar here
      Visitor[ThisDay][ThisSpace] = ThisName
      Car[ThisDay][ThisSpace] = ThisCar
      NextAccessibleSpace[ThisDay] += 1
      FreeSpaces[ThisDay] -= 1
      print(Visitor[ThisDay][ThisSpace], "- your car registration -", Car[ThisDay][ThisSpace], "has been booked in space", ThisSpace, "on day", ThisDay ) 
  else:  # If Accessibility == False
    if FreeSpaces[ThisDay] == 0:
      print("There are no more spaces available on day", ThisDay)
    elif NextGeneralSpace[ThisDay] == 5:
      print("There are no more general spaces available on day", ThisDay)
    else:
      print("There are", FreeSpaces[ThisDay], "spaces available on day", ThisDay)
      ThisSpace = NextGeneralSpace[ThisDay]
      ThisName = input("Please enter your name: ")
      #Add validation check for ThisName here
      ThisCar = input("Please enter your car registration: ")
      #Add validation check for ThisCar here
      Visitor[ThisDay][ThisSpace] = ThisName
      Car[ThisDay][ThisSpace] = ThisCar
      NextGeneralSpace[ThisDay] -= 1
      FreeSpaces[ThisDay] -= 1
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

# Task 3 - Request Car Park Statistics
Stats = input("Would you like to know any statistics about the car park usage? Y/N: ")
if Stats == "Y":
  Task3Loop = True
else:
  Task3Loop = False
  print("Thank you for using the car park program")
  
while Task3Loop == True:
  print("Please select which data you would like to know:") 
  print("1: The number of accessible spaces used on any of the 14 days.")
  print("2: The number of general spaces used on any of the 14 days.")
  print("3: The total number of spaces used on any of the 14 days.")
  print("4: The number of accessible spaces used in the whole 14-day period.")
  print("5: The number of general spaces used in the whole 14-day period.")
  print("6: The total number of spaces used in the whole 14-day period.")
  DataSelection = int(input("Enter 1-6: "))
  #Validation check for DataSelection
  while DataSelection < 1 or DataSelection > 6:
    print("That was not one of the choices!") 
    DataSelection = int(input("Enter 1-6: "))
  
  if DataSelection == 1:  # Number of accessible spaces used on a given day
    DataDay = int(input("Please enter the day you would like data for: "))
    Spaces = NextAccessibleSpace[DataDay]
    if Spaces > 5:
      print("All accessible spaces were used on day", DataDay)
    else:
      print("There were", Spaces - 1, "accessible spaces used on day", DataDay)
  if DataSelection == 2: # Number of general spaces used on a given day
    DataDay = int(input("Please enter the day you would like data for: "))
    Spaces = NextGeneralSpace[DataDay]
    if Spaces == 5:
      print("All general spaces were used on day", DataDay)
    else:
      print("There were", 20 - Spaces, "general spaces used on day", DataDay)
  if DataSelection == 3:  #Total spaces used on this day
    DataDay = int(input("Please enter the day you would like data for: "))
    print("There were a total of", 20 - FreeSpaces[DataDay] , "spaces used on day", DataDay) 
  if DataSelection == 4:  #Total accessible spaces used in the whole period
    AccTotal = 0
    for day in range(1, days):
      Spaces = NextAccessibleSpace[day]
      if Spaces > 5:
        AccTotal = AccTotal + 5
      else:
        AccTotal = AccTotal + Spaces - 1
    print("There were a total of", AccTotal, "accessible spaces used in the whole period") 

  if DataSelection == 5:  #Total general spaces used in the whole period
    GenTotal = 0
    for day in range(1, days):
      Spaces = NextGeneralSpace[day]
      if Spaces == 5:
        GenTotal = GenTotal + 15
      else:
        GenTotal = GenTotal + 20 - Spaces    
    print("There were a total of", GenTotal, "accessible spaces used in the whole period") 

  if DataSelection == 6:  #Total spaces used in the whole period
    SpacesTotal = 0
    for day in range(1, days):
      Add = 20 - FreeSpaces[day] 
      SpacesTotal = SpacesTotal + Add 
    print("There were a total of", SpacesTotal, "spaces used in the whole period")
    
  Stats = input("Would you like to know any more statistics about the car park usage? Y/N: ")
  if Stats == "Y":
    Task3Loop = True
  elif Stats = "N":
    Task3Loop = False
  else:
    print("Did you mean to type that? Last chance!")
    Stats = input("Would you like to know any more statistics about the car park usage? Y/N: ")
    if Stats == "Y":
      Task3Loop = True
    else:
      Task3Loop = False
print("Thank you for using this car park booking system")
print("This is the end of the two week period, all data will now be deleted")
