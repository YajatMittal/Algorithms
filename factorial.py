def factorial():
    factorial_num = int(input("Please enter a number -->"))
    numbers = [x for x in range(1,factorial_num+1)]
    
    if factorial_num == 0:
        print("The factorial of 0 is 1")
    
    elif factorial_num < 0:
        print("Factorial of negatives don't exist")

    else:
        while len(numbers) != 1:
            calculate = numbers[0] * numbers[1]
            numbers.pop(0)
            numbers.pop(0)
            numbers.append(calculate)

        print(f"The factorial of {factorial_num} is {numbers[0]}")
    

factorial()