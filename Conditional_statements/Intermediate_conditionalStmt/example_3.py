# Program to check if a number is an Armstrong number
number = int(input("Enter the number :"))
temp = number
sum_of_powers = 0

#cal the sum of power of the digits
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit**len(str(number))
    temp //= 10

#check if number is armstorng or not
if sum_of_powers == number:
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")