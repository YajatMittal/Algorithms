def even_or_odd():
    while True:
        try:
            user_input  = int(input("Enter a number:"))
        except:
            print("Ivalid Input!")
            continue
        else:
            break  
    
    if user_input % 2 == 0:
        print(f"{user_input} is even!")
    
    else:
        print(f"{user_input} is odd!")

even_or_odd()
