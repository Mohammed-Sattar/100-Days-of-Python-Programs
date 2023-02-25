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