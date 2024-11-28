import random
animal_list = ["aardvark", "baboon", "chimp", "dolphin", "elephant"]
animal = random.choice(animal_list)
num = random.randint(10, 99)
gamer_tag = animal+str(num)
print("Your new gamer tag is:", gamer_tag)