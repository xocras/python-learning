# Python Coffee Machine
COMMANDS = ["off", "report"]

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

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
    "water": [3000, "ml"],
    "milk": [2000, "ml"],
    "coffee": [1000, "g"],
    "money": [0, ""]
}


def display_resources():
    for resource, amount in resources.items():
        message = f"{resource[0].upper() + resource[1:]}: "
        message += f"{"$" if resource == "money" else ""}"

        amount, unit = amount

        amount = "{:,.2f}".format(amount)

        message += f"{amount + unit}"

        print(message)


def check_resources(coffee):
    ingredients = MENU[coffee]["ingredients"]

    for ingredient, amount in ingredients.items():
        if resources[ingredient][0] < amount:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True


def update_resources(coffee, setting):
    resource = MENU[coffee][setting]

    if setting == "cost":
        resources["money"][0] += resource
        return

    for item, amount in resource.items():
        resources[item][0] -= amount


def process_coins(coffee):
    total = 0
    cost = MENU[coffee]["cost"]

    print(f"Price: ${"{:,.2f}".format(cost)} dollars")

    for coin, value in COINS.items():
        total += int(input(f"Insert {coin}: ")) * value

    if total > cost:
        print(f"Here's ${"{:,.2f}".format(total)} dollars in change.")

    return total >= cost


def charge_customer(coffee):
    if process_coins(coffee):
        update_resources(coffee, "cost")
        return True

    print("Sorry, that's not enough money. Money refunded.")
    return False


def take_request():
    option = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    if option in MENU or option in COMMANDS:
        return option

    print("That's not a valid item. Please, try again.")
    return take_request()


def run_machine():
    option = take_request()

    if option == "off":
        print("Goodbye!")
        return

    if option == "report":
        display_resources()

    if option in MENU and check_resources(option) and charge_customer(option):
        update_resources(option, "ingredients")
        print(f"Here's your {option}! Enjoy!")

    run_machine()


# Start Coffee Machine
run_machine()
