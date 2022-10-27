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
    "conflates": {
        "ingredients": {
            "water": 50,
            "sugar": 10,
            "milk": 30,
        },
        "cost": 4.5,
    },
}



resources = {
    "water": 150,
    "milk": 88,
    "milo": 50,
    "sugar": 30,
    "coffee": 20,
    "chocolate": 20
}

profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (tea, conflates, pap: )")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Mill: {resources['milo']}ml")
        print(f"Sugar: {resources['sugar']}ml")
        print(f"Money: N {profit}")