import menu


def coffee_machine():

    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower().strip()
    if user_choice == "off":
        print("Turning the machine off, thank you for the preference... ")
        quit()
    elif user_choice == 'report':
        for element in menu.resources:
            print(f"{element.title()}: {menu.resources[element]}")

        print(f"Money: ${menu.profit}")
        coffee_machine()
    elif user_choice == 'latte':
        resource_check(menu.MENU['latte']['ingredients'],  menu.resources, user_choice)
    elif user_choice == 'espresso':
        resource_check(menu.MENU['espresso']['ingredients'],  menu.resources, user_choice)
    elif user_choice == 'cappuccino':
        resource_check(menu.MENU['cappuccino']['ingredients'],  menu.resources, user_choice)
    else:
        print("Please insert valid input.")
        coffee_machine()

    print("Please insert coins.")
    coins_quarter = int(input("How many quarters? "))
    coins_dimes = int(input("How many dimes? "))
    coins_nickles = int(input("How many nickles? "))
    coins_pennies = int(input("How many pennies? "))

    money_change = price_check(coins_quarter, coins_dimes, coins_nickles, coins_pennies, user_choice)
    if money_change != 0:
        print("Here is ${:.2f} in change.".format(money_change))

    print(f"Here is your {user_choice}, enjoy! ")

    if user_choice == 'latte':
        menu.resources['water'] -= menu.MENU['latte']['ingredients']['water']
        menu.resources['milk'] -= menu.MENU['latte']['ingredients']['milk']
        menu.resources['coffee'] -= menu.MENU['latte']['ingredients']['coffee']

    elif user_choice == 'espresso':
        menu.resources['water'] -= menu.MENU['espresso']['ingredients']['water']
        menu.resources['milk'] -= menu.MENU['espresso']['ingredients']['milk']
        menu.resources['coffee'] -= menu.MENU['espresso']['ingredients']['coffee']

    elif user_choice == 'cappuccino':
        menu.resources['water'] -= menu.MENU['cappuccino']['ingredients']['water']
        menu.resources['milk'] -= menu.MENU['cappuccino']['ingredients']['milk']
        menu.resources['coffee'] -= menu.MENU['cappuccino']['ingredients']['coffee']


    menu.profit += menu.MENU[user_choice]['cost']
    coffee_machine()


def resource_check(data_drink, resources, user_choice):
    if data_drink['water'] > resources['water']:
        print("Sorry there is not enough water.")
        coffee_machine()
    elif data_drink['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee.")
        coffee_machine()
    if user_choice != 'espresso':
        if data_drink['milk'] > resources['milk']:
            print("Sorry there is not enough milk.")
            coffee_machine()


def price_check(coins_quarter, coins_dimes, coins_nickles, coins_pennies, user_choice):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total_money = (coins_quarter * 0.25) + (coins_dimes * 0.10) + (coins_nickles * 0.05) + (coins_pennies * 0.01)
    if total_money < menu.MENU[user_choice]['cost']:
        print("You don't have enough money, returning the value...")
        coffee_machine()
    return total_money - menu.MENU[user_choice]['cost']


coffee_machine()