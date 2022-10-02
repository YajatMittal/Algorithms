 def factorial(n):
  if n > 1: 
    n *= factorial(n-1)
  else:
    if n == 0:
      print("The factorial of 0 is 1")
    elif n < 0:
      print("Factorial of negatives don't exist")  
  return n

print(factorial(5))
