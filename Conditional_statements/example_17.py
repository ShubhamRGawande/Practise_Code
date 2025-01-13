# Program to check the type of triangle based on its sides
side1 = float(input("Enter the side of the triangle :"))
side2 = float(input("Enter the side of the triangle :"))
side3 = float(input("Enter the third side of the triangle :"))
if side1 == side2 == side3:
    print("the triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("the triangle is isosceles.")
else:
    print("the triangle is scalene")