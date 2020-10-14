user_input = input("Enter a number/word:").lower()
if user_input == user_input[::-1]:
    print("PALINDROME!")

else:
    print("NOT A PALINDROME!")