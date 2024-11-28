#Paper 2 Long Answer - Weather Readings
#Set up data storage - declaring arrays and variables

CONST_Days = 7
CONST_Hours = 24
Days = [""] * CONST_Days
AverageTemp = [0.0] * CONST_Days
Readings = [[0.0 for x in range(CONST_Hours)] for y in range(CONST_Days)]

#Initialise variables and arrays
Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day = 0

# Input and validate the temperatures for one week
with open('readings.txt') as f:
    for line in f:
        line = line.strip()
        if line[0] != "#":
            temp_input = line.split()  # hopefully there are 24 values on each line!
            num_of_readings = len(temp_input)	#you could check here to see if num_of_readings == CONST_Hours
            #print(temp_input)
            for hour in range(0, num_of_readings):
                if float(temp_input[hour]) < -20.0 or float(temp_input[hour]) > 50.0:
                    print("Temperature of", temp_input[hour], "is rejected")
                    Readings[day][hour] = 0.0  # to avoid affecting average
                else:
                    Readings[day][hour] = float(temp_input[hour])
            #print(Readings[day])
            day += 1

# Average temperature calculations
avgtemp_total = 0.0
for day in range (0, CONST_Days):
    daytemp_total = 0.0
    for hour in range (0, CONST_Hours):
        daytemp_total += Readings[day][hour]		#daytemp_total = daytemp_total + Readings[day][hour]
    AverageTemp[day] = daytemp_total / CONST_Hours
    temp_F = (AverageTemp[day] * 9 / 5) + 32
    print("Average temperature for", Days[day], "is", round(AverageTemp[day], 1), "degrees Celsius, or",
          round(temp_F, 1), "degrees Fahrenheit")
    avgtemp_total += AverageTemp[day]

avgtemp = avgtemp_total/CONST_Days
avgtemp_F = (avgtemp * 9 / 5) + 32
print("The weekly average temperature was", round(avgtemp, 1), "degrees Celsius, or",
      round(avgtemp_F, 1), "degrees Fahrenheit")
