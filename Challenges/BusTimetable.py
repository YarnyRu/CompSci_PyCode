#Bus A Timetable Example

#Fill the arrays with the data
BusA_Data = [0, 0, 0, 2, 2, 4, 0, 3, 4, -2, -5, 0, 0, 3, 4, -1, 8, 1, 1, -2]
BusB_Data = [0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0]
BusC_Data = [2, 0, -1, -1, -2, -2, -3, -1, 0, 0, -2, 0, 1, 1, 1, 1, -1, -1, 2, -2] 
BusD_Data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
BusE_Data = [-1, -1, -1, -2, -4, -10, -2, 0, 0, 0, 0, 1, 2, -3, 1, 1, 3, -1, 0, 0]
BusF_Data = [0, -5, -5, -5, -4, -3, -5, 0, 0, 0, 0, -2, -3, 1, 1, 1, 0, 0, -2, -5]

#Initialise variables
TotalMinsLateA = 0
TotalMinsLateB = 0
TotalMinsLateC = 0
TotalMinsLateD = 0
TotalMinsLateE = 0
TotalMinsLateF = 0
BusA_Late_Count = 0
BusA_Late_Sum = 0
BusB_Late_Count = 0
BusB_Late_Sum = 0
BusC_Late_Count = 0
BusC_Late_Sum = 0
BusD_Late_Count = 0
BusD_Late_Sum = 0
BusE_Late_Count = 0
BusE_Late_Sum = 0
BusF_Late_Count = 0
BusF_Late_Sum = 0

Counter = 0

#Run through each day of the timetable and sum total late times

for index in range (0, 20):
    Counter = Counter + 1
    TotalMinsLateA = TotalMinsLateA + BusA_Data[index]
    TotalMinsLateB = TotalMinsLateB + BusB_Data[index]
    TotalMinsLateC = TotalMinsLateC + BusC_Data[index]
    TotalMinsLateD = TotalMinsLateD + BusD_Data[index]
    TotalMinsLateE = TotalMinsLateE + BusE_Data[index]
    TotalMinsLateF = TotalMinsLateF + BusF_Data[index]

    #Check if bus A was late that day
    if BusA_Data[index] < 0 :
        #If it was, count that day and add the late minutes to the sum
        BusA_Late_Count = BusA_Late_Count + 1
        BusA_Late_Sum = BusA_Late_Sum + BusA_Data[index]

    #Check if bus B was late that day
    if BusB_Data[index] < 0 :
        #If it was, count that day and add the late minutes to the sum
        BusB_Late_Count = BusB_Late_Count + 1
        BusB_Late_Sum = BusB_Late_Sum + BusB_Data[index]

    #Check if bus C was late that day
    if BusC_Data[index] < 0 :
        #If it was, count that day and add the late minutes to the sum
        BusC_Late_Count = BusC_Late_Count + 1
        BusC_Late_Sum = BusC_Late_Sum + BusC_Data[index]

    #Check if bus D was late that day
    if BusD_Data[index] < 0 :
        #If it was, count that day and add the late minutes to the sum
        BusD_Late_Count = BusD_Late_Count + 1
        BusD_Late_Sum = BusD_Late_Sum + BusD_Data[index]

    #Check if bus E was late that day
    if BusE_Data[index] < 0 :
        #If it was, count that day and add the late minutes to the sum
        BusE_Late_Count = BusE_Late_Count + 1
        BusE_Late_Sum = BusE_Late_Sum + BusE_Data[index]

    #Check if bus F was late that day
    if BusF_Data[index] < 0 :
        #If it was, count that day and add the late minutes to the sum
        BusF_Late_Count = BusF_Late_Count + 1
        BusF_Late_Sum = BusF_Late_Sum + BusF_Data[index]


#End of for loop

#Work out which bus was late most frequently
LateArrivals = [BusA_Late_Count, BusB_Late_Count, BusC_Late_Count, BusD_Late_Count, BusE_Late_Count, BusF_Late_Count]
BusList = ["A", "B", "C", "D", "E", "F"]

print (LateArrivals)

WorstBus = 0

for index in range (0, 6):
    if LateArrivals[index] > WorstBus :
        WorstBus = index


print ("Worst Bus EVER was" , BusList[WorstBus])


#Print out results
if TotalMinsLateA > 0 :
    print ("Bus A was" , TotalMinsLateA / Counter , "minutes early on average")
else :
    print ("Bus A was", TotalMinsLateA / Counter , "minutes late on average")

print ("Bus A was late ", BusA_Late_Count, " times")
print ("When the bus was late, it averaged a ", BusA_Late_Sum / BusA_Late_Count, " minute delay")
