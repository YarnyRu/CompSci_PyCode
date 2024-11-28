#Paper 2 Long Answer June 23/22 PYTHON

Size = 3
Account = [["" for x in range(2)] for y in range(Size)]
AccDetails = [[0.0 for x in range(3)] for y in range(Size)]
# Input and populate the arrays Account[] and AccDetails[]
with open('accounts.txt') as f:
    i = 0
    for line in f:
        line = line.strip()
        if line[0] != "#":
            temp_input = line.split()  # hopefully there are 5 values on each line!
            entries = len(temp_input)
            if entries != 5:
                print("Error in reading in file")
            else:
                for item in range(0, entries):
                    if item == 0:             # this is the account name
                        Account[i][0] = temp_input[item]
                    elif item == 1:           # this is the password
                        Account[i][1] = temp_input[item]
                    elif item == 2:           # this is the balance
                        AccDetails[i][0] = float(temp_input[item])
                    elif item == 3:           #this is the overdraft limit
                        AccDetails[i][1] = float(temp_input[item])
                    elif item == 4:           # this is the withdrawal limit
                        AccDetails[i][2] = float(temp_input[item])
            i += 1
print(Account)
print(AccDetails)

# Main code
AccID = int(input("Please enter your account number: "))
Valid = False
if AccID < 0 or AccID >= Size:
    print("Invalid Account Number")
else:
    Name = input("Please enter name: ")
    Password = input("Please enter password: ")
    if Name != Account[AccID][0] or Password != Account[AccID][1]:
        print("Invalid name or password.")
    else:
        Valid = True
if Valid == True:
    Choice = 0
    while Choice != 4:
        print("Menu\n 1. Display balance\n 2. Withdraw money\n 3. Deposit money\n 4. Exit")
        Choice = int(input("Please choose 1, 2, 3 or 4: "))
        if Choice == 1:
            print("Your balance is", AccDetails[AccID][0])
        elif Choice == 2:
            Amount = -999.99	# initialising value so loop happens at least once
            while (Amount > AccDetails[AccID][2] or Amount > AccDetails[AccID][1] + AccDetails[AccID][0] or Amount < 0):
                Amount = float(input("Please enter amount to withdraw: "))
                if Amount > AccDetails[AccID][2]:
                    print("Amount greater than withdrawal limit.")
                if Amount > AccDetails[AccID][1] + AccDetails[AccID][0]:
                    print("Amount greater than cash available.")
                if Amount <= AccDetails[AccID][2] and Amount < AccDetails[AccID][1] + AccDetails[AccID][0]:
                    AccDetails[AccID][0] -= Amount	#decrement by the value of Amount
                    print(Amount, "has been withdrawn")
        elif Choice == 3:
            Amount = -999.99
            while Amount <= 0:
                Amount = float(input("Please enter a positive amount to deposit: "))
            AccDetails[AccID][0] += Amount
        elif Choice == 4:
            Exit = True
            print("Goodbye")
        else:
            print("Invalid choice")