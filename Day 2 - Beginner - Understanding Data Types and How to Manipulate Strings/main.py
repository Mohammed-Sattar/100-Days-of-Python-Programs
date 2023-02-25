# Day 2 - Python Primitive Data Types

# Python Primitive Data Types
# String
print("Hello"[3])
# Integer
# len(233)
print("123" + "456")
print(123 + 456)
# Float
pi = 3.1415
print(pi)
#Boolean
x = True

# Separating code - Type Error, Type Checking and Type Conversion:
num_char = len(input("What is your name? "))
print(type(num_char))
new_num = str(num_char)
print("Your name has " + new_num + " characters.")

x = 3.1414
print(type(x))

print(100 + float("70.5"))
print(str(70) + str(100))
print("----\n")

# Separating code - Mathematical Operations in Python:
# 4 + 2
# 4 - 2
# 4 * 2
# 4 / 2
# 4 // 2
# 4 ** 2

# Separating code - Number Manipulation and F Strings in Python
print(round(8/3, 2))
print(8//3)
height = 1.8
isWining = True
age = 12
print(f"You are {age} years old, your height is {height}, and you are winning is {isWining}")
