# Importy #
import random as rd
import quest_selector as qs
###########

# class Atribute:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value * rd.randint(10, 15)

#     def __str__(self):
#         return f"{self.name}: {self.value}"
    
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
    print(army)
    print(happiness)
    print(money)
    print(population)
    print(diplomacy1)
    print(diplomacy2)
    print(magic)
    print(f"Current quest: {qs.random_quest()}")
    input()
    day += 1
