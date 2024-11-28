# Summer Coding Challenge 2023
# REQUIRES READINGS.TXT
# Weather monitoring station keeps the data for a week, recording the midday temperatures
# Make the code able to store a longer/shorter range of temperatures
# Temps can be entered as decimal (floating point) numbers

# Prep work - learn how to read in from a text file
# with open("file.txt") as f:
# .strip()    getting rid of extra spaces/line breaks
# .split()    dividing up a line into a list of elements, default separator = space

CONST_Days = 3
#Set up data storage
day_temps = [0.0] * CONST_Days
night_temps = [0.0] * CONST_Days

#Initialise variables
daytime_total = 0
nighttime_total = 0
day_count = 0
night_count = 0
highest_temp = -999
lowest_temp = 999

day_num = 0
with open('readings.txt') as f:
  for line in f:
    line = line.strip()
    if line[0] == "#":
      # This means the line contains a comment  
      print(line)
    else:
      temp_input = line.split()  # hopefully there are two values on each line!
      print(temp_input)
      day_temps[day_num] = float(temp_input[0])
      night_temps[day_num] = float(temp_input[1])
      day_num += 1

# Midday temperature calculations
for i in range (0, CONST_Days):
  if day_temps[i] < -40 or day_temps[i] > 50:
    print("Temperature on day", i+1, "out of range")
    day_temps[i] = 0  # to avoid affecting average
  else:
    daytime_total += day_temps[i]
    day_count += 1
    if day_temps[i] > highest_temp:
      highest_temp = day_temps[i]
      high_day = i+1

# Midnight temperature calculations
for i in range (0, CONST_Days):
  if night_temps[i] < -40 or night_temps[i] > 50:
    print("Temperature on day", i+1, "out of range")
    night_temps[i] = 0  # to avoid affecting average
  else:
    nighttime_total += night_temps[i]
    night_count += 1
    if night_temps[i] < lowest_temp:
      lowest_temp = night_temps[i]
      low_day = i+1


print("The midday temperatures were:", day_temps)
midday_avg = daytime_total / day_count
print("The average midday temperature was %.2f degrees C" % midday_avg)
print("Highest temperature recorded was", highest_temp, "on day", high_day)


print("The midnight temperatures were:", night_temps)
midnight_avg = nighttime_total / night_count
print("The average midnight temperature was %.2f degrees C" % midnight_avg)
print("Lowest temperature recorded was", lowest_temp, "on day", low_day)