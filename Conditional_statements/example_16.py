# Program to check if a number is divisible by 2 or 3
number = int(input("Enter a number :"))
if number % 2 == 0 or number % 3 == 0:
    print(f"the number {number} is divisible by 2 or 3")
else:
    print(f"the number {number} is not divisible by 2 or 3")
