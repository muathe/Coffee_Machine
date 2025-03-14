MENU = {
    "espresso": {
        "ingredients": {
            "water": 100,
            "coffee": 36,

        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 400,
            "milk": 300,
            "coffee": 48
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 500,
            "milk": 200,
            "coffee": 48
        },
        "cost": 3.0
    }


}

profit = 0


def available_resources(ingredients):
    """Checks if resources has enough ingredients to make coffee."""
    for item in ingredients:
        if resources[item] < ingredients[item]:
            return False
    return True


def collect_coins():
    """Calculates the total coins inserted."""
    print("Please insert coins:")
    total = int(input("Please enter quarters inserted: ")) * 0.25
    total += int(input("Please enter dimes inserted: ")) * 0.10
    total += int(input("Please enter nickels inserted: ")) * 0.05
    total += int(input("Please enter cents inserted: ")) * 0.01
    return total


def sufficient_payment(payment, cost):
    """Calculates if the customer has  a sufficient amount of coins to buy coffee."""
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f" Your change is ${change}")
        global profit
        profit += cost
        return True

    else:
        print("Sorry you have insufficient coins, GoodBye!")
        return False


def coffee(choice, order_ingredients):
    """Prints coffee order and makes sure to update the resources left i.e. ingredients."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"We hope you enjoy your {choice} CHEERS!")


resources = {
    "water": 2000,
    "milk": 1000,
    "coffee": 800
}

on = True

while on:
    choice = input("Please choose which drink you would like (espresso/latte/cappuccino) ").lower()
    if choice == "off":
        on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if available_resources(drink["ingredients"]):
            payment = collect_coins()
            if sufficient_payment(payment, drink["cost"]):
                coffee(choice, drink["ingredients"])




#cell 47 cents



