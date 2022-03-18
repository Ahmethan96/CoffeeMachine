from Drinks import MENU
from Drinks import resources

res = resources

latte = MENU["latte"]
in_latte = latte["ingredients"]

espresso = MENU["espresso"]
in_espresso = espresso["ingredients"]

cappuccino = MENU["cappuccino"]
in_cappuccino = cappuccino["ingredients"]

print(res)

flag = True
while flag:
    def espresso():
        if res["water"] >= in_espresso["water"] and res["coffee"] >= in_espresso["coffee"]:
            print("please insert coins")
            quartar = int(input("how many quartars? "))
            calc = quartar * 0.25
            if calc >= 2.5:
                change = calc - 2.5
                print(f"here is {change} in change")
                water = res["water"] - in_espresso["water"]
                coffee = res["coffee"] - in_espresso["coffee"]
                res["water"] = water
                res["coffee"] = coffee
                print(res)

            elif calc < 2.5:
                print("sorry that's is not enough money")

        elif res["water"] < in_espresso["water"]:
            print("there is no enough water")
        elif res["coffee"] < in_espresso["coffee"]:
            print("there is no enough coffee")
        elif res["milk"] < in_espresso["milk"]:
            print("there is no enough milk")
            # return flag == False

    def latte():
        if res["water"] >= in_latte["water"] and res["coffee"] >= in_latte["coffee"] and res["milk"] >= in_latte["milk"]:
            print("please insert coins")
            quartar = int(input("how many quartars? "))
            calc = quartar * 0.25
            if calc >= 2.5:
                change = calc - 2.5
                print(f"here is {change} in change")
                water = res["water"] - in_latte["water"]
                coffee = res["coffee"] - in_latte["coffee"]
                milk = res["milk"] - in_latte["milk"]
                res["water"] = water
                res["coffee"] = coffee
                res["milk"] = milk
                print(res)

            elif calc < 2.5:
                print("sorry that's is not enough money")

        elif res["water"] < in_latte["water"]:
            print("there is no enough water")
        elif res["coffee"] < in_latte["coffee"]:
            print("there is no enough coffee")
        elif res["milk"] < in_latte["milk"]:
            print("there is no enough milk")
            # return flag == False

    def cappuccino():
        if res["water"] >= in_cappuccino["water"] and res["coffee"] >= in_cappuccino["coffee"] and res["milk"] >= in_cappuccino["milk"]:
                print("please insert coins")
                quartar = int(input("how many quartars? "))
                calc = quartar * 0.25
                if calc >= 2.5:
                    change = calc - 2.5
                    print(f"here is {change} in change")
                    water = res["water"] - in_cappuccino["water"]
                    coffee = res["coffee"] - in_cappuccino["coffee"]
                    milk = res["milk"] - in_cappuccino["milk"]
                    res["water"] = water
                    res["coffee"] = coffee
                    res["milk"] = milk
                    print(res)

                elif calc < 2.5:
                    print("sorry that's is not enough money")

        elif res["water"] < in_cappuccino["water"]:
            print("there is no enough water")
        elif res["coffee"] < in_cappuccino["coffee"]:
            print("there is no enough coffee")
        elif res["milk"] < in_cappuccino["milk"]:
            print("there is no enough milk")
            # return flag == False

    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask == "espresso":
        espresso()
    elif ask == "latte":
        latte()
    elif ask == "cappuccino":
        cappuccino()
    elif ask == "off":
        flag = False
    elif ask == "report":
        print(res)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# updated coffee machine 
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


from Drinks import MENU
from Drinks import resources

dic = {}
espresso = MENU["espresso"]
latte = MENU["latte"]
cappuccino = MENU["cappuccino"]
##############################
espresso_in = espresso["ingredients"]
latte_in = latte["ingredients"]
cappuccino_in = cappuccino["ingredients"]
########################################
print(espresso_in["water"])
print(resources["water"])
flag = False
while ask_user() != flag:
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    def ask_user():
        if ask == "espresso":
            money = int(input("insert coins: "))
            total = money * 0.25
            if total >= 2.5:
                change = total - 2.5
                print(f"here is you change {change}")
                if resources["water"] >= espresso_in["water"] and resources["coffee"] > espresso_in["coffee"] :
                    resources["water"] = resources["water"] -espresso_in["water"]
                    resources["coffee"] = resources["coffee"] - espresso_in["coffee"]
                    print(f"the rest amount of water is {resources['water']}")
                    print(f"the rest amount of coffee is {resources['coffee']}")
                else:
                    print("you do not have enough ingredients")
            else:
                print("Sorry that is not enough money ")

        elif ask == "latte":
            money = int(input("insert coins: "))
            total = money * 0.25
            if total >= 2.5:
                change = total - 2.5
                print(f"here is you change {change}")
                if resources["water"] >= latte_in["water"] and resources["coffee"] > latte_in["coffee"] and resources["milk"] >= latte_in["milk"] :
                    resources["water"] = resources["water"] - latte_in["water"]
                    resources["coffee"] = resources["coffee"] - latte_in["coffee"]
                    resources["milk"] = resources["milk"] - latte_in["milk"]
                    print(f"the rest amount of water is {resources['water']}")
                    print(f"the rest amount of coffee is {resources['coffee']}")
                    print(f"the rest amount of milk is {resources['milk']}")
                else:
                    print("you do not have enough ingredients")
            else:
                print("Sorry that is not enough money ")
        elif ask == "cappuccino":
            money = int(input("insert coins: "))
            total = money * 0.25
            if total >= 2.5:
                change = total - 2.5
                print(f"here is you change {change}")
                if  resources["water"] >= cappuccino_in["water"] and resources["coffee"] > cappuccino_in["coffee"] and resources["milk"] >= cappuccino_in["milk"] :
                    resources["water"] = resources["water"] - cappuccino_in["water"]
                    resources["coffee"] = resources["coffee"] - cappuccino_in["coffee"]
                    resources["milk"] = resources["milk"] - cappuccino_in["milk"]
                    print(f"the rest amount of water is {resources['water']}")
                    print(f"the rest amount of coffee is {resources['coffee']}")
                    print(f"the rest amount of milk is {resources['milk']}")
                else:
                    print("you do not have enough ingredients")
            else:
                print("Sorry that is not enough money ")
        elif ask == "report":
            print(resources)

        elif ask == "quit":
            flag == True
            return flag

print(ask_user())

