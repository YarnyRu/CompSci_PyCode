# One Man Went to Mow

for verse in range (1, 6, 1):
    # This is going to be repeated in this for loop
    print(verse, "men went to mow, went to mow a meadow,")
    for i in range(verse, 0, -1):
        print(i, "men,", end = " ")
    print("and his dog, Spot, went to mow a meadow\n")
# Code after here happens after the loop has finished
print("This is the end of the song")