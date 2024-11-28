# Simple 'database' table input
# This program reads in from speeds.txt one line at a time

number_plates = [""] * 50
speeds = [0] * 50
vehicle_index = 0
old_speeder = 0
aging_speeder = 0
nearly_new_speeder = 0
new_speeder = 0
non_speeders = 0
total_cars = 0
speed_limit = 40

with open('speeds.txt', 'r') as file_nickname:
  for line in file_nickname:
    line = line.strip()
    elements = line.split()
    number_plates[vehicle_index] = elements[0]
    plate = number_plates[vehicle_index]
    speeds[vehicle_index] = int(elements[1])
    year = int(plate[2:4])
    if year > 50:
        year -= 50
    age = 24 - year
    print(elements[0], "age", age, "was travelling at", elements[1], "mph")
    if speeds[vehicle_index] > speed_limit:
        if age > 10:
            old_speeder += 1
        elif age > 5:
            aging_speeder += 1
        elif age > 3:
            nearly_new_speeder += 1
        else:
            new_speeder += 1
    else:
        non_speeders += 1
    vehicle_index += 1
total_cars = non_speeders + old_speeder + aging_speeder + nearly_new_speeder + new_speeder
if total_cars != vehicle_index:
    print("Error in vehicle total", total_cars)
print(f'Speeding cars over 10 years old - {old_speeder}')
print(f'Speeding cars over 5 years old - {aging_speeder}')
print(f'Speeding cars over 3 years old - {nearly_new_speeder}')
print(f'Speeding cars under 3 years old - {new_speeder}')
print(f'Cars not speeding - {non_speeders}')