# Summer Term Skills REQUIRES SCORES.TXT
# Prep work - learn how to read in from a text file
# with open("file.txt") as f:
# .strip()    getting rid of extra spaces/line breaks
# .split()    dividing up a line into a list of elements, default separator = space

scores = [0] * 5
running_total = 0
score_count = 0
highest_score = -999
lowest_score = 999

score_num = 0
with open('scores.txt') as f:
  for line in f:
    line = line.strip()
    if line[0] == "#":
      print(line)
    else:
      scores[score_num] = int(line)
      score_num += 1

# Top score calculations
for i in range (0, 5):
  if scores[i] < 0:
    print("Score of", scores[i], "invalid")
    scores[i] = 0
  else:
    running_total += scores[i]
    score_count += 1
    if scores[i] > highest_score:
      highest_score = scores[i]
    if scores[i] < lowest_score:
      lowest_score = scores[i]
      
score_avg = running_total / score_count
print("The average score was", score_avg)
print("Highest score was", highest_score)
print("Lowest score was", lowest_score)



# Summer Term Skills
# Prep work - learn how to read in from a text file
# with open("file.txt") as f:
# .strip()    getting rid of extra spaces/line breaks
# .split()    dividing up a line into a list of elements, default separator = space

scores = [0] * num_of_lines
names = [""] * num_of_lines
print(scores)
print(names)
score_num = 0
running_total = 0
highest_score = -9999

with open("scores.txt") as f:
  for line in f:
    line = line.strip()
    temp_data = line.split()
    print(temp_data)
    scores[score_num] = int(temp_data[0])
    names[score_num] = temp_data[1]
    running_total = running_total + scores[score_num]
    if scores[score_num] > highest_score:
      highest_score = scores[score_num]
      highest_scorer = names[score_num]
    score_num += 1
print(scores)
print("Mean average is", running_total / 5)
print("Highest score is", highest_score, "scored by", highest_scorer)