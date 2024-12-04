#Bus Timetable Example

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

DayCount = 0

#Add up total minutes late for average number of minutes late

for index in range (0, 20):
    TotalMinsLateA = TotalMinsLateA + BusA_Data[index]
    TotalMinsLateB = TotalMinsLateB + BusB_Data[index]
    TotalMinsLateC = TotalMinsLateC + BusC_Data[index]
    TotalMinsLateD = TotalMinsLateD + BusD_Data[index]
    TotalMinsLateE = TotalMinsLateE + BusE_Data[index]
    TotalMinsLateF = TotalMinsLateF + BusF_Data[index]

    if BusA_Data[index] < 0 :
        BusA_Late_Count = BusA_Late_Count + 1
        BusA_Late_Sum = BusA_Late_Sum + BusA_Data[index]

    if BusB_Data[index] < 0 :
        BusB_Late_Count = BusB_Late_Count + 1
        BusB_Late_Sum = BusB_Late_Sum + BusB_Data[index]

    if BusC_Data[index] < 0 :
        BusC_Late_Count = BusC_Late_Count + 1
        BusC_Late_Sum = BusC_Late_Sum + BusC_Data[index]

    if BusD_Data[index] < 0 :
        BusD_Late_Count = BusD_Late_Count + 1
        BusD_Late_Sum = BusD_Late_Sum + BusD_Data[index]

    if BusE_Data[index] < 0 :
        BusE_Late_Count = BusE_Late_Count + 1
        BusE_Late_Sum = BusE_Late_Sum + BusE_Data[index]

    if BusF_Data[index] < 0 :
        BusF_Late_Count = BusF_Late_Count + 1
        BusF_Late_Sum = BusF_Late_Sum + BusF_Data[index]
