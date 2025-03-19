from random import choice
import json
import army_quests

quest_queue = { # Questy, které mají dopad později v čase 
# příklad  "10": "example_quest" # Quest "example_quest" se spustí až na 10. den
}

with open("quest.json", "r", encoding="utf-8") as f: 
    data = json.load(f)

def random_quest():
    return choice(quests)

quests = ["fsdfsfd", "sdfsgd", "dhsc", "ffgsd"]