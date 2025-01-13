# Program to check if a point lies inside a circle

x_center, y_center = map(float, input("Enter the center of the circle (x y): ").split())
radius = float(input("Enter the radius of the circle : "))

x_point, y_point = map(float, input("Enter the points coordinates (x y): ").split())

distance = ((x_point - x_center)**2 + (y_point - y_center)**2)**0.5

if distance < radius:
    print("the point lies on the circle.")
elif distance == radius:
    print("the point lies on the circle.")
else:
    print("the point lies outside the circle.")