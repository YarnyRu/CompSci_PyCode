counter = 0
carryOn = True
while carryOn == True:
    number = int(input("Please enter a positive number: "))
    if number > 0:
        counter += 1
        if counter >= 50:
            carryOn = False