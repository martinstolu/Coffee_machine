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
    "money": 0.0,
}

rep_resources = {
    "water": 900,
    "milk": 600,
    "coffee": 300,
}


# TODO: 1. Prompt user by asking
#  “What would you like? (espresso/latte/cappuccino):

import time

def prompt(answer):

    # TODO: 2. Turn off the
    #  Coffee Machine by entering “off” to the prompt
    if answer == "off":
        print("🔌 Turning off the coffee machine. Bye!")
        exit()
    # TODO: 3. Print report.
    elif answer == "report":
        for lot in resources:
            if lot == "money":
                print(f"{lot}: ${resources[lot]:.2f}")
            else:
                print(f"{lot}: {resources[lot]}")
        return None
    elif answer == "replenish":
        for lot in rep_resources:
            resources[lot]+= rep_resources[lot]
        print("Resources replenished!")
        return None
    else:
        return answer

# TODO: 4. Check resources sufficient?
def check_resources(ingredients):
    for res in ingredients:
        if ingredients[res] > resources.get(res, 0):
            print(f"❌  Sorry there is not enough {res}.")
            return False
    return  True


# TODO: 5. Process coins.
def display_coin():
    print("💰 Please insert coin.")
    try:
        total = (int(input("How many quarters: ")) * 0.25
        + int(input("How many dimes: ")) * 0.10
                 + int(input("How many nickles: ")) * 0.05
                       + int(input("How many pennies: "))
                 * 0.01)
    except ValueError:
        print("⚠️ Invalid input! Please enter numbers only.")
        return 0.0
    return round(total, 2)

# TODO: 6. Check transaction successful?
def process_coin(drink_name, info):
        user_amount = display_coin()
        cost = info["cost"]
        if user_amount == cost:
            resources["money"] +=cost
            print(f"Preparing {drink_name}... Please wait")
            time.sleep(1)
            print(f"✅ Here is your {drink_name}!☕ Enjoy!")
            return True
        elif user_amount > cost:
            change = round(user_amount - cost, 2)
            resources["money"] += cost
            print(f"💸 Here is ${change:.2f} dollars "
                  f"in change.")
            print(f"Preparing {drink_name}... Please wait")
            time.sleep(2)
            print(f"✅ Here is your {drink_name}!☕ Enjoy!")
            return True
        else:
            print("❌ Sorry that's not enough money."
                  " Money refunded.")
            return False


def deduction(drink_name):
    for item in MENU[drink_name]["ingredients"]:
        resources[item] -= (
            MENU)[drink_name]["ingredients"][item]

# TODO: 7. Make Coffee.
def coffee():
    while True:
        user_input = input("What would you like? "
                           "(espresso/latte/cappuccino):"
                           " ").lower()
        drink = prompt(user_input)

        if drink is None:
            continue

        if drink in MENU:
            ingredients = MENU[drink]["ingredients"]

            if check_resources(ingredients):
                if process_coin(drink,MENU[drink]):
                    deduction(drink)
            else:
                print("❓ Invalid option. Please try again.")


            again = input("Do you want more coffee?"
                          " (y/n): ").lower()
            while again not in ["y", "n"]:
                print("❓ Invalid option. Please try again.")
                again = input("Do you want more coffee? "
                                 "Type 'y' for yes and 'n'"
                              " for no: ").lower()
            if again == "n":
                print("🔌 Turning off the coffee machine."
                      " Bye!")
                break


coffee()







