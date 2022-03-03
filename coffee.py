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
            water = res["water"] - in_espresso["water"]
            coffee = res["coffee"] - in_espresso["coffee"]
            res["water"] = water
            res["coffee"] = coffee
            print(res)
            # print(f"the rest amount of water is {water}")
            # print(f"the rest amount of coffee is {coffee}")
        elif res["water"] < in_espresso["water"]:
            print("there is no enough water")
        elif res["coffee"] < in_espresso["coffee"]:
            print("there is no enough coffee")
        elif res["milk"] < in_espresso["milk"]:
            print("there is no enough milk")
            # return flag == False



    def latte():
        if res["water"] >= in_latte["water"] and res["coffee"] >= in_latte["coffee"] and res["milk"] >= in_latte["milk"]:
            water = res["water"] - in_latte["water"]
            coffee = res["coffee"] - in_latte["coffee"]
            milk = res["milk"] - in_latte["milk"]
            res["water"] = water
            res["coffee"] = coffee
            res["milk"] = milk
            print(res)
        elif res["water"] < in_latte["water"]:
            print("there is no enough water")
        elif res["coffee"] < in_latte["coffee"]:
            print("there is no enough coffee")
        elif res["milk"] < in_latte["milk"]:
            print("there is no enough milk")
            # return flag == False

    def cappuccino():
        if res["water"] >= in_cappuccino["water"] and res["coffee"] >= in_cappuccino["coffee"] and res["milk"] >= in_cappuccino["milk"]:
            water = res["water"] - in_cappuccino["water"]
            coffee = res["coffee"] - in_cappuccino["coffee"]
            milk = res["milk"] - in_cappuccino["milk"]
            res["water"] = water
            res["coffee"] = coffee
            res["milk"] = milk
        elif res["water"] < in_cappuccino["water"]:
            print("there is no enough water")
        elif res["coffee"] < in_cappuccino["coffee"]:
            print("there is no enough coffee")
        elif res["milk"] < in_cappuccino["milk"]:
            print("there is no enough milk")
            # return flag == False



    # ask = input("What would you like? (espresso/latte/cappuccino): ")
    # if ask != "report" and ask != "off":
    #     order()
    # elif ask == "off":
    #     flag = False
    # elif ask == "report":
    #     print(res)


    def order():

        print("please insert coins")
        quartar = int(input("how many quartars? "))
        calc = quartar * 0.25

        if ask == "espresso" and calc >= 2.5:
            if calc >= 2.5:
                change = calc - 2.5
                print(f"here is {change} in change")
                espresso()
            elif calc < 2.5:
                print("sorry that's is not enough money")

            # espresso()
        elif ask == "latte" and calc >= 2.5:
            if calc >= 2.5:
                change = calc - 2.5
                print(f"here is {change}")
                latte()
            elif calc < 2.5:
                print("sorry that is not enough money")
            # latte()
        elif ask == "cappuccino":
            if calc >= 2.5:
                change = calc - 2.5
                print(f"here is {change}")
                cappuccino()
        elif calc < 2.5:
            print("sorry that is not enough money")
            # cappuccino()



    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask != "report" and ask != "off":
        order()
    elif ask == "off":
        flag = False
    elif ask == "report":
        print(res)




