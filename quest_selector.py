from random import choice
import json
import army_quests
import magic_quests
import domestic_diplomacy
# import finance?

def get_stat(stat): #stat - string název statu
    #načte soubor data.json (neměnit)
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    return data["stats"][stat]

def choose_quest():
    with open("data.json", "r", encoding="utf-8") as f: 
        data = json.load(f)
    current_day = get_stat("day")
    if str(current_day) in data["quest_queue"].keys():
        func = data["quest_queue"][str(current_day)]
        return eval(func)
    return choice(quest_categories)()

quest_categories = [magic_quests.magic, army_quests.ddddd, domestic_diplomacy.diplomacy]