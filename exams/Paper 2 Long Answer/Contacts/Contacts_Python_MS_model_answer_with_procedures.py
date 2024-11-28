# Contacts Python with procedures

def PopulateArray(FileName):
    with open(FileName) as f:
        i = 0
        for line in f:
            line = line.strip()
            if line[0] != "#":
                temp_input = line.split()
                entries = len(temp_input)
                if entries != 2:
                    print("Error in reading in file")
                else:
                    for item in range(0, entries):
                        if item == 0:             # this is the contact's name
                            Contacts[i][0] = temp_input[item]
                        elif item == 1:           # this is the contact's phone number
                            Contacts[i][1] = temp_input[item]
                        else:
                            print("Error in entering contact details")
            i += 1	# Move on to the next line/row in the file, keep an index number of the row
    print("A total of", i, "contacts were saved")
    print(Contacts)
    return (i)

def Enter_Contacts(size):
    print("You currently have", size, "contacts in your list")
    NewContacts = int(input("Number of new contacts to enter (maximum of 5): "))
    # Validates user input, range between 1 and 5 only
    while NewContacts < 1 or NewContacts > 5:
        NewContacts = int(input("You may only enter between 1 and 5 contacts. Please try again: "))
    # Ensures there is space in the contacts array
    while size + NewContacts > max_size:
        print("Not enough space. The maximum number you may input is", max_size - size)
        NewContacts = int(input("Please try again: "))
    # Store new contacts in Contacts[] array
    for Count in range(size, size + NewContacts):
        Contacts[Count][0] = input("Enter the contact name: ")
        Contacts[Count][1] = input("Enter the telephone number: ")
    # Update variable holding number of contacts entered
    size += NewContacts
    # Bubble sort to sort array if it contains 2 or more contacts
    if size >= 2:
        SortNeeded = True
        while SortNeeded == True:			# Continue this sort until no 'out of order' contacts are found
            SortNeeded = False				# Reset this flag to check whether the array is now in order
            for Count in range(0, size-1):
                if Contacts[Count + 1][0] < Contacts[Count][0]:
                    SortNeeded = True		# An out of order contact has been found, bubble sort needed
                    Temp1 = Contacts[Count][0]						# Temporarily store the name
                    Temp2 = Contacts[Count][1]  					#    and number of the first contact
                    Contacts[Count][0] = Contacts[Count + 1][0]		#Move the second contact to the position
                    Contacts[Count][1] = Contacts[Count + 1][1]		#    of the first contact
                    Contacts[Count + 1][0] = Temp1					# Now insert the first contact back in
                    Contacts[Count + 1][1] = Temp2					#    to where the second contact had been
    return(size)

def Display_Contacts(size):
    if size > 0:
        print("\nName and Telephone Number")
        for Count in range (0, size):
            print(Contacts[Count][0], Contacts[Count][1])

def Delete_Contacts(size):
    for Count in range(0, size):
        for Count2 in range (0, 2):
            Contacts[Count][Count2] = ""

max_size = 10
Contacts = [["" for x in range(2)] for y in range(max_size)]
CurrentSize = PopulateArray("contacts.txt")

CarryOn = True
while CarryOn:	# Allows program to continue indefinitely 
    print("\nMenu. \n 1: Enter new contacts \n 2: Display your contacts \n 3: Delete all contacts") # Display menu
    Choice = int(input("Please enter 1, 2 or 3: "))		
    while Choice < 1 or Choice > 3:		# Validate choice as 1, 2 or 3
        Choice = int(input("Incorrect entry – please enter 1, 2, or 3"))
        
    while Choice == 1 and CurrentSize = 100:
        Choice = int(input("Your contacts are full, please enter 2 or 3"))
    
    if Choice == 1:
        print("Let's enter contacts!")
        CurrentSize = Enter_Contacts(CurrentSize) 	# enter new contacts
    elif Choice == 2:
        print("Let's display contacts!")
        Display_Contacts(CurrentSize)	# display all contacts
    elif Choice == 3:
        print("Let's delete contacts!")
        Delete_Contacts(CurrentSize)	# delete all contacts
    else:
        print("Error")