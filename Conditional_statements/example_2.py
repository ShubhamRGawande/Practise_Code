# Program to find the largest of two numbers
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
if num1 > num2:
    print(f"The largest number is {num1}")
elif num1 < num2:
    print(f"The larger number is {num2}")
else:
    print("Both the numbers are equal.")