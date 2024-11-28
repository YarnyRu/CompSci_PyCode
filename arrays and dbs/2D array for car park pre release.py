# Car Park Spaces
# Oct/Nov 2022 Pre-Release Coding Challenge
# This time, we are creating one 2-dimensional array for all the CarRegs and Visitor Names for each 
# day (1 to 14) for holding the values for the 20 car park spaces. 

spaces = 21
days = 15

Visitor = [["" for i in range (spaces)] for j in range(days)]
Car = [["" for i in range (spaces)] for j in range(days)]

#Fill up with dummy data
print("This 2D array uses the format Visitor[day#][space#]")
for space in range(1, spaces):
  for day in range(1, days):
    Visitor[day][space] = "Day"+ str(day) + "Name" + str(space)
    Car[day][space] = "Day"+ str(day) + "Reg" + str(space)

print("Visitor arrays as follows:")
for i in range(0, days):
  print(Visitor[i])

print("Car arrays as follows:")
for i in range(0, days):
  print(Car[i])

