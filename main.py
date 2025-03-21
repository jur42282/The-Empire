# Importy #
import random as rd
import quest_selector as qs
import json
###########

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

set_stat("army", rd.randint(50,150))
set_stat("money", rd.randint(5000,10000))
set_stat("population", rd.randint(100,150))
set_stat("diplomacy1", 50)
set_stat("diplomacy2", 50)
set_stat("happiness", 50)
set_stat("magic", 0)
set_stat("day", 0)

# Main Loop
game_running = True

while game_running:
    change_stat("day", 1)
    for key, value in json.load(open("data.json", "r", encoding="utf-8"))["stats"].items():
        print(f"{key.capitalize()}: {value}")
    qs.choose_quest()
    input()