import random
import json

def change_stat(stat, value): #stat - string název statu, value - hodnota změny (číslo)
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)

class ItemManager():
    def __init__(self, name : str, desc : str, price : int, can_sell = False) -> None:
        self.name = name
        self.desc = desc
        self.price = price
        self.can_sell = can_sell

    def __str__(self) -> str:
        return f" \n name: {self.name} \n description: {self.desc} \n price : {self.price}"


class ShopManager():

    def __init__(self) -> None:
        pass

    shop = [
        ItemManager("Choice n.1", "c1", 1000),
        ItemManager("Choice n.2", "c2", 2000),
        ItemManager("Choice n.3", "c3", 3000)
            ]



    def open_shop():
        for item in ShopManager.shop:
    
            print(f"{item}")
    
    def choice():
        global user_choice_shop
        user_choice_shop = input("Choose your option: ")
        if int(user_choice_shop) in range(0, len(ShopManager.shop) + 1):
            user_choice_real = int(user_choice_shop) - 1
            item = ShopManager.shop[user_choice_real]
            print(f"You have selected {item.name} for {item.price} golds!")
            print("Do you want to buy this item?")

            #opatřit inputy aby necrashovalo
            while True:
                global final_choice_shop
                amount = input("How much of this item you want to buy? (write number - or if you want to go back write 0): ")
                
                if amount.isnumeric():
                    amount = int(amount)
                    if amount > 0:
                        print(f"You want to buy {amount} of {item.name} for {item.price * amount} golds?")
                        final_choice_shop = input("yes/no: ")
                        break
                    #PŘIDAT MOŽNOST "ZPÁTKY" DO SHOPU
                    else:
                        print("Please, enter a number!") # oveřit funkčnost
                else:
                    print("Please, enter a number!")
                


            if final_choice_shop == "yes":
                print(f"You have bought {item.name}!")
                change_stat("money", (-item.price * amount)) # oveřit funkčnost

            else:
                print("You didn't buy the item!")
        else:
            print("upsík")
            print(len(ShopManager.shop))

        




def call_shop():
    shop_entity = ShopManager
    shop_entity.open_shop()
    shop_entity.choice()

# for i in(ShopManager.shop):
#     print(i)

call_shop()


#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p
#SHOP work in progress bude brzy dw :p