# ISBN checker and generator... tbc
ISBN = [9, 7, 8, 1, 3, 7, 0, 6, 4, 5, 8, 2]
odd_total = 0
even_total = 0

for i in range(len(ISBN)):
  if i % 2 == 0:	# number is even
      even_total += ISBN[i]
  else:
      odd_total += ISBN[i]

print(odd_total)
print(even_total)
ISBN_total = even_total + 3*odd_total
remainder = ISBN_total %10
print("Total of", ISBN_total, "remainder in modulo 10 is", remainder, "so check digit is", 10 - remainder) 