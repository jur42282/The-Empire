# Importy #
import random as rd
# import quest_selector as qs
import json
###########

def load_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

print(load_json("quest.json"))
    
kingdom1 = "Elven Kingdom"
kingdom2 = "Dwarfs Kingdom"

# army = Atribute("Army", 1)
# happiness = Atribute("Population Happiness", 2)
# money = Atribute("Gold", 10)
# population = Atribute("Population", 100)
# diplomacy1 = Atribute(kingdom1, 1)
# diplomacy2 = Atribute(kingdom2, 1)
# magic = Atribute("Magic", 0)

# print(army)
# print(happiness)
# print(money)
# print(population)
# print(diplomacy1)
# print(diplomacy2)
# print(magic)



# Main Loop
day = 1
while True:
    print(f"Day: {day}")
    # print(army)
    # print(happiness)
    # print(money)
    # print(population)
    # print(diplomacy1)
    # print(diplomacy2)
    # print(magic)
    # print(f"Current quest: {qs.random_quest()}")
    input()
    day += 1