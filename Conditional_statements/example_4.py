# Program to check if a character is a vowel or consonant
char = input("Enter  the single character : ")
if char.isalpha() and len(char) == 1:
    char = char.lower()
    if char in 'aeiou':
        print(f"The character '{char}' is vowel.")
    else:
        print(f"The character '{char}' is consonant.")
else:
    print("Invalid input. please enter a single character alphabet character.")

