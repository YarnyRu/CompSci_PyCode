BABY = 1
TODDLER = 2
CHILD = 5
TEENAGER = 13
ADULT = 21
OLD = 50

 
name = input ("Please enter your name: ")

age = input ("how old are you? ")
age = int(age)

age_dif = age - BABY
message = "you were a baby %s years ago"
print (message % age_dif)

print ("you were a toddler", age - TODDLER,"years ago.")

if age > CHILD:
    print ("you were a child", age - CHILD,"years ago.")

if age > TEENAGER:
    print ("you were a teenager", age - TEENAGER,"years ago.")

if age > ADULT:
    print ("you were a adult", age - ADULT,"years ago.")

if age > OLD:
    print("you are very old!")
