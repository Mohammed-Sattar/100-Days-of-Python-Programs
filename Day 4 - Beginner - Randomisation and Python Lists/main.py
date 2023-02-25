import random
import my_module

# Video Code - Random Module:
random_int = random.randint(1, 10) # Returns a random integer in range [a, b], including both end points.
print(random_int)

# touched on explanation of modules and importing them to explain the random module
print(my_module.pi)       

random_float = random.random()      # a random float number between 0 and 1 (1 is excluded)
print(random_float)

rand_5 = random.randint(0,4) + random.random()          #one solution: printing a random float number between 0 and 5
random_5 = random.random() * 5          #another solution
print(rand_5)       #printing a random float number between 0 and 5

# Separating code - Understanding the Offset and Appending Items to Lists:
us_states = ["Delaware", "Pennslyvania", "New Jersey", "Georgia", "Connticut", "Massachussetts"]    # Whenever we have squre brackets, it means its related to lists
print(us_states[0])         # The index tells us the offset of data from the start, Delaware is the 1st so it's 0 elements from the start

us_states.append("Maryland")
print(us_states)
us_states.extend(["South Carolina", "New Hampshire", "Virginia"])
print(us_states)

# Separating code - IndexErrors and Working with Nested Lists:
# dirty_dozen = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Pears", "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(f"{dirty_dozen[0][0]} & {dirty_dozen[0][-3]} are Yum!")

