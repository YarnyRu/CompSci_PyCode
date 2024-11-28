letters = ['d', 'j', 'a', 's', 'b', 'x', 'a', 'h', 'w', 'm', 'a', 'n', 'r', 'q', 'e', 't', 'y', 'd', 'e', 'y', 'q', 'j',
        'o', 'u', 'e', 'd', 's', 'b', 'm', 'z', 'v','i','a', 'f', 'u', 'o', 'g']
letter_count = 0
user_entry = input('what letter would you like to search for ').lower()
print(letters)
maxnum = len(letters)
for i in range(0, maxnum):
    if letters[i] == user_entry:  #count this as a match
        letter_count = letter_count + 1
if letter_count == 1:
    print('we found',user_entry, letter_count, 'time')
else:
    print('we found',user_entry, letter_count, 'times')