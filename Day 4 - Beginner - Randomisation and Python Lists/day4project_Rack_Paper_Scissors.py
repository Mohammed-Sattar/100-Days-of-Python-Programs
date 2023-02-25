
# Day 4 Project - Rock Paper Scissors
import random

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