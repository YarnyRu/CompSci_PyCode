#Diana's Hex Converter August 2019
import math

#Set up data array
HexDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

#Initialising variables
DecNumber = 0
HexDigitLen = len(HexDigits)
Run = True

while Run == True:
    #User entry of Hex value to convert
    print("Which hex number would you like to convert to denary?")
    HexNumber = input("Please enter 3 digits max: ").upper()
    HexNumLen = len(HexNumber) 
    DecNumber = 0

    #Validation & Verification checks
    ValidHex = True
    for j in range(0, HexNumLen):
        ValidChar = False
        #Check to see if HexNumber[j] is one of the accepted values
        for k in range(0, HexDigitLen):
            if HexDigits[k] == HexNumber[j]:
                ValidChar = True
        if ValidChar == False:
            #This digit was not valid so the whole number is invalid
            # print(HexNumber[j], "is not a valid hexadecimal digit")
            ValidHex = False
    
    if ValidHex == False:
        print(HexNumber, "is not a valid hexadecimal number.")
    else:	# ValidHex is True
        if HexNumLen > 3:
            print("Hex value exceeded maximum size")
            ValidHex = False
        elif HexNumLen == 3:
        #Conversion for a 3 digit hex number
            for i in range(0, HexDigitLen):
                if HexDigits[i] == HexNumber[0]:
                    DecNumber = i * 256
            for i in range(0, HexDigitLen):
                if HexDigits[i] == HexNumber[1]:
                    DecNumber = DecNumber + (i * 16)   
            for i in range(0, HexDigitLen):
                if HexDigits[i] == HexNumber[2]:
                    DecNumber = DecNumber + i
        elif HexNumLen == 2:
        #Conversion for a 2 digit hex number
            for i in range(0, HexDigitLen):
                if HexDigits[i] == HexNumber[0]:
                    DecNumber = DecNumber + (i * 16)   
            for i in range(0, HexDigitLen):
                if HexDigits[i] == HexNumber[1]:
                    DecNumber = DecNumber + i
        elif HexNumLen == 1:
        #Conversion for a 1 digit hex number   
            for i in range(0, HexDigitLen):
                if HexDigits[i] == HexNumber[0]:
                    DecNumber = DecNumber + i
        else:
            print("Input invalid")
    
        if ValidHex == True:
            print(HexNumber, "is", DecNumber, "in denary")

    UserContinue = input("Would you like to convert another value? Y/N ")
    if UserContinue.upper() == 'Y':
        Run = True
    else:
        Run = False
print("Thank you for using my hex converter!")
