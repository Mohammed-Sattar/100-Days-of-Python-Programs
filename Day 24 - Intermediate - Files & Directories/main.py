# file = open(r"Day 24 - Intermediate -\file.txt")
# contents = file.read()
# print(contents)
# file.close()

# A more efficient and preferred way to open and access files in Python:
# path = r"C:\Users\User\Desktop\Mohammed\Coding\100 Days of Python\Day 24 - Intermediate -\main.py"
# with open(r"C:\Users\User\Desktop\file.txt") as file:
#     contents = file.read()
#     print(contents)

# Challenge: backtracking to Desktop to find file.txt
with open("../../../file.txt") as file:
    contents = file.read()
    print(contents)

# if a file doesn't exist when you try opening it with write mode, it will be created
# with open(r"Day 24 - Intermediate -\new_file.txt", mode="w") as file:
#     file.write("New Text.")

