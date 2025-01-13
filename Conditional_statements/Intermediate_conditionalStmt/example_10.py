# Program to calculate grade based on marks
marks = float(input("Enter your marks (out of 100) : "))

if 90 <= marks <= 100:
    print("Grade : A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
elif 50 <= marks < 60:
    print("Grade E")
else:
    print("Grade F")