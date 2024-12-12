days_of_christmas = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
                     'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

gifts_of_christmas = ['a partridge in a pear tree.', 'Two turtle doves, and ', 'Three French hens, ',
                    'Four calling birds, ', 'Five gold rings\n', 'Six geese a-laying, ',
                    'Seven swans a-swimming, ', 'Eight maids a-milking, ', '\nNine ladies dancing, ',
                     'Ten lords a-leaping, ', 'Eleven pipers piping, ', 'Twelve drummers drumming, ']


#print("On the {} day of Christmas my true love sent to me: ".format(days_of_christmas[day]))
#for gift in range(day, -1, -1):          
#    print(gifts_of_christmas[gift])
lyrics = ''

for i in range(0, 12):
  print('\nOn the', days_of_christmas[i], 'day of Christmas, my true love sent to me...')
  # "On the {} day of Christmas, my true love sent to me...".format(days_of_christmas[day])
  lyrics = gifts_of_christmas[i] + lyrics
  print(lyrics)