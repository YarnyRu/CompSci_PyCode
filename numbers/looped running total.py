number = 0
running_total = 0
for i in range(1,4):
    number = int(input('please enter a number '))
    running_total = running_total + number
    print('the running total of those numbers is...',running_total)
print('the average of these numbers is..',running_total / 3)

