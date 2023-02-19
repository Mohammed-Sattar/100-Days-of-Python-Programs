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



# Exercise 1 - Heads or Tails:
coin_side = random.randint(0,1)

if (coin_side == 1):
    print("Heads")
else:
    print("Tails")

# Exercise 3 - Banker Roulette:
names = input("Give me everybody's names, separated by a comma & space. ")
list_names = names.split(", ")
# rand_choice = random.randint(0, len(list_names)-1)
# A more efficient way to do this is to use the random.choice() method, it automatically chooses one of multiple options:
rand_choice = random.choice(list_names)
print(f"{rand_choice} is going to buy the meal today!")
# print(f"{list_names[rand_choice]} is going to buy the meal today!")

# Exercise 4 - Treasure Map:
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

coloumn = int(position[0]) -1
row = int(position[1]) - 1
# print(row, coloumn)
map[row][coloumn] = "x"
print(f"{row1}\n{row2}\n{row3}")


# Day 4 Project - Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
computer_choice = random.randint(0,2)

if user_choice in (0, 1, 2):
    print(f"{choices[user_choice]}\n")
    print(f"Computer chose: \n{choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw")    
    elif (user_choice - 1 == computer_choice) and (user_choice - 1 >= 0):
        print("You win.")
    elif (user_choice == 0) and (computer_choice == 2):
        print("You win")
    else:
        print("You lose")
else:
    print("Invalid Value")