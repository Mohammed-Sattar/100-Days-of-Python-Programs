# Day 3 - Exercise 2 - BMI 2.0:
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))
bmi = round(weight / (height ** 2))

interpret = ""
if bmi < 18.5:
    interpret = "you are underweight"
elif bmi < 25:
    interpret = "you have a normal weight"
elif bmi < 30:
    interpret = "you are overweight"
elif bmi < 35:
    interpret = "you are obese"
else:
    interpret = "you are clinically obese"

print(f"Your BMI is {bmi}, {interpret}")