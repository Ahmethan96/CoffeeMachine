from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ask_user = input("What would you like? (espresso/latte/cappuccino/): ")

# print(Menu().menu[0].ingredients["water"])
# print(Menu().find_drink(ask_user).ingredients)
# print(Menu().menu[Menu().find_drink(ask_user)])
# for i in CoffeeMaker().resources:
#     print(i, CoffeeMaker().resources[i])


# print(CoffeeMaker().resources["water"])
#
# for i in CoffeeMaker().resources:
#     print(i)
#
# print(f" this is {Menu().find_drink(ask_user).ingredients}")

def subtract():
    for i in CoffeeMaker().resources:
        print(CoffeeMaker().resources[i])
        CoffeeMaker().resources[i] = CoffeeMaker().resources[i] - Menu().find_drink(ask_user).ingredients[i]

    return CoffeeMaker().resources


def check_resource():
    for j in Menu().menu:
        print(j.name)
        if j.name == ask_user:
            for i in CoffeeMaker().resources:
                if CoffeeMaker().resources[i] > Menu().find_drink(ask_user).ingredients[i]:
                    print("you have enough amount of {} {}".format(i, Menu().find_drink(ask_user).ingredients[i]))
                    print(subtract())
                elif CoffeeMaker().resources[i] < Menu().find_drink(ask_user).ingredients[i]:
                    print(
                        "you DO NOT have enough amount of {} {}".format(i, Menu().find_drink(ask_user).ingredients[i]))


for i in range(len(Menu().menu)):
    if Menu().menu[i].name == ask_user:
        check_resource()


# drink = MenuItem(ask_user, 200, 51, 24, 1.5)
# print(drink.name)
# print(drink.ingredients)
# print(drink.cost)

# print(Menu().menu[0].name)
# print(Menu().menu[0].ingredients)
#
# for j in range(len(Menu().menu)):
#     print(Menu().menu[j].name)
#     if Menu().menu[j].name == ask_user:
#         print("good job, you choose {}".format(ask_user))
#
#
# for i in Menu().menu[0].ingredients:
#     print(i)
#
# print(Menu().get_items())
# print(Menu().find_drink(ask_user).name)
# print(Menu().menu[1].name)
# print(Menu().find_drink(ask_user).name)

# for x in Menu().menu:
#     print(x.name)
