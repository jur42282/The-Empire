import random
import json

level = 0
denied_magic = False

def magic():
    if not denied_magic:
        if level == 0:
            for quest in research["lvl0"]:
                if quest.is_complete():
                    continue
                return quest()
        else:
            choiced = random.choice(research["lvl" + str(level)])
            while choiced.is_complete():
                choiced = random.choice(research["lvl" + str(level)])
            return choiced()
        
def get_inventory(): #vrátí inventář (slovník)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    return data["inventory"]
def change_resource(resource, value): #resource - string název věci v inventáři, value - hodnota změny (číslo)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    data["inventory"][resource] += value
    if data["inventory"][resource] < 0:
        raise ValueError("Hodnota materiálu šla do mínusu. Oprav si to pls.")
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
def get_stat(stat): #stat - string název statu
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    return data["stats"][stat]
def change_stat(stat, value): #stat - string název statu, value - hodnota změny (číslo)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    data["stats"][stat] += value
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

class Quest:
    def __init__(self, id:str, prologue:str, description:str, options:list):
        self.id = id
        self.prologue = prologue
        self.description = description
        self.options = options
        self.__completed = False

    def formatCost(self):
        if len(self.options[0]["cost"]) > 0:
          return ", ".join(f"{key}: {value}" for key, value in self.options[0]["cost"].items())
        else:
          return "Nothing"

    def __str__(self):
        return f"{self.prologue}\n\n{self.description}\n\n{self.options[0]['answer_desc']}\n\nThis action will cost you: {self.formatCost()}"
    
    def __call__(self):
        global denied_magic
        print(self, end=" ")
        user_input = input("\033[1m[Y/N]: ").lower()
        if user_input == "y":
            return self.options[0]["yes"]()
        else:
            if research["lvl0"][0] == self:
                denied_magic = True
            return self.options[0]["no"]()
    
    def is_complete(self):
        return self.__completed
    def completed(self):
        self.__completed = True

def test():
    print("hahahaha")

def everything_is_ok(kwargs):
    everything_is_okay = True
    inventory = get_inventory()
    for item, value in kwargs.items():
        if item == "gold":
            if get_stat("money") - value < 0:
                print(f"You don't have enough {item} ({- (get_stat("money") - value)} missing).")
                everything_is_okay = False
        elif inventory[item] - value < 0:
            print(f"You don't have enough {item} ({- (inventory[item] - value)} missing).")
            everything_is_okay = False
    return everything_is_okay
    
def decision(quest,**kwargs):
    def effect():
        if everything_is_ok(kwargs):
            quest.completed() # this is wrong!!!!!!!!!
            for item, value in kwargs.items():
                if item == "gold":
                    change_stat("money", -value)
                else:
                    change_resource(item, -value)
        else:
            print("Quest was automatically denied.")

        print("proměnné změněny:)")
    # stats = json.load(open("quest.json","r",encoding='utf-8'))
    # for key, value in kwargs.items():
    #     stats[key] += value
    # json.dump(stats,open("quest.json","w",encoding='utf-8'),indent=4)
    return effect

class Answer:
    def __init__(self, description, epilogue, function):
        self.description = f'\nEmpress Gažarová:\033[0m "{description}"\n'
        self.epilogue = epilogue
        self.function = function
    
    def __call__(self):
        self.function()
        print(self.description)
        print(self.epilogue)
        return ""
    

mage_name = "\033[1mJohn\033[0m"
mage_ranks = ["\033[1mAspiring Mage\033[0m", "\033[1mApprentice Mage\033[0m", "\033[1mTower Mage\033[0m", "\033[1mMaster Mage\033[0m", "\033[1mThe Great Mage\033[0m", "\033[1mThe Grand Archmage\033[0m"]

research = {
  "lvl0": [
    Quest(
      "tower_permission",
      f"An ambitious mage stands before the mighty Empress, his heart filled with arcane dreams. With great respect, he presents his request—to construct a grand Magic Tower within her lands, a sanctuary where mages from across the realm may gather, study, and advance the art of magic.",
      f'{mage_ranks[0]} {mage_name}: "Your Majesty, I humbly seek your permission to construct a Magic Tower within your lands—a sanctuary where mages from across the realm may gather, study, and advance the arcane arts. With your blessing, we shall create a beacon of knowledge and power that will serve the kingdom for generations to come. Will you grant us this honor?"',
      [{
        "answer_desc": "Will you grant permission for the Magic Tower to be built within your lands?",
        "cost": {},
        "yes":
          Answer(
            "You have my blessing. May your Magic Tower become a pillar of wisdom and strength for the realm.",
            "With the Empress's approval, the Magic Tower took shape. Mages gathered, knowledge flourished, and the aspiring mage's dream became reality—a beacon of magic within the empire.",
            decision("tower_permission"),
          ),
        "no":
          Answer(
            "I cannot allow this. Magic is a force both wondrous and dangerous—I will not take such a risk within my lands.",
            "Without the Empress's blessing, the mage left in search of a new land. Though the Magic Tower would not rise in the empire, his vision found a home elsewhere, and his name became legend beyond its borders.",
            decision("tower_permission"),
          ),
      }],
    ),
    Quest(
      "tower_construction",
      f"After receiving permission to build the Magic Tower, the aspiring mage returns once more to the Empress. Though construction has begun, progress is slow, and resources are dwindling. With great humility, he now seeks financial support to hasten the completion of this grand project.",
      f'{mage_ranks[0]} {mage_name}: "Your Majesty, the Magic Tower rises, but not as swiftly as I had hoped. Our resources are stretched thin, and without aid, its completion may take years. I humbly ask for your support—your generosity would ensure that this beacon of magic stands strong within your kingdom far sooner. Will you grant us this assistance?"',
      [{
        "answer_desc": "Will you provide financial support to aid in the swift completion of the Magic Tower?",
        "cost": {'Gold': 200, 'Iron': 10},
        "yes":
          Answer(
            "Very well. The kingdom shall invest in your vision—see to it that this tower becomes a source of wisdom and strength for my people.",
            "With the Empress's aid, the Magic Tower rose swiftly. Mages filled its halls, and in gratitude, the mage swore loyalty to the empire, ensuring magic's lasting place in its future.",
            decision(),
          ),
        "no":
          Answer(
            "I have already granted you my permission; I will not grant you my gold. If your tower is meant to stand, let it rise by your own means.",
            "Lacking imperial support, the mage sought other patrons. Though progress was slow, his determination never wavered. In time, the Magic Tower stood—not by royal decree, but by sheer will.",
            decision(),
          ),
      }],
    ),
  ],
  "lvl1": [
    Quest(
      "harvest_effectivity",
      f"desc",
      f'{mage_ranks[1]} {mage_name}: "dialog text"',
      [{
        "answer_desc": "desc of harvesting answer",
        "cost": {},
        "yes":
          Answer(
            "dialog when approved",
            "desc when approved",
            test,
          ),
        "no":
          Answer(
            "dialog when disapproved",
            "desc when disapproved",
            test,
          ),
      }],
    ),
  ],
  "lvl2": [],
  "lvl3": [],
  "lvl4": [],
  "lvl5": [],
}

ruins = {
    "small": [],
    "medium": [],
    "large": [],
}

events = {
    "small": [],
    "medium": [],
    "large": [],
}

# print(magic())
# print("-------"*16)
# print(magic())
# Quest(
#   "",
#   f"",
#   f'{mage_ranks[0]} {mage_name}: ""',
#   [{
#     "answer_desc": "",
#     "cost": {},
#     "yes":
#       Answer(
#         "",
#         "",
#         test,
#       ),
#     "no":
#       Answer(
#         "",
#         "",
#         test,
#       ),
#   }],
# ),