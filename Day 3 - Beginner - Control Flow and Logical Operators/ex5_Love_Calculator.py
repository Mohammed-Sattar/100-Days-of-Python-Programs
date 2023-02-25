# Day 3 - Exercise 5 - Love Calculator:
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.upper()
name2 = name2.upper()

true_count = 0
lo_count = 0

# My solution:
# true_count += name1.count("T")
# true_count += name2.count("T")
# true_count += name1.count("R")
# true_count += name2.count("R")
# true_count += name1.count("U")
# true_count += name2.count("U")
# true_count += name1.count("E")
# true_count += name2.count("E")

# lo_count += name1.count("L")
# lo_count += name2.count("L")
# lo_count += name1.count("O")
# lo_count += name2.count("O")
# lo_count += name1.count("V")
# lo_count += name2.count("V")
# lo_count += name1.count("E")
# lo_count += name2.count("E")

# Better solution more efficient:
combine_string = name1 + name2
true_count += combine_string.count("T")
true_count += combine_string.count("R")
true_count += combine_string.count("U")
true_count += combine_string.count("E")

lo_count += combine_string.count("L")
lo_count += combine_string.count("O")
lo_count += combine_string.count("V")
lo_count += combine_string.count("E")
# End of difference between solutions
score =int(str(true_count) + str(lo_count))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")