numbers = [6,4,8,2,3,1,5,7]
temp = 0
swapped = True
print("this is my mixed up list",numbers)
while swapped == True:
    swapped = False
    for i in range(0,7):
        #print(numbers[i])
        if(numbers[i]) > (numbers[i + 1]):
            swapped = True
            temp = (numbers[i + 1])
            (numbers[i + 1]) = (numbers[i])
            (numbers[i]) = temp

print(numbers)

        
    
    
