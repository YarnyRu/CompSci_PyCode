# Write a program that allows the user unlimited attempts to enter 50 positive integers
# Pseudocode version
Counter <- 0
CarryOn <- TRUE
WHILE CarryOn = TRUE DO
    INPUT Number
    IF Number > 0 THEN
        Counter <- Counter + 1
        IF Counter >= 50 THEN
            CarryOn = FALSE
        ENDIF
    ENDIF
ENDWHILE

# Python version
counter = 0
carryOn = True
while carryOn == True:
    number = int(input("Please enter a positive number: "))
    if number > 0:
        counter += 1
        if counter >= 50:
            carryOn = False