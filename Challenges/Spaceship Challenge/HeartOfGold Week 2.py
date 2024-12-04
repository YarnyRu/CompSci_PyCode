# SPACESHIP CHALLENGE Week 1 - No Aliens Allowed!
from random import randint
from time import sleep
# Spaceship login
crew_names = ["Arthur", "Zaphod", "Ford", "Marvin"]
crew_passwords = ["Towel", "Beeblebrox", "SoLong", "AllSpareParts"]
crew_ages = [34, 564, 100, 100000000000000000]

print("Welcome to the 'Heart of Gold' Spaceship!")
print("We apologise for the inconvenience")
CarryOn = False
planet_temp = -274

def check_temperature():
    print("\nChecking planetary surface temperature...")
    sleep(2)
    temperature = randint(-273, 800)
    print("The surface temperature of this planet is", temperature, "degrees C")
    return (temperature)

def spacewalk_check(t):
    print("\nChecking conditions for a spacewalk...")
    print("Current temperature is", t, "degrees C")
    print("Which spacesuit are you using?")
    spacesuit = input("Enter D for Deluxe or S for Standard: ")
    if spacesuit.upper() == "D":
        if t < -200 or t > 400:
            print("DANGER - DO NOT LEAVE SPACESHIP! You will either combust or freeze in approx", abs(round(1000/t, 2)), "seconds!")
        elif t < -100 or t > 200:
            print("WARNING - SHORT SPACEWALK ONLY! You can only survive on the planet's surface for", abs(round(10000/t, 0)), "minutes!")
        else:
            print("SAFE temperature for a spacewalk - don't forget your spacesuit!")
    elif spacesuit.upper() == "S":
        if t < -100 or t > 200:
            print("DANGER - DO NOT LEAVE SPACESHIP! You will either combust or freeze in approx", abs(round(500/t, 2)), "seconds!")
        elif t < -50 or t > 100:
            print("WARNING - SHORT SPACEWALK ONLY! You can only survive on the planet's surface for", abs(round(5000/t, 0)), "minutes!")
        else:
            print("SAFE temperature for a spacewalk - don't forget your spacesuit!")
        
def check_oxygen():
    print("\nChecking oxygen levels now...")
    sleep(1)
    print("Oxygen levels satisfactory")
    print("Have a nice day")

def translate_mode():
    alien_text = input("\nPlease enter the alien's statement: ")
    print("I don't understand that yet, sorry")
    
# Ask for name of crew member
username = input("Please enter your first name: ")
# Check to see whether the name entered is in the crew list.
for i in range (0, len(crew_names)):
    if crew_names[i] == username:
        print("Hello", username.title())
        # If name found, ask for password
        userpwd = input("Please enter your password: ")
        # Check the matching password in the crew_passwords list
        if crew_passwords[i] == userpwd:
            print("Password accepted")
            # ONLY set CarryOn to True if both username and password have been entered incorrectly
            CarryOn = True
        else:
            print("Password incorrect")
    
if CarryOn == False:	# This means either the username or the password was incorrect
    print("Sorry, no aliens allowed")

# Only continue with displaying the menu if the user has been validated
while CarryOn == True:
    print("\nHeart of Gold Computer System")
    print("What would you like to do?")
    print("   1: Check surface temperature of planet")
    print("   2: Check oxygen levels inside spaceship")
    print("   3: Check conditions for a spacewalk")
    print("   4: Translate alien speech mode")
    print("   5: EXIT")
    # Ask user to select one of these options.
    option = int(input("Enter option: "))
    if option == 1:
        print("Checking surface temperature...")
        planet_temp = check_temperature()
    elif option == 2:
        print("Checking oxygen levels...")
        check_oxygen()
    elif option == 3:
        print("Checking spacewalk conditions...")
        if planet_temp == -274:
            print("Checking surface temperature first")
            planet_temp = check_temperature()
        spacewalk_check(planet_temp)
    elif option == 4:
        print("Initiating alien translation mode...")
        translate_mode()
    elif option == 5:
        print("Shutdown sequence initiated")
        CarryOn = False
    else:
        print("That is not a valid option, please try again")
# Shut down code
print("So long, and thanks for all the fish!")