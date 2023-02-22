import math
# Video code - Functions with Inputs:
def greet():
    print("Hello")
    print("Welcome to the program")
    print("Hope you are well")

greet()

def greet_name(name):
    print(f"Hello {name}")
    print(f"Welcome to the program {name}")

greet_name("Mohammed")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}?")

greet_with("Mohammed", "Saudi Arabia")      # using positional arguments
greet_with(name="Yusuf", location="Nowhere")        # using keyword arguments




# Exercise 1 - Paint Area Calculator:
def paint_calc(height, width, cover):
    cans_needed = (height * width)/coverage
    print(f"You'll need {math.ceil(cans_needed)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise 2 - Prime Numbers:
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            # print(f"{number} % {i} = {number % i}")
            is_prime = False
            print(f"It's not a prime number.")
            break

    if is_prime == True:
        print(f"It's a prime number.")
        

n = int(input("Check this number: "))
prime_checker(number=n)

# Day 8 Project - Caesar Cipher:
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar (text, shift, direction):
    new_text = ""
    shift %= 26         # to handle very large shifts

    if direction == "decode":
        shift *= -1

    for l in text:  
        if l not in alphabet:
            new_text += l
            continue

        new_index = alphabet.index(l) + shift       # getting each letter from text and adding the shift amount to it
        new_text += alphabet[new_index]
    print(f"The {direction}d text is {new_text}")

repeat = "yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
