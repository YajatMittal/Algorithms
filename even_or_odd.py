def even_or_odd():
    active = True
    while active:
        try:
            user_input  = int(input("Enter a number:"))
    
        except:
            print("Ivalid Input!")
            continue
        
        else:
            active = False  
    
    if user_input % 2 == 0:
        print(f"{user_input} is even!")
    
    else:
        print(f"{user_input} is odd!")

even_or_odd()