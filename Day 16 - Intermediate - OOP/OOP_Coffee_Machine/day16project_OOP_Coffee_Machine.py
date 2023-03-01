from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

customer_drink = Menu()
report = CoffeeMaker()
money = MoneyMachine()

user_choice = ""
while user_choice != "off":
    user_choice = input(f"What would you like? ({customer_drink.get_items()}): ").lower()
    
    if user_choice == "report":
        report.report()
        money.report()

    else:
        drink = customer_drink.find_drink(user_choice)
        if drink != None:
            is_sufficient = report.is_resource_sufficient(drink)
            if is_sufficient:
                transaction_success = money.make_payment(drink.cost)
                if transaction_success:
                    report.make_coffee(drink)
