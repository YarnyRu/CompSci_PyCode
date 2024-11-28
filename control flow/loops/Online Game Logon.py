# Logon for an online game
# Initialisation values
Name = "This is the default value which is longer than 8"
Age = -99
Nickname = "This is the default value which is longer than 8"

#REPEAT
#  PRINT "Enter your name, using 8 characters or less"
#  INPUT Name
#UNTIL Length(Name) <= 8

while len(Name) > 8:
  Name = input("Enter your name, using 8 characters or less: ")

#REPEAT
#  PRINT "Enter your age in years"
#  INPUT Age
#UNTIL Age > 5 AND Age < 128

while Age < 5 or Age >= 128:
  Age = int(input("Enter your age in years: "))

#REPEAT
#  PRINT "Enter your nickname, using 8 characters or less"
#  INPUT Nickname
#UNTIL Length(Nickname) <= 8

while len(Nickname) > 8:
  Nickname = input("Enter your nickname, using 8 characters or less: ")

#PRINT "Do you want to use your name (enter TRUE) or your nickname (enter FALSE)"
#INPUT Choice

Choice = input("Do you want to use your name (enter TRUE) or your nickname (enter FALSE): ")

#IF Choice = TRUE THEN
#  PRINT "Welcome", Name, "aged", Age
#ELSE
#  PRINT "Welcome", Nickname, "aged", Age
#ENDIF

if Choice == "TRUE":
  print("Welcome", Name, "aged", Age)
else:
  print("Welcome", Nickname, "aged", Age)