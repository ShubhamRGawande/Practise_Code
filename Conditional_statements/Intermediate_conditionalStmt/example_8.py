# Program to determine the type of quadrilateral

side1 = float(input("Enter the first side :"))
side2 = float(input("Enter the second side :"))
side3 = float(input("Enter the third side :"))
side4 = float(input("Enter the fourth side :"))

if side1 == side2 == side3 == side4:
    print("Its an sqaure.")
elif side1 == side3 and side2 == side4:
    print("Its an rectangle.")
else:
    print("its an irregular quadrilateral.")