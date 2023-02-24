# Day 10 - Functions with outputs:
# Video code - Functions with Outputs:

def format_name(f_name, m_name, l_name):
    """Takes the first middle and last names and capitlizes the first letter if each"""
    if f_name == "" or m_name == "" or l_name == "":
        return "You didn't enter your name"     # function with multiple with multiple returns

    formatted_f_name = f_name.title()
    formatted_m_name = m_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_m_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your middle name? "), input("What is your last name? ")))


# Exercise 1 - Expanding leap year program from day 3 Exercise 3 - Leap Year:
def is_leap(year):
    """Returns True if its a leap year, otherwise returns False"""
    is_leap = True
    if (year % 4 == 0):
        if year % 100 == 0:

            if year % 400 != 0:
                is_leap = False
    else:
        is_leap = False
    
    return is_leap

def days_in_month(year, month):
    """Calculates how many days in requested month. It also takes leap years into account."""
    if is_leap(year) and month == 2:
        return 29

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    return (month_days[month-1])
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



# Day 10 Project - Calculator:
import art
import os
clear = lambda: os.system('cls') #on Windows System     # copied from Stack Overflow

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    # By putting this code into the calculator() function it enables the recursion functionality
    print(art.logo)
    another_operation = "y"
    operators = {"+": add, "-": subtract, "*": multiply, "/": divide}

    num1 = float(input("What's the first number? "))

    for symbol in operators:
        print(symbol)


    while another_operation.lower() == "y":
        operation_choice = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operators[operation_choice](num1, num2)     # functions can be stored as values in a dictionary, 
                # so ^^ line of code accesses the function stored as a value and passes the arguments to it (num1, num2)

        print(f"{num1} {operation_choice} {num2} = {operators[operation_choice](num1, num2)}")
        another_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if another_operation == "y":
            num1 = answer
        elif another_operation == "n":
            clear()
            calculator()    # this is recursion, where a function is called inside itself, it creates a loop

calculator()


















# print(f"{num1} {operation_choice} {num2} = {operators[operation_choice](num1, num2)}")

# second_operation = input("Pick another operation: ")
# num3 = int(input("What's the second number: "))
# second_answer = operators[second_operation](answer, num3)

# print(f"{answer} {second_operation} {num3} = {second_answer}")