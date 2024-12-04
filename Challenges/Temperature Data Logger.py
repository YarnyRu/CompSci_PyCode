# Temperature Data Logger Summer15/21
# Task 1: input and store midday and midnight temperatures each day for a month
#   Store in two one-dimensional arrays and validate

# Task 2: Calculate the average temperature for midday and average temp for midnight

# Task 3: Select day with highest midday temp and lowest midnight temp

# Declare and initialise variables
MiddayTemps = [0] * 7
MidnightTemps = [0] * 7
#MiddayTemps[30] = [0] * 30
#MidnightTemps[30]= [0] * 30
MiddayRunningTotal = 0
MidnightRunningTotal = 0
MiddayCount = 0
MidnightCount = 0

# Ask for inputs
for i in range (0, 7):
    MiddayString = "Please enter the midday temp for day " + str(i+1) + ": "
    MiddayInput = float(input(MiddayString))
    if MiddayInput < -40 or MiddayInput > 50:
        # Input rejected
        print("Temperature out of range")
        MiddayTemps[i] = 0
    else:
        MiddayTemps[i] = MiddayInput
        MiddayRunningTotal += MiddayTemps[i]
        MiddayCount += 1

    # Midnight Input
    MidnightString = "Please enter the midnight temp for day " + str(i+1) + ": "
    MidnightInput = float(input(MidnightString))
    if MidnightInput < -40 or MidnightInput > 50:
        # Input rejected
        print("Temperature out of range")
        MidnightTemps[i] = 0
    else:
        MidnightTemps[i] = MidnightInput
        MidnightRunningTotal += MidnightTemps[i]
        MidnightCount += 1
       
# This code executes after the for loop
MiddayAvg = MiddayRunningTotal / MiddayCount
MidnightAvg = MidnightRunningTotal / MidnightCount
print("The midday temperatures were:", MiddayTemps)
print("The average midday temperature was %.2f" % MiddayAvg, "degrees C")
print("The midnight temperatures were:", MidnightTemps)
print("The average midnight temperature was %.2f" % MidnightAvg, "degrees C")

