days_of_christmas = [['first', 'A partridge in a pear tree.'], ['second', 'Two turtle doves, and'],
           ['third', 'Three French hens,'], ['fourth', 'Four calling birds,'],
           ['fifth', 'Five gold rings,'], ['sixth', 'Six geese a-laying,'],
           ['seventh', 'Seven swans a-swimming,'], ['eighth', 'Eight maids a-milking,'],
           ['ninth', 'Nine ladies dancing,'], ['tenth', 'Ten lords a-leaping,'],
           ['eleventh', 'Eleven pipers piping,'], ['twelfth', 'Twelve drummers drumming,']]

day = int(input('What day of Christmas is it? (1-12) ')) - 1 
print("On the {} day of Christmas my true love sent to me: ".format(days_of_christmas[day][0]))
for gift in range(day, -1, -1):          
    print(days_of_christmas[gift][1])
    
    