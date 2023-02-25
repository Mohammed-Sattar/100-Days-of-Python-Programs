# Day 8 - Exercise 2 - Prime Numbers:
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