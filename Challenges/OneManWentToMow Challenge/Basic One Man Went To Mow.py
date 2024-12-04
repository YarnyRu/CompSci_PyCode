# Program to print out the lyrics to "One man went to mow"
men = 0
verse = 1
maxmen = 5

for men in range (1, maxmen+1):
    print( men, "men went to mow, went to mow a meadow,")
    for rep_men in range(verse, 0, -1):
        print(verse, "men,", end=" ")
    print("and his dog, Spot, went to mow a meadow.")
    verse = verse + 1