#Park Run Pre-Release Code - August 2019
#Children register with name and age (4-14)
#4 digit identification number per runner, last digit is a check digit
#Each time they run, the time is recorded and number of runs is incremented
#Personal Best (PB) time is updated if necessary
#After 11 runs a half-marathon wristband is awarded, 22 runs gets a full marathon
#Identify the fastest child for age 4 to 6, 7 to 10, and 11 to 14.
#Start with 20 children

#Task 1 - Registration to take part
#Name, Age, ID, PB=0.00, Number of Runs=0

NumberOfChildren = 4
Name = ['_'] * NumberOfChildren
Age = [0] * NumberOfChildren
ID = ['_'] * NumberOfChildren
PB = [0.00] * NumberOfChildren
ParkRuns = [0] * NumberOfChildren

print("Please register each child now")
for i in range (0, NumberOfChildren):
    Name[i] = input("Runner's Name: ")
    Age[i] = int(input("Runner's Age: "))
    #Find out how to take first character from a string in an array
    IDName = Name[i]
    if i < 10:
        IDNum = '0' + str(i)
    else:
        IDNum = str(i)
    ID[i] = IDName[0:1] + IDNum
    PB[i] = float(0.00)
    ParkRuns[i] = int(0)

#print(Name)
#print(Age)
print(ID)

#Task 2 - Recording the times
#Unique ID and start and finish times
print("Please enter run times for each runner ID")
Run = True

while Run == True:
    ThisID = 0
    ThisRunner = input("Enter runner ID: ")
    for j in range(0, NumberOfChildren):
        if ID[j] == ThisRunner:
            #We have found the correct runner
            ThisID = j
            print("Runner", Name[ThisID], "has ID", ID[ThisID])
    StartTime = float(input("Please enter the start time: "))
    FinishTime = float(input("Please enter the finish time: "))
    RaceTime = FinishTime - StartTime
    print("Race time = ", RaceTime)
    if RaceTime > PB[ThisID]:
        PB[ThisID] = RaceTime
    data = (Name[ThisID], Age[ThisID], ID[ThisID], PB[ThisID])
    format_string = "Runner %s (age %d) with ID '%s' has a PB of %.2f"
    print(format_string % data)
    UserContinue = input("Would you like to enter more data? Y/N ")
    if UserContinue == 'N':
        Run = False
    elif UserContinue == 'n':
        Run = False
    else:
        Run = True
