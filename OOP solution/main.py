from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#
# for i in Menu().menu:
#     print(i.ingredients)
#
# print(Menu().find_drink(ask).ingredients)
# print(chosen_drink["water"])
# print(CoffeeMaker().resources)
# for i in CoffeeMaker().resources:
#     print("this is {} chosen drink".format(chosen_drink[i]))
#     print("this is {} inventory".format(inventory[i]))

# flag = True
# inventory = CoffeeMaker().resources
# while flag:
#
#     ask = input("What would you like? (espresso/latte/cappuccino/): ")
#     chosen_drink = Menu().find_drink(ask).ingredients
#
#     def check_source():
#         for i in CoffeeMaker().resources:
#             if inventory[i] >= chosen_drink[i]:
#                 # print("enjoy your drink! ")
#                 inventory[i] = inventory[i] - chosen_drink[i]
#
#             elif inventory[i] < chosen_drink[i]:
#                 print("no enough {}".format(i))
#                 print("game over")
#
#
#
#     print(check_source())
#     print(inventory)
#


flag = True
while flag:

    ask = input("What would you like? (espresso/latte/cappuccino/): ")
    order = Menu().find_drink(ask)
    check = CoffeeMaker().is_resource_sufficient(order)
    # print(order.name)
    # print(order.cost)
    # print(order.ingredients)
    # print(order.ingredients)

    if check == True:
        CoffeeMaker().make_coffee(order)
        print(CoffeeMaker().resources)
        
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
SOLUTION
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)

