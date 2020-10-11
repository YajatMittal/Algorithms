word_input = str(input("Enter a word/phrase:"))
letter_input = str(input("Enter a letter:"))

letter_count = 0

for x in word_input:
    if x.lower() == letter_input.lower():
        letter_count += 1

print(f"There are {str(letter_count)} {letter_input}'s in {word_input} ")
