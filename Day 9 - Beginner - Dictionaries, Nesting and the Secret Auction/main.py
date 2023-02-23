# Day 9 - Dictionaries and nested blocks
# Video code - The Python Dictionary: Deep Dive:

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running",
    "Function": "A peice of code that you can easily call over and over again"
}

programming_dictionary["Loop"] = "The action of doing something over and over again"        # adding data to a dictionary
print(programming_dictionary)

# programming_dictionary = {}     # removing all data from a dictionary

programming_dictionary["Bug"] = "A moth in your computer"       # reassinging data in a dictionary
print(programming_dictionary, "\n")

for key in programming_dictionary:        # looping through a dictionary only gives the key
    print(key)
    print(programming_dictionary[key])

# Separating code - Nesting Lists and Dictionaries:
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuggart"]
}
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12, 
        "last_visit_date": "01/02/22"
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuggart"], 
        "total_visits": 5, 
        "last_visit_date": "09/12/2017"
    }
]
print(travel_log[0])

# Exercise 1 - Grading Program:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for name in student_scores:
    if student_scores[name] > 90 :
        student_grades[name] = "Outstanding"
    elif student_scores[name] > 80 :
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] > 70 :
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)

# Exercise 2 - Dictionary in List:
travel_log = [          # same list as in video code
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    add_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }

    travel_log.append(add_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Day 9 Project 
import art
import os

clear = lambda: os.system('cls') #on Windows System

print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}
another_bidder = "yes"
while (another_bidder.lower() == "yes"):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    clear()

highest_bid = 0
highest_bidder = ""     # stores the name of the highest bidder
for x in bidders:           # x iterates through all the names stored as a key value in the bidders dictionary
    if bidders[x] > highest_bid:
        highest_bid = bidders[x]
        highest_bidder = x

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
# print(bidders)