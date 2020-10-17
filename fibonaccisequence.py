def fib(n):
  numbers = [0,1]
  for i in range(0,n+1):
    addition = numbers[i] + numbers[i+1]
    numbers.append(addition)
  
  print(numbers[n])

fib(100)