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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Count coins
def count_coins():
    q_amount = quarters * 0.25
    d_amount = dimes * 0.10
    n_amount = nickels * 0.05
    p_amount = pennies * 0.01
    amount = round(q_amount + d_amount + n_amount + p_amount,2)
    return amount

# Make coffee
def make_coffee():
    resources['water']-= MENU[ask_coffee]["ingredients"]["water"]
    resources['milk']-= MENU[ask_coffee]["ingredients"]["milk"]
    resources['coffee']-= MENU[ask_coffee]["ingredients"]["coffee"]
    print(f"Here is your {ask_coffee}. Enjoy!")

money = 0.00
# Off
machine_off = False
is_sufficient = True
while not machine_off:
    # Ask coffee
    ask_coffee = input("What would you like? Espresso, Latte, Cappuccino: ").lower()

    if ask_coffee == "off":
        machine_off = True
    # Print report
    elif ask_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        ask_coffee = input("What would you like? Espresso, Latte, Cappuccino: ").lower()

    # Check sufficient
    for key in resources:
        if resources[key] < MENU[ask_coffee]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            is_sufficient = False
    if not is_sufficient:
        continue

    # Process coins
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    count = count_coins()
    print(count)

    # Check transaction
    change = round(count - MENU[ask_coffee]["cost"],2)
    if change >= 0:
        print(f"Here is ${change} dollars in change.")
        money += MENU[ask_coffee]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")

    make_coffee()

