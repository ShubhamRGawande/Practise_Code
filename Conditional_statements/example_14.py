# Program to check if a year is a century year
year = int(input("Enter a year :"))
if year % 100 == 0:
    print(f"the year {year} is a century year.")
else:
    print(f"the year {year} is not a century.")