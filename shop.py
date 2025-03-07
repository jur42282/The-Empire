import random

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
        ItemManager("Fontána","Postav fontánu a zvyš happiness obyvatelstva o 10%",1000),
        ItemManager("Fontána","Postav fontánu a zvyš happiness obyvatelstva o 40%",1000),
        ItemManager("Fontána","Postav fontánu a zvyš happiness obyvatelstva o 50%",1000)
            ]

    def open_shop():
        pocitadlo = 0
        for item in ShopManager.shop:
            pocitadlo += 1
            print(f" [{pocitadlo}] {item}")
    
    def choice():
        user_choice = input("Choose your option: ")
        if user_choice in range(0, len(ShopManager.shop)):
            item = ShopManager.shop[user_choice -1]
            print("Vybral jsi f{item.name}")
        else:
            print("kkt")
            print(len(ShopManager.shop))

        



def call_shop():
    shop_entity = ShopManager
    shop_entity.open_shop()
    shop_entity.choice()


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