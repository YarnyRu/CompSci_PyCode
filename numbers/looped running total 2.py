#initialising variables
user_number = 0 
number = 0
running_total = 0
run = False
#valication check
while run == False: 
    user_number = int(input('how many numbers do you want? '))
    if user_number > 20: 
        print('please enter a number less than 20')
    else:
        run = True
#keeping a running total
for i in range(1,user_number + 1):
    number = int(input('please enter number '))
    running_total = running_total + number
    print('the running total of those numbers is...')
    print(running_total)
#calculating the average
print('the average of these numbers is..')
print(running_total / user_number)
