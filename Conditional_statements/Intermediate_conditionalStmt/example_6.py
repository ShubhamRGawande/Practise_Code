# Program to calculate electricity bill

units = int(input("Enter electricity usage in units : "))

if units <= 100:
    print(f"Bill is {units * 1.5}")
elif units <= 200:
    print(f"Bill is {(units - 100) * 2.5}")
elif units <= 300:
    print(f"Bill is {100 * 1.5 + 100 * 2.5 + (units - 200) * 4}")
else:
    print(f"Bill is {100 * 1.5 + 2.5 * 100 * 4 + (units - 300) * 6}")