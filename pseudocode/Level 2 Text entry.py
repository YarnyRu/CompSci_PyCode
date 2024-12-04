#// Level 2 challenge, complete Level 1 first, then make these improvements
#// This is an algorithm, written in Python, that reads in a username and checks that the user is in the array
#// If the user exists, it allows the user 3 password attempts, then stops.
Users = ["Bob", "Jim", "Fred", "Sam"]
Passwords = ["Bob1", "Jimminy", "Froggo", "SamTheGreat"]

UserCheck = False
Fail = 0
PwdCheck = False
UserName = input("Please enter username: ")

for Index in range(0, 4):
    if Users[Index] == UserName:
        UserCheck = True
        UserIndex = Index
        print("User found at index", Index)

if UserCheck == True:
    while PwdCheck == False and Fail < 3:
        Password = input("Please enter password: ")
        if Password == Passwords[UserIndex]:
            print("Password Accepted")
            PwdCheck = True
        else:
            print("Password Incorrect")
            Fail += 1
    if Fail == 3:
        print("You have reached the maximum number of attempts")
else:
    print("User not found")