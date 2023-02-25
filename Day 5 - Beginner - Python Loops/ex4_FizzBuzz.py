# Day 5 - Exercise 4 - FizzBuzz:
for num in range (1, 101):
    if (num % 3 == 0) and (num % 5) == 0:
        print("FizzBuzz")
    elif (num % 3) == 0:
        print("Fizz", sep="")
    elif (num % 5) == 0:
        print("Buzz", sep="")
    else:
        print(num)
        