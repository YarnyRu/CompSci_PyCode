# SPACESHIP CHALLENGE Week 1 - No Aliens Allowed!
from time import sleep
# Spaceship login
crew_names = ["Arthur", "Zaphod", "Ford", "Marvin"]
crew_passwords = ["Towel", "Beeblebrox", "SoLong", "AllSpareParts"]

print("Welcome to the 'Heart of Gold' Spaceship!")
print("We apologise for the inconvenience")
CarryOn = False

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
            # ONLY set CarryOn to True if both username and password have been entered correctly
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
    elif option == 2:
        print("Checking oxygen levels...")
    elif option == 3:
        print("Checking spacewalk conditions...")
    elif option == 4:
        print("Initiating alien translation mode...")
    elif option == 5:
        print("Shutdown sequence initiated")
        CarryOn = False
    else:
        print("That is not a valid option, please try again")
# Shut down code
print("So long, and thanks for all the fish!")