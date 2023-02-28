MENU = {
    "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
        "cost": 1.5,
    },
    "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
        "cost": 2.5,
    },
    "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculate_resources (resources, user_input=""):

    is_enough = True

    for ingredient in MENU[user_input]['ingredients']:
        ingredients_enough = sufficient_resources(user_input, resources, ingredient)

        if (ingredients_enough):
            resources[ingredient] -= MENU[user_input]['ingredients'][ingredient]

        else:
            is_enough = False
            break

    return is_enough    

def sufficient_resources (user_input, resources, ingredient ):
    if resources[ingredient] >= MENU[user_input]['ingredients'][ingredient]:
        return True
    else:
        print(f"Sorry there is not enough {ingredient}")
        return False

def accept_money (money, user_input, enough_ingredients):
    """Accepts the payment from the customer, processes it, and sends an output to the user accordingly.
    It also returns he amount of money made from the transaction back to the program."""
    if (enough_ingredients):
        print("Please insert coins")
        coins = {"quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}

        money = 0
        cost = MENU[user_input]['cost'] * 100 # gets the price of the coffe option user chose and converts it from $ to pence
        change = 0
        for pay in coins:
            payment = int(input(f"how many {pay}? "))
            money += payment * coins[pay]

        change = (money - cost)/100     # calculating the amount of change for the user

        if money < cost:
            print("Sorry that's not enough money. Money Refunded")
            return False
        elif money > cost:
            print(f"Here is ${change} in change")
        # print(money)

        return round((money/100) - change, 2)       # this returns the amount of money made from the transaction in dollars

money = 0
user_input = ""
while (user_input != "off"):
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
  
    if user_input == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${money}")
        
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        x = calculate_resources(resources, user_input)
        y = accept_money(money, user_input, enough_ingredients= x)

        if (not y or not x):
            continue
        money += y
        # if (x == False):
        #     continue

        print(f"Here is your {user_input} ☕. Enjoy!")

