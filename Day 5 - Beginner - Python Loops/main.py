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

    