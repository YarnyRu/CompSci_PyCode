numbers = [5,6,8,3,4,2,7,1,]
temp = 0
swapped = True
user_entry = input('do you want to use your own data? yes or no. ')
if user_entry == 'yes':
    for i in range (0,8):
        numbers[i] = input('please enter a number ')

else:
    print('we will use our own numbers')





print("here is the list",numbers)
while swapped == True:
    swapped = False
    for i in range(0,7):
        #print(numbers[i])
        if(numbers[i]) > (numbers[i + 1]):
            #print('we need to swap the numbers')
            swapped = True
            temp = (numbers[i + 1])
            (numbers[i + 1]) = (numbers[i])
            (numbers[i]) = temp

print(numbers)

        
    
    
