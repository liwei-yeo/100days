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


def coffee(stored_resources, stored_wallet):
    order_cleared = False
    payment_cleared = False

    ##### ORDER
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    request_list = {}
    if request == "report":
        print(f'Water: {stored_resources["water"]}ml\n'
              f'Milk: {stored_resources["milk"]}ml\n'
              f'Coffee: {stored_resources["coffee"]}g\n'
              f'Money: ${stored_wallet}')
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        # load order
        request_list = MENU[request]

        # check 'stored_resources' sufficient
        insufficient_item = ""
        for ingre in request_list["ingredients"]:
            if request_list["ingredients"][ingre] > stored_resources[ingre]:
                # if loop return item if fail
                insufficient_item = ingre
        if insufficient_item == "":
            order_cleared = True
        else:
            print(f"Sorry there is not enough {insufficient_item}.")
    else:
        print("Order not recognised, please try again.")


    #### PAYMENT
    collected = 0
    if order_cleared:
        print(f'Please insert ${request_list["cost"]}.')
        quar_amt = float(input("How many quarters?: ")) * 0.25
        dime_amt = float(input("How many dimes?: ")) * 0.1
        nick_amt = float(input("How many nickles?: ")) * 0.05
        penn_amt = float(input("How many pennies?: ")) * 0.01
        collected = round(quar_amt + dime_amt + nick_amt + penn_amt, 2)
        if collected < request_list["cost"]:
            # if loop fail
            print(f"Sorry that's not enough money. {collected} refunded.")
        else:
            # if loop pass 'payment_cleared' True
            payment_cleared = True

    #### FUFILLMENT
    if payment_cleared:
        # add payment to new_wallet
        new_wallet = stored_wallet + request_list["cost"]
        change = collected - request_list["cost"]
        # deduct resources to new_resource
        for amt in request_list["ingredients"]:
            stored_resources[amt] -= request_list["ingredients"][amt]
        new_resource = stored_resources
        # return change and send order
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {request} ☕. Enjoy!")
    else:
        new_resource = stored_resources
        new_wallet = stored_wallet

    return [new_resource,new_wallet]


wallet = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_storage = [resources,wallet]
powered = True
while powered:
    machine_storage = coffee(machine_storage[0], machine_storage[1])