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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_report():
    """Displays the current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(coffee):
    """Returns True when order can be made, False if ingredients are insufficient."""
    coffee_ingredients = MENU[coffee]['ingredients']
    for ingredient in coffee_ingredients:
        if resources[ingredient] < coffee_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_payment():
    """Returns the total amount calculated from coins inserted."""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def process_coffee(coffee):
    """Deduct the required ingredients from the resource."""
    coffee_ingredients = MENU[coffee]['ingredients']
    for ingredient in coffee_ingredients:
        resources[ingredient] -= coffee_ingredients[ingredient]
    print(f"Here is your {coffee} ☕ Enjoy!")


def make_coffee(coffee, total_profit) -> float:
    if coffee in MENU:
        has_enough_resource = check_resources(option)
        if has_enough_resource:
            coffee_price = MENU[coffee]['cost']
            total_payment = process_payment(option)
            if total_payment > coffee_price:
                print(f"Here is ${total_payment - coffee_price:.2f} in change.")
                process_coffee(coffee)
                total_profit += coffee_price
                return total_profit
            else:
                print("Sorry that's not enough money. Money refunded.")
                return 0
    else:
        print("Invalid option. Please only select from the list of available options.")
        return 0


still_active = True
while still_active:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == 'report':
        show_report()
    elif option == 'off':
        still_active = False
    else:
        profit += make_coffee(option, profit)
