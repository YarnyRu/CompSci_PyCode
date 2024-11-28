hangman_word = ['b', 'a', 'n', 'a', 'n' ,'a', 's',]
answer = ['_', '_', '_', '_', '_', '_', '_']
underscores = 7
turns_taken = 0
while underscores > 0 and turns_taken < 10:
    print(answer)
    letter_count = 0
    user_entry = input('what letter would you like to search for ')   
    turns_taken = turns_taken + 1  
    for i in range(0,7):
        if hangman_word[i] == user_entry:
            if answer[i] == '_':
                answer[i] = user_entry
                underscores = underscores - 1
                if underscores == 0:
                    print('you guessed correctly')
if underscores > 0:
    print('you did not guess the word')
print(hangman_word)
