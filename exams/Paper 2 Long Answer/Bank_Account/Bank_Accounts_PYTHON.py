
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
# Input and validate account name and password
name = input("Please enter your account name: ")
for i in range(0, Size):
    if name == Account[i][0]:
        print("Account holder found at index", i)
        pwd = input("Please enter your password: ")
        if pwd != Account[i][1]:
            print("Password is incorrect")
        else:
            print("Password is correct")
            print("Please select from one of the following options:")
            print("1. display balance \n2. withdraw money \n3. deposit money \n4. exit")
            choice = int(input("> "))
            if choice == 1:			#Display balance
                print(f'Your balance is £{AccDetails[i][0]}')
            elif choice == 2:		# Withdraw money
                #Calculate max withdrawal available using overdraft
                available = AccDetails[i][0] + AccDetails[i][1] 
                if available > AccDetails[i][2]:		#Check against withdrawal limit
                    available = AccDetails[i][2]		#Set withdrawal amount to limit
                print(f'You can withdraw £{available}')
                print(f'Your balance is £{AccDetails[i][0]}')
                if available > 0:
                    withdraw = float(input("How much would you like to withdraw? "))
                    if withdraw > 0:
                        if withdraw <= available:
                            AccDetails[i][0] -= withdraw
                            print(f'You now have a balance of £{AccDetails[i][0]}')
            elif choice == 3:		# Deposit money
                deposit = float(input("How much would you like to deposit? "))
                if deposit > 0:
                    AccDetails[i][0] += deposit
                    print(f'Your balance is now £{AccDetails[i][0]}')
            else:
                #Exit or error
                print("Goodbye")