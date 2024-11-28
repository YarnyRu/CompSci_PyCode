#Paper 2 Long Answer June 23/22 PYTHON
# THIS CODE WILL NOT RUN!!!
# This is the code they expect you to write in the exam, it assumes variables and arrays are all setup

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