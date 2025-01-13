# Program to check if a character is uppercase or lowercase
char = input("Enter a single alphabet character :")

if char.isalpha() and len(char) == 1:
    if char.isupper():
        print(f"the character '{char}' is uppercase")
    else:
        print(f"the character '{char}' is lowercase")
else:
    print("invalid input.")