from random import randint, choice
import json





def add_to_queue(day, quest): #day číslo, quest je soubor.funkce (například army_quests.attacked(True))
    #načte soubor quest.json (neměnit)
    with open("quest.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    day += data["stats"]["day"]
    #zjistí, jestli je daný den již obsazený
    while str(day) in data["quest_queue"].keys():
        day += 1

    #přidá quest do fronty
    data["quest_queue"][str(day)] = quest

    #zapíše to zpátky do souboru
    with open("quest.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)








add_to_queue(2, "army_quests.pppp()")


def pppp():
    print("pppp")



def attribute_change(army=0, happiness=0, money=0, population=0, diplomacy1=0, diplomacy2=0, magic=0):
  #DODELAT
    pass

class Quest: # Základní class, neměnit
    def __init__(self, name:str, description:str, options:list):
        self.name = name
        self.description = description
        self.options = options

    def __str__(self):
        return f"{self.name}\n{self.description}"

#--------------------------------------#
""""
Scammer = Quest("Scammer", f"Your Majesty, I beg you, to send thy guards to the city market. A vile thief plagues the market, and none dare stop him! Justice is needed. ", [
    {"answer_desc" : "Will you send guards?", "They have greater matters to attend." : attribute_change(happiness=-5), "Justice shall be served...": attribute_change(happiness=5)}
])
PressureWest = Quest("Pressure West", f"Your Majesty, the western border is under pressure. The {m.kingdom1} are attacking our villages. We need to send reinforcements.", [
    {"answer_desc" : "Will you send reinforcements?", "We need to protect our kingdom." : attribute_change(army=-5), "We can trust them, they are definitely just training ." : attribute_change(army=5)}
])
# upravit na cvičení atd


# Storování questů template
quests = {
  "common": [
    Scammer
  ],
  "uncommon": [
    Quest()
  ],
}
"""