# # Video code - Namespaces: Local vs. Global Scope: 
# player_health = 10      # vairable with global scope, not within a function
# def health():
#     health_potion = 2   # variable with local scope, not accessible outside this function

# print(player_health)
# # print(health_potion)

# # Seaparating code - Does Python Have Block Scope?
# # Python does not have block scope
# # if a variable is created within an if-statement or while-loop it is accessible anywhere within the same function

# enemies = ["Skeleteons", "Zombies", "aliens"]
# level = 3
# if level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)


# no_enemies = 1
# def increase_enemies():
#     global no_enemies       # it's a bad practice modify a vairbale with global scope within a function

#     no_enemies += 1
#     print(f"enemies inside the function {no_enemies}")
# increase_enemies()
# print(f"enemies outside the function {no_enemies}")

# # Constants are variables that don't change throughout the program, the naming convention for defining constants is to use all UPPERCASE
# PI = 3.14159
# GOOGLE_URL = "https://www.google.com"



# Day 12 Project - 
import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

NUMBER = random.randint(1, 100)
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_choice.lower() == "easy":
    attempts = 10
else:
    attempts = 5
# user_guess = int(input("Make a guess: "))

def guess (user_guess, attempts_left):
    global NUMBER

    if user_guess == NUMBER:
        print(f"You got it! The answer was {NUMBER}")
        return
    elif user_guess > NUMBER:
        print(f"Too high.")
    elif user_guess < NUMBER:
        print(f"Too low.")

    attempts_left  -= 1
    if (attempts_left == 0):
        print("You've run out of guesses, you lose")
        return

    print("Guess again")
    print(f"You have {attempts_left} attempts remaining to guess the number.")
    guess(user_guess=int(input("Make a guess: ")), attempts_left=attempts_left)


user_guess = int(input("Make a guess: "))
guess(user_guess, attempts)























# if difficulty_choice.lower() == "easy":
#     for tries in range(10):
#         user_guess = int(input("Make a guess: "))
#         guess(user_guess=user_guess, attempts=tries)

