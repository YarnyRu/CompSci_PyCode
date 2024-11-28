#Paper 2 Long Answer - Weather Readings
#Set up data storage - declaring arrays and variables

CONSTANT MaxDays = 7
CONSTANT MaxHours = 24
DECLARE Days : [1, MaxDays] AS STRING
DECLARE Readings : ARRAY [1, MaxDays: 1, MaxHours] AS REAL
DECLARE AverageTemp : [1, MaxDays] AS REAL

#Initialise array
Days[1] <- "Mon"
Days[2] <- "Tue"
Days[3] <- "Wed"
Days[4] <- "Thu"
Days[5] <- "Fri"
Days[6] <- "Sat"
Days[7] <- "Sun"

# Input and validate the temperatures for one week
FOR day <- 1 TO MaxDays
    FOR hour <- 1 TO MaxHours
        PRINT "Please enter temperature for hour", hour, "for day", Days[day]
        INPUT InTemp
        WHILE InTemp < -20.0 OR InTemp > 50.0 DO
            PRINT "The temperature must be between -20.0 and +50.0 inclusive. Please try again"
            INPUT InTemp
        ENDWHILE
        Readings[day][hour] <- InTemp
    NEXT hour
NEXT day

# Average temperature calculations
FOR day <- 1 TO MaxDays
    daytemp_total <- 0.0
    FOR hour <- 1 TO MaxHours
        daytemp_total <- daytemp_total + Readings[day][hour]
    NEXT hour
    AverageTemp[day] <- daytemp_total / MaxHours
    temp_F <- (AverageTemp[day] * 9 / 5) + 32
    PRINT "Average temperature for", Days[day], "is", ROUND(AverageTemp[day], 1), "degrees Celsius, or",
          ROUND(temp_F, 1), "degrees Fahrenheit"
NEXT day   

# Weekly average calculations
avgtemp_total <- 0.0
FOR day <- 1 to MaxDays
    avgtemp_total = avgtemp_total + AverageTemp[day]

avgtemp <- avgtemp_total/MaxDays
avgtemp_F <- (avgtemp * 9 / 5) + 32
PRINT "The weekly average temperature was", ROUND(avgtemp, 1), "degrees Celsius, or",
      ROUND(avgtemp_F, 1), "degrees Fahrenheit"

