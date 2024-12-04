#Diana's Milk Cart Code August 2019
import math

#Set up data arrays
MilkRoundA = [3, 2, 4, 1, 1, 6, 4, 8, 0, 1, 2, 2, 4, 1, 0, 3, 1, 4, 4, 2]
RoundALen = len(MilkRoundA)

#Initialising variables
TotalPintsA = 0 

#Summing up the pints of milk ordered in the milk round (running total)
for i in range(0,RoundALen):
    TotalPintsA = TotalPintsA + MilkRoundA[i]

print("Milk Round A is delivering", TotalPintsA, "pints to", RoundALen, "homes.")

#Calculating the number of crates required
TotalCratesA = TotalPintsA // 16 + 1
print("This round requires", TotalCratesA, "crates to be loaded onto the cart")
if TotalCratesA > 32:
    print("You will need more than one milk cart")
elif TotalCratesA > 16:
    print("You will need to use both ends of the cart")
else:
    print("You only need to use one end of the cart")
    
#Calculating the number of spare pints
SparePintsA = TotalCratesA*16 - TotalPintsA
print("You have", SparePintsA, "pints spare in this round.")
