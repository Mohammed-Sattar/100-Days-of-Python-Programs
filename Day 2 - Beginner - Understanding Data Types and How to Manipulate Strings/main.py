# Day 2 - Python Primitive Data Types

# Python Primitive Data Types
# String
print("Hello"[3])
# Integer
# len(233)
print("123" + "456")
print(123 + 456)
# Float
pi = 3.1415
print(pi)
#Boolean
x = True

# Separating code - Type Error, Type Checking and Type Conversion:
num_char = len(input("What is your name? "))
print(type(num_char))
new_num = str(num_char)
print("Your name has " + new_num + " characters.")

x = 3.1414
print(type(x))

print(100 + float("70.5"))
print(str(70) + str(100))
print("----\n")

# Separating code - Mathematical Operations in Python:
# 4 + 2
# 4 - 2
# 4 * 2
# 4 / 2
# 4 // 2
# 4 ** 2

# Separating code - Number Manipulation and F Strings in Python
print(round(8/3, 2))
print(8//3)
height = 1.8
isWining = True
age = 12
print(f"You are {age} years old, your height is {height}, and you are winning is {isWining}")


# # Exercise 1 - Data Types 
num = input("Type a 2 digit number: ")
digit1 = str(num)[0]
digit2 = str(num)[1]
print(int(digit1) + int(digit2))

# Exercise 2 - Calculating the BMI
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))
BMI = int(weight / (height ** 2))
print(BMI)

# Exercise 3 - Weeks in Life:

age = int(input("What is your current age? "))
years_to_90 = 90 - age
days_to_90 = years_to_90 * 365      # (365 days/year)
weeks_to_90 = years_to_90 * 52      # (52 weeks/year)
months_to_90 = years_to_90 * 12     # (12 months/year)

print(f"You have {days_to_90} days, {weeks_to_90} weeks, and {months_to_90} months left to 90.")


# Day 2 Project - Tip Calculator
print("Welcome to the tip calculator.")
price = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
people_split = int(input("How many people to split the bill? "))

tip_amount = price * (tip_percentage/100)
sum = price + tip_amount
# total_per_person = round((sum / people_split), 2)
total_per_person = "{:.2f}".format(sum / people_split)# This formating always gives 2 decimals, whereas the previous will 1 decimal if price is exact

print(f"Each person should pay: ${total_per_person}")
