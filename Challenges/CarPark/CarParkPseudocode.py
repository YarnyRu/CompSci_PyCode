# PSEUDOCODE
spaces <- 21
days <- 15
DECLARE Visitor : ARRAY[1:14, 1:20] OF STRING
DECLARE Car : ARRAY[1:14, 1:20] OF STRING
DECLARE FreeSpaces : ARRAY [0:20] OF INTEGER
DECLARE NextGenSpace : ARRAY [0:20] OF INTEGER
DECLARE NextAccSpace : ARRAY [0:20] OF INTEGER
carryon <- True
WHILE carryon = True DO
  PRINT "Which day would you like to park? (Day 1-14): "
  INPUT ThisDay
  PRINT "Do you need an accessible space? (Y/N): "
  INPUT Acc
  IF Acc = True THEN
    IF FreeSpaces[ThisDay] = 0 THEN PRINT "No more spaces on day", ThisDay
    ELSE PRINT "There are", FreeSpaces[ThisDay], "spaces on day", ThisDay
      ThisSpace <- NextAccSpace[ThisDay]
      PRINT "Please enter your name and car reg"
      INPUT ThisName, ThisCar
      Visitor[ThisDay][ThisSpace] <- ThisName
      Car[ThisDay][ThisSpace] <-  ThisCar
      NextAccSpace[ThisDay] <- NextAccSpace[ThisDay] + 1
      FreeSpaces[ThisDay] <- FreeSpaces[ThisDay] - 1
      PRINT Visitor[ThisDay][ThisSpace], "- your car reg", Car[ThisDay][ThisSpace], 
               "is booked in space", ThisSpace, "on day", ThisDay
    ENDIF
  ELSE  # If Accessibility is False
    IF FreeSpaces[ThisDay] = 0 THEN PRINT "There are no more spaces available on day", ThisDay
    ELIF NextGenSpace[ThisDay] = 5 THEN PRINT "No more general spaces on day", ThisDay
    ELSE PRINT "There are", FreeSpaces[ThisDay], "spaces on day", ThisDay
      ThisSpace <- NextGenSpace[ThisDay]
      PRINT "Please enter your name and car reg"
      INPUT ThisName, ThisCar
      Visitor[ThisDay][ThisSpace] <- ThisName
      Car[ThisDay][ThisSpace] <- ThisCar
      NextGenSpace[ThisDay] <- NextGenSpace[ThisDay] - 1
      FreeSpaces[ThisDay] <- FreeSpaces[ThisDay] - 1
      PRINT Visitor[ThisDay][ThisSpace], "- your car reg", Car[ThisDay][ThisSpace], 
          "is booked in space", ThisSpace, "on day", ThisDay
    ENDIF
  ENDIF
  INPUT carryon
ENDWHILE
PRINT "Would you like to know any statistics about the car park usage? Y/N: "
INPUT Stats
WHILE Stats = True DO
  PRINT "Please select from options 1 to 6:"
  INPUT DataSelection
  CASE OF DataSelection 
    1:  # Number of accessible spaces used on a given day
    INPUT DataDay
    Spaces <- NextAccessibleSpace[DataDay]
    IF Spaces > 5 THEN PRINT "All accessible spaces were used on day", DataDay
    ELSE PRINT "There were", Spaces - 1, "accessible spaces used on day", DataDay
    ENDIF
    2:  # Number of general spaces used on a given day
    INPUT DataDay
    Spaces <- NextGeneralSpace[DataDay]
    IF Spaces = 5 THEN PRINT "All general spaces were used on day", DataDay
    ELSE PRINT "There were", 20 - Spaces, "general spaces used on day", DataDay
    ENDIF
    3:  #Total spaces used on this day
    INPUT DataDay
    PRINT "There were a total of", 20 - FreeSpaces[DataDay] , "spaces used on day", DataDay
    4:   #Total accessible spaces used in the whole period
    AccTotal <- 0
    FOR day <- 1 TO days
      Spaces <- NextAccessibleSpace[day]
      IF Spaces > 5 THEN AccTotal <- AccTotal + 5
      ELSE AccTotal <- AccTotal + Spaces - 1
      ENDIF
    NEXT day
    PRINT "There were a total of", AccTotal, "accessible spaces used in the whole period"
    5:   #Total general spaces used in the whole period
    GenTotal <- 0
    FOR day <- 1 TO days
      Spaces <- NextGeneralSpace[day]
      IF Spaces = 5 THEN GenTotal <- GenTotal + 15
      ELSE GenTotal <- GenTotal + 20 - Spaces    
      ENDIF
    NEXT day
    PRINT "There were a total of", GenTotal, "accessible spaces used in the whole period"
    6:  #Total spaces used in the whole period
    SpacesTotal <- 0
    FOR day <- 1 TO days
      Add <- 20 - FreeSpaces[day] 
      SpacesTotal <- SpacesTotal + Add 
    NEXT day
    PRINT "There were a total of", SpacesTotal, "spaces used in the whole period")
  ENDCASE
  INPUT Stats
ENDWHILE
PRINT "Thank you for using this car park booking system"
PRINT "This is the end of the two week period, all data will now be deleted"
