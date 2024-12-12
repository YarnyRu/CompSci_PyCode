#Diana's Denary to Hexadecimal Converter August 2019
import math

#Set up data array
HexDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
HexDigitLen = len(HexDigits)

#Initialising variables
DecNumber = 0
#HexNumber[] = ""
Run = True

while Run == True:
    MultiplesOf256 = 0
    MultiplesOf16 = 0
    UnitsOf1 = 0
    Range = True
    #User entry of Decimal value to convert
    print("Which decimal number would you like to convert to hex?")
    DecNumber = int(input("Please enter 4 digits max: "))
    #HexNumLen = len(HexNumber) 

    #Validation Range Check
    if DecNumber < 0:
        print("Invalid number, please try again")
        Range = False
    elif DecNumber >= 4096:
        print("Number too large, please try again")
        Range = False
    elif DecNumber < 16:
        HexLen = 1
    elif DecNumber < 256:
        HexLen = 2
    elif DecNumber < 4096:
        HexLen = 3
        
    if Range == True:
        if HexLen == 3:
            MultiplesOf256 = math.floor(DecNumber/256)
            HexChar1 = HexDigits[MultiplesOf256]
            Remainder = DecNumber - MultiplesOf256 * 256
            MultiplesOf16 = math.floor(Remainder/16)
            HexChar2 = HexDigits[MultiplesOf16]
            Units = Remainder - MultiplesOf16 * 16
            HexChar3 = HexDigits[Units]
            print(DecNumber, "is", HexChar1 + HexChar2 + HexChar3, "in hex")
        if HexLen == 2:
            MultiplesOf16 = math.floor(DecNumber/16)
            HexChar1 = HexDigits[MultiplesOf16]
            Units = DecNumber - MultiplesOf16 * 16
            HexChar2 = HexDigits[Units]
            print(DecNumber, "is", HexChar1 + HexChar2, "in hex")
        if HexLen == 1:
            HexChar1 = HexDigits[DecNumber]
            print(DecNumber, "is", HexChar1, "in hex")
            
    UserContinue = input("Would you like to convert another value? Y/N ")
    if UserContinue == 'N':
        Run = False
    elif UserContinue == 'n':
        Run = False
    else:
        Run = True
print("Thank you for using my hex converter!")
