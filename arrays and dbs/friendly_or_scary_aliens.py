import random
alien_array = [""] * 6
attribute_array = [""] * 6
line_num = 0
with open('aliens.txt', 'r') as file_nickname:
  for line in file_nickname:
    line = line.strip()
    #print(line)
    elements = line.split()
    alien_array[line_num] = elements[0]
    attribute_array[line_num] = elements[1]
    line_num += 1
    #print("I met a", elements[0], "and they were", elements[1])
choice = random.randint(0, line_num - 1)
#print(choice)
print(alien_array)
print(attribute_array)
#print("I met a", alien_array[choice], "and they were", attribute_array[choice])