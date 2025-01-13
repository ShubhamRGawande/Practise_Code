# Program to check if a character is an alphabet, digit, or special character
char = input("Enter a single character : ")
if len(char) == 1:
    if char.isalpha():
        print(f"This character '{char}' is alphabet.")
    elif char.isdigit():
        print(f"This character '{char}' is digit.")
    else:
        print(f"This character '{char}' is special character.")
else:
    print("invalid input.please enter a single character.")