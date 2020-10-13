numbers = [1,2]
even_numbers = []

for x in range(0,4000000):
  for a in numbers:
    addition = numbers[x] + numbers[x+1]
    numbers.append(addition)
    
    if a % 2 == 0:
      even_numbers.append(a)

print(even_numbers)

