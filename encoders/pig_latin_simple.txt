# Pig Latin Translator
# User enters a word and the code translates it into Pig Latin
# Remove first letter, then print rest of word, then add first letter, then add ay
# e.g. hello -> ellohay
#      how  -> owhay
#      are  -> areyay
#      you  -> ouyay
word = input("Please enter a word to turn into Pig Latin: ")
first = word[0]
rest = word[1:]
print(first, rest)
print(f'{rest}{first}ay')