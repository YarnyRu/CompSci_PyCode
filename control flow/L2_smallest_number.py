# Smallest Number Pseudocode to Python
# Small <- 9999
# Counter <- 0
Small = 9999
Counter = 0

#REPEAT
#  INPUT Num
#  IF Num < Small THEN
#    Small <- Num
#  ENDIF
#  Counter <- Counter + 1
#UNTIL Counter = 10

while Counter < 10:
  Num = int(input("Please enter a number: "))
  if Num < Small:
    Small = Num
  Counter = Counter + 1

#PRINT "Smallest Number is", Small
print("Smallest Number is", Small)