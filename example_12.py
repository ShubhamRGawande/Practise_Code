# Program to check if a number is positive and even
number = int(input("Enter the number :"))
if number > 0 and number % 2 == 0:
    print(f"the number {number} is positive and even.")
else:
    print(f"the number {number} is not positive and even.")