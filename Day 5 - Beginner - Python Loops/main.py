# Video code - Using the for loop with Python Lists:
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)       # Lack of indentation means outside the loop

# useful functions in python that replace some of the functions of loops: sum(), max(), min(), len()

# Seaprating code - for loops and the range() function:
sum = 0
for number in range(1, 101):
    sum += number
print(sum)

# Exercise 1 - Average Height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = sum = 0
for single_student in student_heights:
    sum += single_student
    count += 1

print(f"{round(sum/count)}")

# Exercise 2 - High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = student_scores[0]
for score in student_scores: 
    if(score > max):
        max = score
print(f"The highest score in the class is: {max}")

# Exercise 3 - Adding Even Numbers:
sum = 0
for z in range(2, 101, 2):
    sum += z
print(sum)

# Exercise 4 - FizzBuzz:
for num in range (1, 101):
    if (num % 3 == 0) and (num % 5) == 0:
        print("FizzBuzz")
    elif (num % 3) == 0:
        print("Fizz", sep="")
    elif (num % 5) == 0:
        print("Buzz", sep="")
    else:
        print(num)
    

# Day 5 Project - Create a Password Generator:
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

# letter_in_pass = ""
for l in range(nr_letters):
    # my solution
    # random_letter = letters[random.randint(0, len(letters)-1)]     
    # random_letter = random.choice(letters)      
    # letter_in_pass += random_letter

    password +=random.choice(letters)       #better solution
# print(letter_in_pass)

# symbol_in_pass = ""
for l in range(nr_symbols):
    # my solution
    # random_symbol = symbols[random.randint(0, len(symbols)-1)]      
    # symbol_in_pass += random_symbol

    password +=random.choice(symbols) # better solution
# print(symbol_in_pass)

# numbr_in_pass = ""
for l in range(nr_numbers):
    # my solution
    # random_numbr = numbers[random.randint(0, len(numbers)-1)]   
    # numbr_in_pass += random_numbr          

    password +=random.choice(numbers) # better solution

# print(numbr_in_pass)

# password = letter_in_pass + symbol_in_pass + numbr_in_pass
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

rand_pass = random.sample(password, k=len(password))

# random.shuffle(list_pass)
print(''.join(rand_pass))
