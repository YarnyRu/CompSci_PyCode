#Courier code

delivery_round = [1, 1, 2, 0, 4, 2, 3, 0, 6, 1]
addresses = len(delivery_round)
print("There are", addresses, "houses in today's round")
houses = 0
packages = 0
round_length = addresses * 4

for p in range(0, addresses):
  packages = packages + delivery_round[p]
  if delivery_round[p] != 0:
    houses += 1
  if delivery_round[p] > 2:
    round_length += 1  

round_length -= 4 * (addresses - houses)
print("You ACTUALLY have", houses, "houses to deliver to today")
print("You are delivering", packages, "packages today")
print("Your round should take you", round_length, "minutes")