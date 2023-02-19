# # # Day 3 - Control Flow

# # # Video Code - Control Flow with if / else and Conditional Operators:
# # print("Welcome to the rollercoaster!")
# # height = int(input("What is your height in cm? "))

# # bill = 0

# # if height >= 120:
# #     print("You can ride the rollercoaster!")

# #     # Separating Code - Nested if statements and elif statements
# #     age = int(input("What is your age? "))
# #     if (age >= 45) and (age <= 55):
# #         bill = 0
# #         print(f"Tickets are ${bill}")
# #     elif (age <= 12):
# #         bill = 5
# #         print(f"Child tickets are ${bill}.")
# #     elif (age <= 18):
# #         bill = 7
# #         print(f"Youth tickets are ${bill}.")
# #     else:
# #         bill = 12
# #         print(f"Adult tickets are ${bill}.")

# #     wants_photo = input("Do you want a photo taken? Y or N.")
# #     if wants_photo == "Y":
# #         bill += 3

# #     print(f"Your total bill is: ${bill}")

# # else:
# #     print("Sorry, you have to grow taller before you can ride.")



# # # Exercise 1 - Odd or Even:
# # num = int(input("Which number do you want to check? "))

# # if (num % 2 == 0):
# #     print("This is an even number.")
# # else:
# #     print("This is an odd number.")

# # # Exercise 2 - BMI 2.0:
# # weight = float(input("Enter your weight in kilograms (kg): "))
# # height = float(input("Enter your height in meters (m): "))
# # bmi = round(weight / (height ** 2))

# # interpret = ""
# # if bmi < 18.5:
# #     interpret = "you are underweight"
# # elif bmi < 25:
# #     interpret = "you have a normal weight"
# # elif bmi < 30:
# #     interpret = "you are overweight"
# # elif bmi < 35:
# #     interpret = "you are obese"
# # else:
# #     interpret = "you are clinically obese"

# # print(f"Your BMI is {bmi}, {interpret}")

# # # Exercise 3 - Leap Year:
# # year = int(input("Which year do you want to check? "))

# # if (year % 4 == 0):
# #     if year % 100 == 0:

# #         if year % 400 == 0:
# #             print("Leap year.")
# #         else:
# #             print("Not leap year.")
# #     else:
# #         print("Leap year.")

# # else:
# #     print("Not leap year.")

# # # Exercise 4 - Pizza Order Practice:
# # print("Welcome to Python Pizza Deliveries!")
# # size = input("What size pizza do you want? S, M, or L ")
# # add_pepperoni = input("Do you want pepperoni? Y or N ")
# # extra_cheese = input("Do you want extra cheese? Y or N ")

# # pizza = 0

# # if size == "S":
# #     pizza = 15
# #     if add_pepperoni == "Y":
# #         pizza += 2

# # elif size == "M":
# #     pizza = 20
# #     if add_pepperoni == "Y":
# #         pizza += 3

# # elif size == "L":
# #     pizza = 25
# #     if add_pepperoni == "Y":
# #         pizza += 3

# # if extra_cheese == "Y":
# #     pizza += 1

# # print(f"Your final bill is: ${pizza}")


# # Exercise 5 - Love Calculator:
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# name1 = name1.upper()
# name2 = name2.upper()

# true_count = 0
# lo_count = 0

# # My solution:
# # true_count += name1.count("T")
# # true_count += name2.count("T")
# # true_count += name1.count("R")
# # true_count += name2.count("R")
# # true_count += name1.count("U")
# # true_count += name2.count("U")
# # true_count += name1.count("E")
# # true_count += name2.count("E")

# # lo_count += name1.count("L")
# # lo_count += name2.count("L")
# # lo_count += name1.count("O")
# # lo_count += name2.count("O")
# # lo_count += name1.count("V")
# # lo_count += name2.count("V")
# # lo_count += name1.count("E")
# # lo_count += name2.count("E")

# # Better solution more efficient:
# combine_string = name1 + name2
# true_count += combine_string.count("T")
# true_count += combine_string.count("R")
# true_count += combine_string.count("U")
# true_count += combine_string.count("E")

# lo_count += combine_string.count("L")
# lo_count += combine_string.count("O")
# lo_count += combine_string.count("V")
# lo_count += combine_string.count("E")
# # End of difference between solutions
# score =int(str(true_count) + str(lo_count))

# if (score < 10) or (score > 90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")

# Day 3 Project - Treasure Islaand:
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
if cross_road.lower() == "left":
    lake = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    
    if lake.lower() == "wait":
        doors_3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n')

        if doors_3.lower() == "red":
            print("You entered a room of lava. Came Over.")
        elif doors_3.lower() == "blue":
            print("You entered a room of beasts. Game Over.")
        elif doors_3.lower() == "yellow":
            print("Congratulations! You found the treasure.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You were eaten by the lockness monster. Game Over.")
else:
    print("You fell into a hole. Game Over.")