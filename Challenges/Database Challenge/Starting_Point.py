# Two-dimensional array tests
max_rows = 3
max_cols = 2
Names = [["Bob" for x in range(max_cols)] for y in range(max_rows)]
for row in range(0, max_rows):
    for col in range(0, max_cols):
        print("Names["+str(row)+"]["+str(col)+"] is "+Names[row][col], end = "    ")
    print("\n")

# Your first challenge is to change every name from Bob to something different!
carry_on = True
while carry_on == True:
    row = int(input("Which row do you want to change? "))
    col = int(input("And which column? "))
    new_name = input("What name do you want to input? ")
    Names[row][col] = new_name
    print("Names["+str(row)+"]["+str(col)+"] is "+Names[row][col])
    for row in range(0, max_rows):
        for col in range(0, max_cols):
            print("Names["+str(row)+"]["+str(col)+"] is "+Names[row][col], end = "    ")
        print("\n")
    if input("Do you want to continue? y/n ").lower() == 'n':
        carry_on = False