# Program to check if a number is divisible by both 5 and 11
number = int(input("Enter the number : "))
if number % 5 == 0 and number % 10 == 0:
    print(f"The number {number} is divisible by both 5 and 10.")
else:
    print(f"The number {number} is not divisible by both 5 and 10.")