from random import randint, choice
import json





def get_stat(stat): #stat - string název statu
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    return data["stats"][stat]

def change_stat(stat, value): #stat - string název statu, value - hodnota změny (číslo)
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    
    data["stats"][stat] += value

    #zapíše to zpátky do souboru
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    
def set_stat(stat, value):
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    
    data["stats"][stat] = value

    #zapíše to zpátky do souboru
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)







# change_stat(stat, value)
# get_stat(stat)

def add_to_queue(day, quest): #day číslo, quest je soubor.funkce (například army_quests.attacked(True))
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    day += data["stats"]["day"]
    #zjistí, jestli je daný den již obsazený
    while str(day) in data["quest_queue"].keys():
        day += 1

    #přidá quest do fronty
    data["quest_queue"][str(day)] = quest

    #zapíše to zpátky do souboru
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)





def pppp():
    print("pppp")
def ddddd():
    print("ddddd")



def attribute_change(army=0, happiness=0, money=0, population=0, diplomacy1=0, diplomacy2=0, magic=0):
  #DODELAT
    pass

class Quest: # Základní class, neměnit
    def __init__(self, name:str, description:str, options:list, action:list):
        self.name = name
        self.description = description
        self.options = options
        self.action = action

    def __str__(self):
        return f"{self.name}\n{self.description}"
    
    def __call__(self):
        print(self, end=" ")
        print("You have those options:")
        count = 1
        for i in self.options:
            print(f"{count}) {i}")
            count += 1
        user_input = input("Choose an option: ")
        self.action[int(user_input)-1]()
        return ""

#--------------------------------------#

Scammer = Quest(
    "Scammer",
    "Your Majesty, I beg you, to send thy guards to the city market. A vile thief plagues the market, and none dare stop him! Justice is needed. \n Will you send guards?",
    ["Yes, justice shall be served...", "No, they have greater matters to attend."],
    [lambda: change_stat("happiness", -5), lambda: change_stat("happiness", 5)]
)

Blackmailer = Quest(
    "Blackmailer",
    "On my way to the forest I came across a troll. He said I must either pay him or he will be evil. I need soldiers to fight.",
    ["Yes, send 5 armed soldiers to fight, some of them might survive","No, pay him and run away"],
    [lambda: change_stat("army", -3), lambda: change_stat("money", -60)]
)

Recruitment = Quest(
    "Recruitment",
    "There will be a recruitment of new soldiers, but the training and tests will not be cheap! \nEither you pay and we will get 18 new and fresh guys, or we will save money but our army will be the same",
    ["Yes, do the recruiting, new guys are good for us","No, our army is good, let's save money"],
    [lambda: change_stat("army", 18), change_stat("money", -120),
     lambda: change_stat("money", 0)]
)

"""
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
    Recruitment
  ],
  "common": [
    Blackmailer
  ],
}
"""

print(Recruitment())