import random
import json




def change_stat(stat, value): #stat - string název statu, value - hodnota změny (číslo)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    data["stats"][stat] += value
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_stat(stat): #stat - string název statu
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    return data["stats"][stat]

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
        pocitadlo = 0
        for item in ShopManager.shop:
            pocitadlo += 1
            print(f" [{pocitadlo}] {item}")
            print("\n")
        print(" [exit] - Exit shop")
            

    
    def choice():
        global user_choice_shop
        global exit_shop_active
        exit_shop = "exit"
        while True:
            
            user_choice_shop = input("Choose your option: ")
            if str(user_choice_shop) == exit_shop:
                print("You have left the shop!")
                exit_shop_active = True
                break

            if int(user_choice_shop) in range(0, len(ShopManager.shop) + 1):
                user_choice_real = int(user_choice_shop) - 1
                item = ShopManager.shop[user_choice_real]
                print(f"You have selected {item.name} for {item.price} golds!")
                print("Do you want to buy this item?")

            #opatřit inputy aby necrashovalo
            while True:
                global final_choice_shop
                global amount_item

                if exit_shop_active == True:
                    print("You have left the shop!")
                    exit_shop_active = False
                    break

                if final_choice_shop == "yes" or final_choice_shop == "no":
                    break

                amount_item = input("How much of this item you want to buy? (write number - or if you want to go back write 0): ")
                
                if amount_item.isnumeric():
                    amount_item = int(amount_item)
                    if amount_item > 0:
                        print(f"You want to buy {amount_item} of {item.name} for {item.price * amount_item} golds?")
                        final_choice_shop = input("yes/no: ")
                        
                        if final_choice_shop == "yes" or final_choice_shop == "no":
                            break
                        else:
                            print("Please, enter yes or no!")
                            while True:
                                final_choice_shop = input("yes/no: ")
                                if final_choice_shop == "yes" or final_choice_shop == "no":
                                    break
                            


                    #PŘIDAT MOŽNOST "ZPÁTKY" DO SHOPU
                    elif amount_item == 0:
                        final_choice_shop = None
                        break
                        
                    else:
                        print("Please, enter a number!") # oveřit funkčnost
                else:
                    print("Please, enter a number!")
                
            if amount_item == 0:
                call_shop()

            elif final_choice_shop == "yes":
                if get_stat("money") < item.price * amount_item:
                    print("You don't have enough golds!")
                    call_shop()
                else:
                    print(f"You have bought {item.name}!")
                    change_stat('money', (-(item.price * amount_item))) # oveřit funkčnost
                    print(f"You have {get_stat('money')} golds left!")
                    call_shop()

            

            else:
                print("You didn't buy the item!")
        else:
            print("upsík")
            print(len(ShopManager.shop))

        
def variable_reset_shop():
    global user_choice_shop
    global final_choice_shop
    global exit_shop_active
    global amount_item
    user_choice_shop = None
    final_choice_shop = None
    exit_shop_active = False
    amount_item = None

def call_shop():
    variable_reset_shop()
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