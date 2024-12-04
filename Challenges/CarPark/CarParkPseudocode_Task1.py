# PSEUDOCODE
spaces <- 21
days <- 15
DECLARE Visitor : ARRAY[1:14, 1:20] OF STRING
DECLARE Car : ARRAY[1:14, 1:20] OF STRING
DECLARE FreeSpaces : ARRAY [0:20] OF INTEGER
DECLARE NextSpace : ARRAY [0:20] OF INTEGER
carryon <- True
WHILE carryon = True DO
  PRINT "Which day would you like to park? (Day 1-14): "
  INPUT ThisDay
  IF FreeSpaces[ThisDay] = 0 THEN PRINT "No more spaces on day", ThisDay
  ELSE PRINT "There are", FreeSpaces[ThisDay], "spaces on day", ThisDay
    ThisSpace <- NextSpace[ThisDay]
    PRINT "Please enter your name and car reg"
    INPUT ThisName, ThisCar
    Visitor[ThisDay][ThisSpace] <- ThisName
    Car[ThisDay][ThisSpace] <-  ThisCar
    NextSpace[ThisDay] <- NextSpace[ThisDay] + 1
    FreeSpaces[ThisDay] <- FreeSpaces[ThisDay] - 1
    PRINT Visitor[ThisDay][ThisSpace], "- your car reg", Car[ThisDay][ThisSpace], 
             "is booked in space", ThisSpace, "on day", ThisDay
  ENDIF
  PRINT "Would you like to make another booking?"
  INPUT carryon
ENDWHILE
PRINT "Thank you for using this car park booking system"
PRINT "This is the end of the two week period, all data will now be deleted"
