import main as m

class Quest: # Záladní class, neměnit
    def __init__(self, name:str, description:str, options:list):
        self.name = name
        self.description = description
        self.options = options

    def __str__(self):
        return f"{self.name}\n{self.description}"
    
# zakládání questu
quest1 = Quest("Scammer", "Your Majesty, I beg you, to send thy guards to the city market. A vile thief plagues the market, and none dare stop him! Justice is needed. ", [
    {"answer_desc" : "Will you send guards?", "They have greater matters to attend." : "<funkce1>", "Justice shall be served...": "<funkce2>"}
])

# Storování questů template
quests = {
  "common": [
    Quest()
  ],
  "uncommon": [
    Quest()
  ],
}

char = "PanzerKommandantLukas"

def attribute_change(army=0, happiness=0, money=0, population=0, diplomacy1=0, diplomacy2=0, magic=0):
    m.army += army
    