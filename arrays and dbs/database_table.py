# SIMPLE DATABASE TABLE
# Use data.txt to store the database table values, columns separated by spaces
# e.g. Student scores for mock papers 1 and 2
#      Jim  49  62
#      Fred 55  59
#      Bob  62  67

# 1. How many lines are in the text file? This is equal to the number of records (=rows) in the table
# Note either DO NOT put headers or field names in the file OR use # to comment it out and set up your
# code to ignore rows that start with #

record_number = 0
with open('data.txt', 'r') as f:
    for line in f:
        if line[0] != "#":
            record_number += 1
    print("There are", record_number, "records in this table")

# 2. Set up database arrays, 1D arrays for each field (=column) in the table
    database_field1 = [""] * record_number      # To store student names
    database_field2 = [0] * record_number        # To store paper 1 scores
    database_field3 = [0] * record_number        # To store paper 2 scores
    row_count = 0
    
# 3. Read in each line, strip off white space, split into columns and store each field in its 1D array
with open('data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line[0] == "#":
            print(line)
        else:
            print(line)
            record_entry = line.split()
            database_field1[row_count] = record_entry[0]
            database_field2[row_count] = int(record_entry[1])
            database_field3[row_count] = int(record_entry[2])
            row_count += 1

# 4. Print out each record using the appropriate index (up to a max of record_number)
for i in range (0, record_number):
    print("Student", database_field1[i], "scored", database_field2[i], "on paper 1, and", database_field3[i],
           "on paper 2")