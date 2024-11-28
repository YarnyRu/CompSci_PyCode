#Paper 2 Long Answer - Weather Readings

#Initialise variables and arrays
Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_of_days = len(Days)
num_of_hours = 24

# Input and validate the temperatures for one week
for day in range(0, num_of_days):
    for hour in range(0, num_of_hours):
        new_reading = float(input("Please enter the temperature for hour", hour,
                                  "on day", Days[day]))
        # Validate input
        while new_reading < -20.0 or new_reading > 50.0:
            print("The temperature must be between -20.0 and +50.0 inclusive.")
            new_reading = float(input("Please enter the temperature for day", day,
                                      "and hour", hour))
        Readings[day][hour] = new_reading		# Store new_reading in the 2D array

# Average temperature calculations
avgtemp_total = 0.0
for day in range (0, CONST_Days):
    daytemp_total = 0.0
    for hour in range (0, CONST_Hours):
        daytemp_total += Readings[day][hour]
    AverageTemp[day] = daytemp_total / CONST_Hours	#calculate mean
    temp_F = (AverageTemp[day] * 9 / 5) + 32
    print("Average temperature for", Days[day], "is", round(AverageTemp[day], 1),
          "degrees Celsius, or", round(temp_F, 1), "degrees Fahrenheit")
    avgtemp_total += AverageTemp[day]

avgtemp = avgtemp_total/CONST_Days
avgtemp_F = (avgtemp * 9 / 5) + 32
print("The weekly average temperature was", round(avgtemp, 1), "degrees Celsius, or",
      round(avgtemp_F, 1), "degrees Fahrenheit")
