# Day 13 - Debugging:

############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):    
#     if i == 20:         # before debugging not within the for loop range, never reaches 20
#       print("You got it")
# my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)        # before dubugging the number 6 is out of range of the list
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:          # before debugging it was always checking if greater or less than, but never equal to
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? "))     # before debugging input not converted to int
# if age > 18:
#     print(f"You can drive at age {age}.")     # before debugging not using f string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))       # before debugging using the comparison == operator, no assignment =
# print(f"pages= {pages} \t words per page= {word_per_page}")     # use this line to find were the problem is
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])