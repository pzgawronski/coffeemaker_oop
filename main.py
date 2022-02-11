from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def full_report(user_input):
    if user_input.upper() == "REPORT":
        return coffee_maker.report(), money_machine.report()


def kill_switch(user_input):
    if user_input.upper() == "OFF":
        print("I hope you have a great day!")
        exit()


def check_input(user_input):
    full_report(user_input)
    kill_switch(user_input)


def get_coffee(name, options):
    coffee_obj = ""
    for menu_item in options:
        if menu_item.name == name:
            coffee_obj = menu_item
    return coffee_obj


def keep_running():
    valid_input = False
    options = ("Y", "N")
    while not valid_input:
        decision = input("Make another coffee? Y/N ")
        check_input(decision)
        if decision in options:
            valid_input = True
        return False if decision.upper() == "N" else True


brewing = True
while brewing:
    print("Good day to you!")
    coffee_menu = menu.get_items()
    coffee_select = input(f"What kind of coffee would you like? {coffee_menu}")
    check_input(coffee_select)

    if not menu.find_drink(coffee_select):
        break

    coffee = get_coffee(coffee_select, menu.menu)

    if not money_machine.make_payment(coffee.cost):
        break

    if not coffee_maker.is_resource_sufficient(coffee):
        break

    coffee_maker.make_coffee(coffee)
    brewing = keep_running()
