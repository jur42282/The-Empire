import random as rd
import source as src


""""
Nákup zbraní, Nákup jídla, nemovitostí -> +X % spokojenosti obyvatel, stavba památek a kulturních objektů, odkoupení surovin/zboží od jiného království, pořádání slavností +spokojenost, -finance, -jídlo

Prodej surovin, jídla jinému království, X goldů za splnění questu
Obchod pro lidi/jiné království
"""




quests = {
    "common": [
        Quest("Arrival of the nobleman", "Organization of a celebration in honor of his arrival", [{"answer_desc": "You will organize a celebration in his honor", "yes" : nobleman_yes(), "no": nobleman_no()}]
)
    ]
}

def nobleman_yes():
    if money.value >= 1000:
        print("Uspořádal jsi slavnost a vyšla tě na 1000 goldů, a obyvatelé jsou spokojenější o 4%")
        money.value -= 1000

        happiness.value += 4 

    else:
        print("You don't have enough money! ")
        happiness.value -= 4 

def nobleman_no():
    print("You declined nobleman and ")
    happiness.value -= 4


# class Mines():
#     def __init__(self, workers : int, ) -> None:
#         pass



# print(money.value)
# print(happiness.value)



    