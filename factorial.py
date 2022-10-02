def factorial():
    factorial_num = int(input("Please enter a number:"))
    
    if factorial_num == 0:
        print("The factorial of 0 is 1")
    elif factorial_num < 0:
        print("Factorial of negatives don't exist")    
    else:
        for x in range(1,factorial_num):
            factorial_num *= x
        print(factorial_num)
        
factorial()
