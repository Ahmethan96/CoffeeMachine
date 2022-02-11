from Drinks import MENU
from Drinks import resources

# TODO: 1. ask the user what he/she want to drink
drink = input("What would you like? (espresso/latte/cappuccino): ")


dic = {}
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def ask_user(drink):
    if drink == "report":
        return drink
    return drink



def up_date():
    dic[ask_user(drink)] = calculation()
    print(dic)
    cof = dic["latte"]
    if ask_user(drink) == "latte":
        if cof["water"] >= 200:
            print("nice")
        elif cof["water"] < 200:
            print("no water")

def calculation():
    menu = MENU[ask_user(drink)]
    cost = menu["cost"]
    ingredients = menu["ingredients"]
    amount = resources
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    if ask_user(drink) == "latte":
        water = resources["water"] - ingredients["water"]
        milk = resources["milk"] - ingredients["milk"]
        coffee = resources["coffee"] - ingredients["coffee"]

        print(f"the rest amount of water is {water}")
        print(f"the rest amount of milk is {milk}")
        print(f"the rest amount of coffee is {coffee}")
        print(f"the ingredients is {ingredients} and the cost is {cost}")

        return {'water': water, 'milk': milk, 'coffee': coffee}

    elif ask_user(drink) == "cappuccino":
        water = resources["water"] - ingredients["water"]
        milk = resources["milk"] - ingredients["milk"]
        coffee = resources["coffee"] - ingredients["coffee"]

        print(f"the rest amount of water is {water}")
        print(f"the rest amount of milk is {milk}")
        print(f"the rest amount of coffee is {coffee}")
        print(f"the ingredients is {ingredients} and the cost is {cost}")

        return {'water': water, 'milk': milk, 'coffee': coffee}

    elif ask_user(drink) == "espresso":
            # menu = MENU[ask_user(drink)]
            # cost = menu["cost"]
            # ingredients = menu["ingredients"]
            # amount = resources
            # water = resources["water"] - ingredients["water"]
            # coffee = resources["coffee"] - ingredients["coffee"]
        water = resources["water"] - ingredients["water"]
        coffee = resources["coffee"] - ingredients["coffee"]

        print(f"the rest amount of water is {water}")
        print(f"the rest amount of coffee is {coffee}")
            # up_date()
        return {'water': water, 'coffee': coffee}

    elif ask_user(drink) == "report":
        print(resources)

ask_user(drink)
# calculation()
up_date()

