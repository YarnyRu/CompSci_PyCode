print("this an OR gate simulator")
check = "NO"
check2 = "NO2"
while check == "NO":
    print("please use '1' or '0' ")
    answerA = int(input("what is answer 'a' "))
    if answerA == 1 or answerA == 0:
        check = "YES"
    else:
        print("invalid data")
    
while check2 == "NO2":
    print("please use '1' or '0' ")
    answerB = int(input("what is answer 'b' "))
    if answerB == 1 or answerB == 0:
        check2 = "YES2"
    else:
        print("invalid data")

if answerA == 0 and answerB == 0:
    print("0")
else:
    print("1") 
