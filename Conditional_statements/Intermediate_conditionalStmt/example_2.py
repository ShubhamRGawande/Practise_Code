# Program to check if a triangle is valid based on angles
angle1 = float(input("Enter the first angle : "))
angle2 = float(input("Enter the second angle : "))
angle3 = float(input("Enter the third angle : "))

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("triangle is valid.")
else:
    print("the triangle is not valid.")