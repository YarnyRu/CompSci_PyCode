#High score gaming program
print("Super Mario High Score Chart")
score = int(input("Please enter your highest score: "))
if score < 0:
  print("Weird...")
elif score < 500:
  print("Keep it up, you're doing well for a noob")
elif score < 1000:
  print("You're not bad at this game!")
elif score < 5000:
  print("You're a pro!")
else:
  print("HACKER!")