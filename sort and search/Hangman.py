#HANGMAN VERSION 2 BY DIANA July 2019
import random
word_list = ["beetroot", "cabbage", "apricot", "snozzcumber", "potato", "mandarin", "blackberry", "radish", "pineapple"]
chosen_word = random.randint(0,len(word_list)-1)
whole_word = word_list[chosen_word]
whole_word_len = len(whole_word)
#print ("Your word is number", chosen_word+1, "in the list and is", whole_word_len, "characters long")

#This answer needs to be in the form of an array (list) as assignment can't be done on
# individual characters in a string data type

answer = ['_'] * whole_word_len

max_fails = 3
print("You lose if you guess", max_fails, "wrong letters")

underscores = whole_word_len
fails = 0
while underscores > 0 and fails < max_fails:
    #letter_count = 0
    user_entry = input("What letter would you like to search for? ")
    found = False
    for i in range(0, whole_word_len):
        if whole_word[i] == user_entry:
            # A matching letter has been found in the hangman word
            #letter_count += 1
            found = True
            if answer[i] == '_':
                # Replace an underscore with the letter in the printed answer
                answer[i] = user_entry
                underscores = underscores - 1
    if found == False:
        print("I'm sorry", user_entry, "was not in the word.")
        fails += 1
    if underscores == 0:
        print("You guessed correctly! It was", word_list[chosen_word])
    else:
        print (answer)

if underscores > 0:
    print("You did not guess the word, it was", word_list[chosen_word])
#print(word_list[chosen_word])
