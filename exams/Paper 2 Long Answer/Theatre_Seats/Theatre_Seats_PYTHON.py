# Theatre Seats
CONST_rows = 10
CONST_seats = 20
Evening = [[False for x in range(CONST_seats)] for y in range(CONST_rows)]

def ImportData(filename):
    with open(filename) as f:
        row = 0
        for line in f:
            line = line.strip()
            if line[0] != "#":
                temp_input = line.split()  # This temp_input array should have each element on a single line
                number_of_elements = len(temp_input)	# This can double-check the number
                #print(temp_input)
                for element in range(0, number_of_elements):		# Validate entries
                    if temp_input[element] == "T":
                        Evening[row][element] = True
                    elif temp_input[element] == "T":
                        Evening[row][element] = False
                row += 1

ImportData("seats.txt")
# Count total number of seats already booked
SeatsBooked = 0
for row in range(0, 10):		# Check every seat in the theatre
    for seat in range (0, 20):
        if Evening[row][seat] == True:
            SeatsBooked += 1		# Tally up seats booked

print ("There are", SeatsBooked, "seats booked")
CarryOn = True
while CarryOn == True:
    # Ask user to enter how many seats to book
    Number = int(input("Enter the number of seats required (1-4): "))
    while Number < 1 or Number > 4:				# Validate number of seats input
        Number = int(input("Enter the number of seats required (1-4): "))

    BookingMade = False		# To keep track of whether the booking has been made
    for row in range(0, 10):		# Check for available seats
        for seat in range (0, 20):
            if BookingMade == False:					# This seat is available for booking
                if Evening[row][seat] == False:
                    # Start checking for consecutive seats
                    if seat + Number - 1 < 20:		# Seats can be booked on this row
                        BookingMade = True				# This ensures seats are only booked once
                        for i in range(0, Number):			# For each seat to be booked
                            Evening[row][seat + i] = True
                            print("Seat", seat + i, "in row", row, "is booked")

    if SeatsBooked == 200:					# No more seats available
        print("House full")
    else:
        if BookingMade == False:				# Seats were not available together, or insufficient seats remaining
            print("There are only", 200 - SeatsBooked, "seats available")
    response = input("Would you like to make another booking? Y/N: ")
    if response.upper() == "N":
        CarryOn = False
print(Evening)