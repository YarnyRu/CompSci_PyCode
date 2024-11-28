# Number guessing game, min and max values are programmable
import random
minimum = 1
maximum = 100
num = int(random.randint(minimum, maximum))
print("Welcome to my number guessing game!")
found = False
max_tries = 4
tries = 0
while found == False and tries < max_tries:
    print("Please guess a number between", minimum, "and", maximum)  
    guess = int(input())
    if guess == num:
        print("You guessed correctly!")
        found = True
    elif guess > num:
        print("Too high!")
        tries += 1
    elif guess < num:
        print("Too low!")
        tries += 1
if found == False:
    print("The number you were looking for was", num)                                                                                 
