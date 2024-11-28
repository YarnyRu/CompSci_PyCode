# Code to print emojis
print(":-D")
print('\N{T-Rex}'*10)
penguin = '\N{penguin}'
# Finding out the Unicode for the penguin emoji
value = ord(penguin)
print("The Unicode for", chr(value), "is", value)
# Finding out the Unicode for the user's choice of emoji
emoji = input("Please enter a funky emoji: ")
value = ord(emoji)
print("The Unicode for", chr(value), "is", value)