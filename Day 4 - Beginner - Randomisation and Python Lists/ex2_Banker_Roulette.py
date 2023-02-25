# Day 4 - Exercise 2 - Banker Roulette:
import random

names = input("Give me everybody's names, separated by a comma & space. ")
list_names = names.split(", ")

# rand_choice = random.randint(0, len(list_names)-1)
# A more efficient way to do this is to use the random.choice() method, it automatically chooses one of multiple options:
rand_choice = random.choice(list_names)

print(f"{rand_choice} is going to buy the meal today!")
# print(f"{list_names[rand_choice]} is going to buy the meal today!")