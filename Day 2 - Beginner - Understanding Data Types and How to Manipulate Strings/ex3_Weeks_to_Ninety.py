# Day 2  Exercise 3 - Weeks in Life:

age = int(input("What is your current age? "))
years_to_90 = 90 - age
days_to_90 = years_to_90 * 365      # (365 days/year)
weeks_to_90 = years_to_90 * 52      # (52 weeks/year)
months_to_90 = years_to_90 * 12     # (12 months/year)

print(f"You have {days_to_90} days, {weeks_to_90} weeks, and {months_to_90} months left to 90.")