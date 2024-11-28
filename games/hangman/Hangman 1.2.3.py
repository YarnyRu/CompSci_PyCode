hangman_word = ['h', 'a', 'n', 'g', 'm' ,'a', 'n',]
answer = ['_', '_', '_', '_', '_', '_', '_']
underscores = 7
while underscores > 0:
    print(answer)
    letter_count = 0
    user_entry = input('what letter would you like to search for ')   
    for i in range(0,7):
        if hangman_word[i] == user_entry:
            answer[i] = user_entry
            underscores = underscores - 1
            if underscores == 0:
                print('you guessed correctly')
                






    #if letter_count == 1:
       # print(user_entry,'appeared', letter_count, 'one time')
   # elif letter_count == 0:
       # print(user_entry, 'did not appear')
    #else:
        #print(user_entry, 'appeared', letter_count, 'times')
