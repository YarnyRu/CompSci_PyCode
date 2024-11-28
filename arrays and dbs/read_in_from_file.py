# Simple 'database' table input
# This program reads in from data.txt one line at a time
name = [""] * 5
paper1 = [0] * 5
row_count = 0
with open('data.txt', 'r') as f:
  for line in f:
    line = line.strip()
    record = line.split()
    #print(record[0])
    name[row_count] = record[0]
    paper1[row_count] = int(record[1])
    row_count += 1   #increment row_count to the next empty space in the array
print(name)
print(paper1)