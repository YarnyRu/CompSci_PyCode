# This is an algorithm, written in Python, that reads in a username and allows the user 3 password attempts, then stops.
fail = 0
pwd_check = False
stored_pwd = "Bob1"
username = input("Please enter your username: ")
while pwd_check == False and fail < 3:
    password = input("Please input your password: ")
    if password != stored_pwd:
        fail += 1
        print("Password Incorrect")
    else:
        print("Password Accepted")
        pwd_check = True
if fail == 3:
    print("You have reached the maximum number of attempts")