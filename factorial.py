def factorial():
    factorial_num = int(input("Please enter a number -->"))
    numbers = [x for x in range(1,factorial_num+1)]
    

    while len(numbers) != 1:
        
        calculate = numbers[0] * numbers[1]
        numbers.pop(0)
        numbers.pop(0)
        numbers.append(calculate)
    
    print(numbers)
    

factorial()