# Day 3 - Exercise 4 - Pizza Order Practice:
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza = 0

if size == "S":
    pizza = 15
    if add_pepperoni == "Y":
        pizza += 2

elif size == "M":
    pizza = 20
    if add_pepperoni == "Y":
        pizza += 3

elif size == "L":
    pizza = 25
    if add_pepperoni == "Y":
        pizza += 3

if extra_cheese == "Y":
    pizza += 1

print(f"Your final bill is: ${pizza}")