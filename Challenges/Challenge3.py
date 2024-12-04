# PSEUDOCODE
# An algorithm has been written in pseudocode to allow some numbers to be input.
# All the positive numbers are counted up, the negative numbers are ignored
# At the end, the program prints out how many positive numbers were entered.
# An input of 0 (zero) stops the algorithm

# Find the 4 mistakes in the algorithm

Exit <- 0
Count <- 0
WHILE Exit <> 0 DO
  INPUT Number
  IF Number < 0 THEN
    Count <- Count + 1
  ELSE
    IF Number = 0 THEN
        Exit <- 1
    ENDIF
  ENDIF
ENDWHILE
OUTPUT "There were a total of", Number, "positive numbers input"
