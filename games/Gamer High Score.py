# Catan Board Gamer's High Score Program
# Read in a score from the user (number / integer)
score = int(input("What is your score?: "))

# IF score is the highest score EVER, print out a "Wow!" message
if score > 10000:
  print("Top score EVER!")

# IF score is greater than <average>, print out praise message
elif score > 5000:
  print("Awesome job!")

# IF score is greater than <minimum>, print out encouragement message
elif score > 0:
  print("Good try, better luck next time")

else:
  print("What happened there?")
