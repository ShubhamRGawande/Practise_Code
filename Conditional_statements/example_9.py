# Program to calculate grade based on marks
marks = float(input("Enter your marks (0-100):"))
if 90 <= marks <= 100:
    print("grade A")
elif 80 <= marks < 90:
    print("grade B")
elif 70 <= marks < 80:
    print("grade C")
elif 60 <= marks < 70:
    print("grade D")
elif 0 <= marks < 60:
    print("FAil")
else:
    print("Entered invalid marks")
