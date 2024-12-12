letters = "The quick brown fox jumped over the lazy dog."
letter_count = 0
user_entry = input('Which letter of the alphabet would you like to search for? :').lower()
print(letters)
maxnum = len(letters)
for i in range(0, maxnum):
    if letters[i] == user_entry:  #count this as a match
        letter_count = letter_count + 1
if letter_count == 1:
    print('Letter',user_entry, 'occurs once')
else:
    print(f'Letter {user_entry} occurs {letter_count} times')