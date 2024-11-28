#Milk Cart code
import math
milk_round = [1, 5, 8, 0, 12, 4]
bottles = 0
total_bottles = 0
crates = 0
round_length = 0
spares = 0
houses = len(milk_round)
for i in range (0, houses):
  bottles = bottles + milk_round[i]
  if milk_round[i] > 0:
    round_length = round_length + 1
crates = math.ceil(bottles/16)
total_bottles = crates * 16
spares = total_bottles - bottles
print("You have", round_length, "deliveries to make today")
print("You need to load", crates, "crates containing", total_bottles, "bottles of milk on to your cart")
print("You are delivering", bottles, "bottles today so you have", spares, "spare")