# Program to check if a character is a digit

char = input("Enter the single character : ")
if len(char) == 1:
    if char.isdigit():
        print(f"the character '{char}' is a digit.")
    else:
        print(f"the character '{char}' is not a digit.")
else:
    print("invalid character..")