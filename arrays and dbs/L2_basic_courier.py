#Courier code
# List containing all the deliveries to do and how many parcels are delivered to each address
delivery_round = [1, 1, 2, 0, 4, 2, 3, 1, 6, 1]

# Calculate how many addresses are included in today's round
addresses = len(delivery_round)
print("There are", addresses, "houses in today's round")

houses = 0
packages = 0
round_length = addresses * 4

for p in range(0, addresses):
  # Calculate how many packages should be on the van at the start of the round
  packages = packages + delivery_round[p]
  # Calculate how many actual houses are receiving a delivery (list must not contain a 0)
  if p != 0:
    houses += 1
  # Calculate length of the round, if each delivery takes 4 mins on average, with an extra minute for more than 2 parcels
  if p > 2:
    round_length += 1  

# correct for any 0s in the list
round_length -= 4 * (addresses - houses)

print("You ACTUALLY have", houses, "houses to deliver to today")
print("You are delivering", packages, "packages today")
print("Your round should take you", round_length, "minutes")