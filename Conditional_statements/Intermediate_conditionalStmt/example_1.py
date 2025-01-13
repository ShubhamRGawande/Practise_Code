# Program to find the roots of a quadratic equation
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b : "))
c = float(input("Enter coefficient c : "))

discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print(f"the root are real and distinct : {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"the root are real and equal : {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"the roots are complex : {real_part} + {imaginary_part}i")