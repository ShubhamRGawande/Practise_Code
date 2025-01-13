# Program to check if a number is a palindrome
number = int(input("Enter the number : "))
reverse_number = int(str(number)[::-1])

if number == reverse_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not palindrome.")