#Milk Round Code
import math
number_of_accidentsA = 0
number_of_cratesA = 0
number_of_bottlesA = 0
number_of_pintsA = 0
#length_of_A
#Set up data arrays
MilkRoundA = [3, 2, 6, 3, 4, 2, 12, 8, 4, 19, 2, 2, 4, 1, 0, 3, 1, 4, 4,]
len(MilkRoundA)
for i in range(0,len(MilkRoundA)):
    number_of_pintsA = number_of_pintsA + MilkRoundA[i]
print("the number of pints you need to take is", number_of_pintsA)
#How many crates
number_of_cratesA = math.ceil(number_of_pintsA / 16)
print("you will need", number_of_cratesA, "crates")
#how many bottles you can break
number_of_accidentsA = (number_of_cratesA * 16) - number_of_pintsA 
print("and you can break", number_of_accidentsA, "bottles.") 


#Now add which customer wants the most milk
#Calculate weekly average for each customer
#Who didn't order any milk this week?
#Total milk dellivery across the whole round
