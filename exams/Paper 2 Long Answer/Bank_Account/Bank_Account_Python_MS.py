#Paper 2 Long Answer June 23/22 PYTHON

def CheckDetails (ID):
    Valid = False
    if ID < 0 or ID >= Size:
        print("Invalid Account Number")
    else:
        Name = input("Please enter name: ")
        Password = input("Please enter password: ")
        if Account[ID][0] != Name:
            print("Invalid name.")
        elif Password != Account[ID][1]:
            print("Invalid password.")
        else:
            Valid = True
    return Valid

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
if CheckDetails(AccID) == True:
    Choice = 0
    Exit = False
    while Exit != True:
        print("Menu\n 1. Display balance\n 2. Withdraw money\n 3. Deposit money\n 4. Exit")
        Choice = int(input("Please choose 1, 2, 3 or 4: "))
        if Choice == 1:
            Balance(AccID)
        elif Choice == 2:
            Withdraw(AccID)
        elif Choice == 3:
            Deposit(AccID)
        elif Choice == 4:
            Exit = True
        else:
            print("Invalid choice")
else:
    print("Invalid details.")
    
def Balance(Acc):
    print("Your balance is", AccDetails[Acc][0])
    
def Withdraw(Acc):
    Amount = -999.99	# initialising value so loop happens at least once
    while (Amount > AccDetails[Acc][2] or Amount > AccDetails[Acc][1] + AccDetails[Acc][0] or Amount < 0):
        Amount = float(input("Please enter amount to withdraw: "))
        if Amount > AccDetails[Acc][2]:
            print("Amount greater than withdrawal limit.")
        if Amount > AccDetails[Acc][1] + AccDetails[Acc][0]:
            print("Amount greater than cash available.")
        if Amount <= AccDetails[Acc][2] and Amount < AccDetails[Acc][1] + AccDetails[Acc][0]:
                    AccDetails[Acc][0] -= Amount	#decrement by the value of Amount
            print(Amount, "has been withdrawn")
    
def Deposit(Acc):
    Amount = -999.99
    while Amount <= 0:
        Amount = float(input("Please enter a positive amount to deposit: "))
    AccDetails[Acc][0] += Amount