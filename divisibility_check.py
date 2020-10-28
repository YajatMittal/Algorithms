def divisibility_check():
    active = True
    divisible_by = []
    while active:
        try:
            num = int(input("Enter a number:"))
        except:
           print("Invalid!")
           continue

        else:
            active = False
    for x in range(1,10):
        if num %  x == 0:
            divisible_by.append(x)
    
    print(f"{num} is divisble by {str(divisible_by)}")

divisibility_check()