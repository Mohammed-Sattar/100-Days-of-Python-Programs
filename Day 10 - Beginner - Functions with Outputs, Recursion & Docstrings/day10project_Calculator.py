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
