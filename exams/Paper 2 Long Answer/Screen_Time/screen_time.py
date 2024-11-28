# SCREEN TIME Paper 22 March 2024
# Variables given in paper, StudentName[], ScreenTime[][], ClassSize
ClassSize = 3
week_length = 5

StudentName = ["Bob", "Jim", "Fred"]
ScreenTime = [[0 for x in range(week_length)] for y in range(ClassSize)]

# Initialise variables
lowest_minutes = 1000
class_total = 0

for student_counter in range(0, ClassSize): # loop for each student
    total = 0
    days_over_300 = 0
    print(StudentName[student_counter])
    for day_counter in range(0, week_length): # loop for each day
        minutes = -1
        while minutes < 0:
            prompt = "Please enter number of minutes for day " + str(day_counter + 1) + ": "
            minutes = int(input(prompt))     # Validate minutes, range check
        ScreenTime[student_counter][day_counter] = minutes  # save into 2D array
        total += minutes                     # calculate running total
        if minutes > 300:
            days_over_300 += 1               # increment tally of days over 300 minutes
        if minutes < lowest_minutes:
            lowest_minutes = minutes
            lowest_index = student_counter    # remember which student had the lowest minutes
    # end of day loop
    print("Screen time:", total//60, "hours and", total % 60, "minutes")
    print("Days with more than 300 minutes screen time: ", days_over_300)
    class_total += total
# end of student loop

# Print results at the end of the program
print(ScreenTime)
#print("Average weekly screen time for class:", class_total / ClassSize, "minutes")
avg = class_total / ClassSize
print("Average weekly screen time for class:", avg//60, "hours and", avg % 60, "minutes")
print("Lowest weekly time:", StudentName[lowest_index])
