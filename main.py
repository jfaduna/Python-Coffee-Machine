from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
still_active = True

while still_active:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == 'off':
        still_active = False
    elif option == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(option)
        if coffee:
            if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
