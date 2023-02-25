# Day 2 Exercise 2 - Calculating the BMI
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))
BMI = int(weight / (height ** 2))
print(BMI)