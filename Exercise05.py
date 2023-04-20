
# Task 1
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))

sum_of_nums = num1 + num2 + num3

print("Sum of the numbers:", sum_of_nums)

#Task 2
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if num1 > num2:
    print("First number is greater!")
elif num2 > num1:
    print("Second number is greater!")
else:
    print("Numbers are equal!")
    
if num1 > 10000 and num2 > 10000:
    print("Numbers are beeeeeeg!")

# Task 4
month_name = input("Enter the name of a month: ")

days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

if month_name in days_in_month:
    print(f"{month_name} has {days_in_month[month_name]} days.")
else:
    print("Invalid month name entered.")


# Task 5
number = int(input("Enter a number: "))

if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is even and divisible by 3.")
else:
    print(f"{number} is not even and/or not divisible by 3.")
