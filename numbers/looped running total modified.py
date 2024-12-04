number = 0
running_total = 0
user_number = int(input("how many numbers do you want? "))
for i in range(1,user_number+1):
    number = int(input('please enter a number '))
    running_total = running_total + number
    print('the running total of those numbers is...',running_total)
print('the average of these numbers is..',running_total / user_number)

