# Festival Tickets
# Under 12s go free
# Age 12 - 17 = Youth Ticket
# Age 18 - 59 = Adult Ticket
# Age 60+ = OAP Ticket
print("Welcome to the festival bookings")
print("We are taking bookings for Glastonbury NOW!")
age = int(input("How old are you? "))
if age < 12:
  print("You get a free ticket - yay!")
elif age < 18:
  print("You need to buy a youth ticket")
elif age < 60:
  print("You need to buy an adult ticket")
else:
  print("You need to buy an OAP ticket")