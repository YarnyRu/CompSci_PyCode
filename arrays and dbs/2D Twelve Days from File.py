# TWELVE DAYS OF CHRISTMAS
#
# 1. How many lines are in the text file? This is equal to the number of records (=rows) in the table
# Note either DO NOT put headers or field names in the file OR use # to comment it out and set up your
# code to ignore rows that start with #

rows = 0
columns = 0
with open('Twelve Days Data.txt') as f:
  for line in f:
    if line[0] != "#":
      line = line.strip()
      record_entry = line.split(',')
      columns = len(record_entry)
      rows += 1
  print("There are", rows, "records and", columns, "fields in this table")

# 2. Set up a 2D array for the days of Christmas data
days_of_christmas = [""] * rows    
columns = columns - 1
days_of_christmas = [["" for i in range (rows)] for j in range(columns)]
print(days_of_christmas)


# 3. Read in each line, strip off white space, split into columns and store each field in its 1D array
row_count = 0
with open('Twelve Days Data.txt') as f:
  for line in f:
    line = line.strip()
    if line[0] != "#":
      record_entry = line.split(',')
      #this is where we would validate data before permanent storage
      days_of_christmas[0][row_count] = record_entry[0]
      days_of_christmas[1][row_count] = record_entry[1]
      row_count += 1

for i in range (rows-1, 0, -1):
  new_message = "On the " + days_of_christmas[0][i] + "day of Christmas, my true love sent to me:" + days_of_christmas[1][i]
  message = new_message + message
  print(message)
