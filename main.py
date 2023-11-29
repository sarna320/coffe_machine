from dictionaries import *


def check_resources(dec):
    for ingredient in MENU[dec]["ingredients"]:
        if resources[ingredient] < MENU[dec]["ingredients"][ingredient]:
            return False, ingredient
        else:
            continue
    return True, "None"


def calculate_monetary_val(dict_coins):
    sum_coins = 0
    for key in dict_coins:
        if key == "quarters":
            sum_coins += 0.25 * dict_coins[key]
        elif key == "dimes":
            sum_coins += 0.10 * dict_coins[key]
        elif key == "nickles":
            sum_coins += 0.05 * dict_coins[key]
        elif key == "pennies":
            sum_coins += 0.01 * dict_coins[key]
    return sum_coins


def payment(dec, client_money):
    if MENU[dec]["cost"] > client_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += MENU[dec]["cost"]
        change = round(client_money - MENU[dec]["cost"], 2)
        print(f"Here is ${change} dollars in change.")
        for key in MENU[dec]["ingredients"]:
            resources[key] -= MENU[dec]["ingredients"][key]
    return True


def main():
    while True:
        decision = input("“What would you like? (espresso/latte/cappuccino) off/report:")
        if decision == "off":
            break

        elif decision == "report":
            print(
                f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}"
            )
            continue
        elif decision == "espresso" or decision == "latte" or decision == "cappuccino":
            check, missing_ingredient = check_resources(decision)
            if check == False:
                print(f"Sorry there is not enough {missing_ingredient}.")
                continue
        else:
            print("Not correct command")
            continue

        for key in coins:
            coins[key] = int(input(f"How many {key}?: "))
        total_sum = calculate_monetary_val(coins)
        if payment(decision, total_sum):
            print(f"Here is your {decision}. Enjoy!")


if __name__ == "__main__":
    main()
