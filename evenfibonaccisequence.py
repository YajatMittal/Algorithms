#here are the two most important variables for the fibonacci sequence
numbers = [1,2]
even_numbers = []

#here is a for loop running until the fibonacci sequence's value exceeds 4 million
for x in range(0,4000000):
    addition = numbers[x] + numbers[x+1]
    numbers.append(addition)
    
    #here I am appending the even number values in the fibonacci sequence into a list
    if x % 2 == 0:
      even_numbers.append(x)

#this is thw last step where I am finding the sum of the even numbers
print(even_numbers)

