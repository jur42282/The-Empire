player_inventory =[
    {"wheat": 0},
    {"coal": 10},
    {"wood": 100},
    {"stone": 100}
]


# if player_inventory["wood"] >= 100:
#     print("You have enough wood")

# print(player_inventory[2])
# print(player_inventory[2].get("wood"))


def sell_material():
    for material in player_inventory:
        print(material)
    selected_material = input("Select material to sell: ")
    selected_material = selected_material.lower()
    print(selected_material)


# sell_material()