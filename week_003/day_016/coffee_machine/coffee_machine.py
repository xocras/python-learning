from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

options = list(map(lambda i: i.name, menu.menu))

while True:
    option = input(f"What would you like? ({menu.get_items()[0:-1]})\n").lower()

    if option == "off":
        print("Goodbye!")
        break

    if option == "report":
        coffee_maker.report()
        continue

    if option not in options:
        print("That's not a valid item. Please, try again.")
        continue

    drink = menu.find_drink(option)

    if not coffee_maker.is_resource_sufficient(drink):
        continue

    print(f"Price: ${"{:,.2f}".format(drink.cost)} dollars")

    if not money_machine.make_payment(drink.cost):
        continue

    coffee_maker.make_coffee(drink)

