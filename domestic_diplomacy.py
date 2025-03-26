import random as rd
import json

class Atribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"

class Quest:
    def __init__(self, name, description, effect_function, decline_effect, rarity):
        self.name = name
        self.description = description
        self.effect_function = effect_function
        self.decline_effect = decline_effect
        self.rarity = rarity
        self.__completed = False

    def __str__(self):
        return f"{self.name} ({self.rarity})\n{self.description}\nAccept this quest? (Y/N)"

    def __call__(self):
        if self.__completed:
            return ""

        print(self)
        answer = input("Do you accept this quest? (Y/N): ").strip().lower()

        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        stats = data["stats"]

        # apply effect or decline effect
        if answer == "y":
            stats = self.effect_function(stats)
        else:
            stats = self.decline_effect(stats)

        # save updated stats
        data["stats"] = stats

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        self.__completed = True
        return ""

    def is_complete(self):
        return self.__completed

# positive quests
def raise_taxes(stats):
    stats["money"] += 3
    stats["happiness"] -= 2
    return stats

def build_university(stats):
    stats["money"] -= 10
    stats["happiness"] += 5
    stats["magic"] += 2
    return stats

def train_knights(stats):
    stats["army"] += 2
    stats["happiness"] -= 3
    return stats

def provide_healing(stats):
    stats["money"] -= 5
    stats["happiness"] += 4
    return stats

def repair_roads(stats):
    stats["money"] -= 10
    stats["happiness"] += 3
    return stats

def hold_festival(stats):
    stats["money"] -= 10
    stats["happiness"] += 6
    return stats

def support_mages(stats):
    stats["money"] -= 8
    stats["magic"] += 3
    return stats

def grant_farmland(stats):
    stats["money"] -= 5
    stats["population"] += 1
    return stats

def build_castle_wall(stats):
    stats["money"] -= 10
    stats["army"] += 5
    return stats

def organize_tournament(stats):
    stats["money"] -= 20
    stats["happiness"] += 8
    return stats

# negative quests
def decline_raise_taxes(stats):
    stats["money"] -= 3
    return stats

def decline_build_university(stats):
    stats["magic"] -= 2
    return stats

def decline_train_knights(stats):
    stats["army"] -= 2
    return stats

def decline_provide_healing(stats):
    stats["happiness"] -= 3
    return stats

def decline_repair_roads(stats):
    stats["happiness"] -= 2
    return stats

def decline_hold_festival(stats):
    stats["happiness"] -= 3
    return stats

def decline_support_mages(stats):
    stats["magic"] -= 1
    return stats

def decline_grant_farmland(stats):
    stats["population"] -= 1
    return stats

def decline_build_castle_wall(stats):
    stats["army"] -= 3
    return stats

def decline_organize_tournament(stats):
    stats["happiness"] -= 3
    return stats

quests = [
    Quest("Raise Taxes", "Increase royal taxes to gain more money, but anger the people.", raise_taxes, decline_raise_taxes, 'Common'),
    Quest("Build University", "Found a center of learning to increase knowledge and happiness.", build_university, decline_build_university, 'Uncommon'),
    Quest("Train Knights", "Recruit and train knights to strengthen the army but reduce happiness.", train_knights, decline_train_knights, 'Common'),
    Quest("Provide Healing", "Offer healing to the sick, improving happiness but reducing money.", provide_healing, decline_provide_healing, 'Common'),
    Quest("Repair Roads", "Invest in better roads to ease travel and trade, improving happiness.", repair_roads, decline_repair_roads, 'Uncommon'),
    Quest("Hold Festival", "A grand festival boosts morale but costs money.", hold_festival, decline_hold_festival, 'Common'),
    Quest("Support Mages", "Fund magical scholars to improve the kingdom’s knowledge.", support_mages, decline_support_mages, 'Rare'),
    Quest("Grant Farmland", "Distribute farmland to the poor, boosting population growth.", grant_farmland, decline_grant_farmland, 'Uncommon'),
    Quest("Build Castle Wall", "Construct strong defenses to protect the kingdom.", build_castle_wall, decline_build_castle_wall, 'Rare'),
    Quest("Organize Tournament", "A tournament brings joy and entertainment but is expensive.", organize_tournament, decline_organize_tournament, 'Legendary')
]

def diplomacy():
    available = [q for q in quests if not q.is_complete()]
    if not available:
        return ""
    quest = rd.choice(available)
    return quest()
