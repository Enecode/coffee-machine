MENU = {
    "tea": {
        "ingredients": {
            "water": 50,
            "milk": 18,
            "chocolate": 20,
            "sugar": 10,
        },
        "cost": 4.5,
    },

    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 20,
        },
        "cost": 5.5
    },
    "conflakes": {
        "ingredients": {
            "water": 50,
            "sugar": 10,
            "milk": 30,
        },
        "cost": 4.5,
    },
}

profit = 0
resources = {
    "water": 150,
    "milk": 88,
    "milo": 50,
    "sugar": 30,
    "coffee": 20,
    "chocolate": 20
}


def is_resources_sufficient(order_ingredients):
    """ Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calaculated from coins entered"""
    print("Enter amount in coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dines?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(amount_recieved, drink_cost):
    """Return True when the payment is accepted, or False if many is insufficient."""
    if amount_recieved >= drink_cost:
        change = round(amount_recieved - drink_cost, 2)
        print(f"here is ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}") 


is_on = True
while is_on:
    choice = input("What would you like? (tea, conflakes, espresso: )")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Mill: {resources['milo']}ml")
        print(f"Sugar: {resources['sugar']}ml")
        print(f"Money: N {profit}")

    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
