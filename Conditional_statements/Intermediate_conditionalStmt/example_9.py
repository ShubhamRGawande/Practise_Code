# Program to calculate BMI and determine weight category
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in metres : "))

bmi = weight / (height**2)

if bmi < 18.5:
    print(f"your BMI is {bmi :.2f}. YOu are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi :.2f}. You have normal weight.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi :.2f}. You are Overweight.")
else:
    print(f"Your BMI is {bmi :.2f}. You are obese.")