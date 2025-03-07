import main as m
from random import randint, choice





def attribute_change(army=0, happiness=0, money=0, population=0, diplomacy1=0, diplomacy2=0, magic=0):
    m.army += army
    m.happiness += happiness
    m.money += money
    m.population += population
    m.diplomacy1 += diplomacy1
    m.diplomacy2 += diplomacy2
    m.magic += magic

class Quest: # Základní class, neměnit
    def __init__(self, name:str, description:str, options:list):
        self.name = name
        self.description = description
        self.options = options

    def __str__(self):
        return f"{self.name}\n{self.description}"

#--------------------------------------#
def dneski_sance(diplomacy, kingdom, b_time):
  time = b_time + randint(3,7)
  if time >= time:

    pass

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

