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
