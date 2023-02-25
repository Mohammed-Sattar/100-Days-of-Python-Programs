# Day 12 Project - The Number Guessing Game:
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
