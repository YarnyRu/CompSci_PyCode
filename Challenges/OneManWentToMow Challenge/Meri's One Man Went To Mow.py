# One man went to mow
# Initiating variables
men = 0
repeat = 1
rep_men = 0
length = int(input("How many men? "))
if length > 100:
  print("I'm not going to print out more than 100 men, think again.")
else:
  # Main loop to print the basic lines
  for men in range (0, length):
    if men+1 == 1:
      print(men+1, "man went to mow,")
    else:
      print( men+1, "men went to mow,")
    print("Went to mow a meadow,")
    # Loop for the third line, to repeat men
    for rep_men in range(repeat, 0, -1):
      if rep_men == 1:
        print(rep_men, "man", end=" ")
      else:
        print(rep_men, "men", end=" ")
    print("and his dog, Woof!")
    #Last line
    print("Went to mow a meadow.")
    repeat = repeat + 1
    
PROGRAM OUTPUT
    
How many men? 5
1 man went to mow,
Went to mow a meadow,
1 man and his dog, Woof!
Went to mow a meadow.
2 men went to mow,
Went to mow a meadow,
2 men 1 man and his dog, Woof!
Went to mow a meadow.
3 men went to mow,
Went to mow a meadow,
3 men 2 men 1 man and his dog, Woof!
Went to mow a meadow.
4 men went to mow,
Went to mow a meadow,
4 men 3 men 2 men 1 man and his dog, Woof!
Went to mow a meadow.
5 men went to mow,
Went to mow a meadow,
5 men 4 men 3 men 2 men 1 man and his dog, Woof!
Went to mow a meadow.    