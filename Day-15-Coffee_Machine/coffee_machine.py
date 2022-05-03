import coffee_ingredients as menu


def coffee_menu():
    """Prints coffee options for users to select"""
    print("What would you like to drink?")
    for letter in menu.MENU:
        coffee_letter = menu.MENU[letter]
        menu_options = coffee_letter['display']
        print(menu_options)


def option_selection():
    """Processes user selection: either returning a key word or a MENU dictionary"""
    user_selection = input().lower()
    if user_selection == 'off':
        return 'off'
    elif user_selection == 'report':
        return 'report'
    elif user_selection == 'profit':
        return 'profit'
    else:
        coffee_letter = menu.MENU[user_selection]
        print(f"You selected:\n{coffee_letter['display']}")
        return coffee_letter


def ingredients_report():
    """Prints a report containing the amount of resources in the coffee machine"""
    resources = menu.resources
    print(f"\nThe coffee machine has:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\n")


def resources_sufficient(coffee_ingredients):
    """Check if there are sufficient resources to make the drink selected by the user"""
    resources = menu.resources
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"\nSorry, there is not enough {item}.\n")
            return False
    return True


def process_coins():
    """Adds up the total number of coins entered and displays the amount entered"""
    print("\nPlease insert coins")
    cents_quarters = int(input("How many quarters? "))
    cents_dimes = int(input("How many dimes? "))
    cents_nickles = int(input("How many nickles? "))
    cents_pennies = int(input("How many pennies? "))

    total_paid = (cents_quarters*25 + cents_dimes*10 + cents_nickles*5 + cents_pennies*1)/100
    print(f"\nYou inserted: ${total_paid:.2f}")

    return total_paid


def validate_transaction(money_received, drink):
    """Checks to see if payment is sufficient"""
    cost = drink['cost']

    if money_received >= cost:
        change = money_received - cost
        print(f"You're change is ${change:.2f}")
        return True
    elif money_received < cost:
        owed = cost - money_received
        print(f"You still need: ${owed:.2f}.")

        print("\nWould you like to insert more coins?")
        more_coins = input("Type 'Y' for Yes. Type 'N' for No. ").lower()
        if more_coins == 'y':
            added_payment = process_coins()
            new_total = money_received + added_payment
            if validate_transaction(new_total, drink):
                return True
        if more_coins == 'n':
            print("\nThank you. Your money has been refunded.\n")
            return False


def make_coffee(drink_name, drink_ingredients):
    """Reduces the amount resources needed to make the selected drink from the coffee machine"""
    resources = menu.resources
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]

    print(f"\nHere is your {drink_name}. Please Enjoy!")
    print("CAUTION: DRINK IS HOT!\n")


def profit(money_made, drink_cost):
    """Returns the profits made from each complete transaction"""
    money_made += drink_cost
    return money_made


earnings = 0
coffee_machine_is_on = True
while coffee_machine_is_on:
    coffee_menu()
    choice = option_selection()
    if choice == 'off':
        coffee_machine_is_on = False
    elif choice == 'report':
        ingredients_report()
    elif choice == 'profit':
        print(f"\nThis machine has earned: ${earnings:.2f}\n")
    else:
        if resources_sufficient(choice['ingredients']):
            payment = process_coins()
            if validate_transaction(payment, choice):
                make_coffee(choice['drink'], choice['ingredients'])
                earnings = profit(earnings, choice['cost'])
