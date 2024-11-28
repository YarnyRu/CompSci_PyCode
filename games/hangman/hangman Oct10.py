#HANGMAN by Xander 10th Oct 2019
guesses = 10
underscores = 9
secret_word = ['m','i','n','e','c','r','a','f','t']
hangman_word = ['_','_','_','_','_','_','_','_','_']
while underscores > 0 or guesses > 0:
  right_guess = False
  user_guess = input('what letter would you like to guess? ')
  for i in range(0,9):
    if user_guess == secret_word[i]:
      #letter guessed correctly
      hangman_word[i] = user_guess
      right_guess = True
      print(hangman_word)
      underscores = underscores - 1
  #this code runs after the for loop
  if right_guess == False:
    #user guess was not in the word
    guesses = guesses - 1
    print(user_guess, 'was not in the word')
    print('you have', guesses, 'remaining')
#this code runs after the while loop
  if underscores == 0:
    print('You guessed the word!')
    print(secret_word)
    break
else:
  print('You lost...')
