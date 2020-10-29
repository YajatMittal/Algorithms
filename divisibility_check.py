def divisibility_check(num):
    divisible_by = []
    for x in range(1,num+1):
        if num %  x == 0:
            divisible_by.append(x)
    
    print(f"{num} is divisble by {str(divisible_by)}")

divisibility_check(100)
