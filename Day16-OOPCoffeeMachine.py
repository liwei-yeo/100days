from Day16_2_menu import Menu
from Day16_1_coffee_maker import CoffeeMaker
from Day16_3_money_machine import MoneyMachine

# my_menu = Menu()
# print(my_menu.get_items())
    # latte/espresso/cappuccino/
# my_latte = my_menu.find_drink("latte")
    # "Sorry that item is not available."
#
# coffee_machine = CoffeeMaker()
# coffee_machine.report()
    # Water: {self.resources['water']}ml
# coffee_machine.is_resource_sufficient(my_latte)
    # "Sorry there is not enough {item}."
# coffee_machine.make_coffee(my_latte)
    # "Here is your {order.name} ☕️. Enjoy!"
#
# wallet = MoneyMachine()
# wallet.report()
    # "Money: {self.CURRENCY}{self.profit}"
    # "Please insert coins."
    # "How many {coin}?: "
# wallet.make_payment(1.5)
    # "Please insert coins."
    # "How many {coin}?: "

    # "Here is {self.CURRENCY}{change} in change."
    # "Sorry that's not enough money. Money refunded."

cm_menu = Menu()
cm = CoffeeMaker()
wallet = MoneyMachine()
powered = True
while powered:
    order = input(f"What would you like? ({cm_menu.get_items()}):").lower()
    if order == "off":
        powered = False
    elif order == "report":
        cm.report()
        wallet.report()
    else:
        if cm_menu.find_drink(order) is not None:
            if cm.is_resource_sufficient(cm_menu.find_drink(order)):
                if wallet.make_payment(cm_menu.find_drink(order).cost):
                    cm.make_coffee(cm_menu.find_drink(order))
