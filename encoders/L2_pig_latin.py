# Pig Latin Translator
# User enters a word and the code translates it into Pig Latin
# Remove first letter, then print rest of word, then add first letter, then add ay
# All in lower case
word = input("Please enter a word: ")
restofword = word[1:]
first = word[0]
if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
  newword = word + "way"
else:
  newword = restofword + first + "ay"
print(newword.lower())
