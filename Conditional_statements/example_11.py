# Program to check if a number is a three-digit number
number = int(input("Enter a number :"))
if 100 <= abs(number) <= 999:
    print(f"The number {number} is a three digit number.")
else:
    print(f"The number {number} is not a three digit number.")
