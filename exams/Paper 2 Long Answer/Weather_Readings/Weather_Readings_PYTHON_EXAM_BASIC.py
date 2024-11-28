#Paper 2 Long Answer - Weather Readings
# Basic solution - no frills

#Populate array
Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Input and validate the temperatures for one week
for day in range(0, 7):
    for hour in range(0, 24):
        new_reading = float(input("Please enter the temperature: "))
        while new_reading < -20.0 or new_reading > 50.0:		# Validate input
            new_reading = float(input("Temp out of range. Please re-enter the temperature: "))
        Readings[day][hour] = new_reading		# Store new_reading in the 2D array once it is validated

# Average temperature calculations
for day in range (0, 7):				# For each day of the week...
    running_total = 0.0					# Reset a variable to hold the running total
    for hour in range (0, 24):				# For each of the 24 hourly readings
        running_total += Readings[day][hour]		# Create a running total of all the temperatures
    AverageTemp[day] = running_total / 24			# Calculate mean average
    temp_in_F = (AverageTemp[day] * 9 / 5) + 32		# Convert to Fahrenheit
    print("Average temperature for", Days[day], "is", round(AverageTemp[day], 1),
          "degrees Celsius, or", round(temp_in_F, 1), "degrees Fahrenheit")
    
# Weekly average calculation
total_of_averages = 0.0
for day in range (0, 7):
    total_of_averages += AverageTemp[day]			# Add to running total of daily averages

weekly_average = total_of_averages/7				# Calculate weekly mean average
weekly_average_in_F = (weekly_average * 9 / 5) + 32	# Convert to Fahrenheit
print("The weekly average temperature was", round(weekly_average, 1), "degrees Celsius, or",
      round(weekly_average_in_F, 1), "degrees Fahrenheit")