import random as rd
import source as src


""""
Nákup zbraní, Nákup jídla, nemovitostí -> +X % spokojenosti obyvatel, stavba památek a kulturních objektů, odkoupení surovin/zboží od jiného království, pořádání slavností +spokojenost, -finance, -jídlo

Prodej surovin, jídla jinému království, X goldů za splnění questu
Obchod pro lidi/jiné království
"""


class Atribute:
    def init(self, name, value):
        self.name = name
        self = value * rd.randint(10, 15)

    def str(self):
        return f"{self.name}: {self}"

kingdom1 = "Elven Kingdom"
kingdom2 = "Dwarfs Kingdom"

army = Atribute("Army", 1)
happiness = Atribute("Population Happiness", 2)
money = Atribute("Gold", 1000)
population = Atribute("Population", 100)
diplomacy1 = Atribute(kingdom1, 1)
diplomacy2 = Atribute(kingdom2, 1)
magic = Atribute("Magic", 0)


class Quest:
    def init(self, name:str, description:str, options:list):
        self.name = name
        self.description = description
        self.options = options

    def str(self):
        return f"{self.name}\n{self.description}"

# inventory = [{"food":50}, {"silver":10}, {""}]

def nobleman_yes():
    if money >= 1000:
        print("You will organize a celebration in his honor and it cost you a 1000 golds and citizens are happier by 4 %.")
        money -= 1000
        if happiness <= 96:
            happiness += 4
        else:
            happiness
    else:
        print("You don't have enough money! ")
        happiness -= 4 
def nobleman_no():
    print("You declined nobleman and citizens are less happier by 4 %.")
    happiness -= 4


def field_yes():
    if money >= 20000 and population >= 10:
        population -= 10
        money -= 20000
        if happiness  >= 98:
            happiness = 100
        else:
            happiness += 2
        print("You built a field and the happiness of citizens has increased by 2 %. It cost you 20000 golds and you have hired 10 farmers.")
        # Každý den by se přičetlo 300 jídla, které by se dalo dále prodávat
    else:
        print("You dont have enough resources.")

def field_no():
    if happiness >= 2:
        happiness -= 2
    else:
        happiness = 0
    print("You declined to built a field and happiness of citizens has decreased by 2 %.")


def build_yes():
    if money >= 100000:
        money -= 100000
        population += 40
        if happiness <= 85:
            happiness += 15
        else:
            happiness = 100
        print("You have built new dwellings for the inhabitants, and 40 new people have joined. The residents are 15% happier, and the entire construction cost you 100,000 gold.")
    else:
        print("You dont have enough resources.")

def build_no():
    if happiness >= 10:
        happiness -= 10
    else:
        happiness = 0
    print("You disagreed with this idea and your citizens are less happier by 15 %.")



def baby_yes():
    if money >= 15000:
        money -= 15000
        population += 100

        if happiness <= 95:
            happiness += 5
        else:
            happiness = 100
        print("You built a maternity hospital and 100 babies has been born.")

def baby_no():
    if happiness >= 10:
        happiness -= 10
    else:
        happiness = 0
    print("You declined to build a new maternity hospital and the happiness has been decreased by 10 %.")



def wheat1_yes():
    if wheat >= 100:
        wheat -= 100
        money += 500
        print("You made a deal. You sold a 100 pt of wheat for 500 gold.")
    else:
        print("You dont have enough amount of wheat.")

def wheat1_no():
    print("You rejected the offer and the trader continued on his way.")


def execute_yes():
    if money >= 200:
        money -= 200
        if population >= 1:
            population -= 1
            if happiness <= 94:
                happiness += 6
            else:
                happiness = 100
            print("You have arranged the execution and satisfied a lot of people. It cost you 200 gold and population happines increased by 6 %.")
        else:
            ("You dont have anyone to execute.")
    else:
        print("You dont have enough gold")
def execute_no():
    if happiness >= 6:
        happiness -= 6
    else:
        happiness = 0
    print("You declined an execution and the bandit goes to jail. Population happiness decreased by 6 %.")

quests = {
    "common": [
        Quest("Nobleman arrival", "The city is buzzing with excitement—a nobleman of great renown, whose name is whispered in reverent conversations, is set to arrive soon! His presence could bring wealth, new alliances, or... unexpected intrigue. The local ruler has entrusted you with an important task: to organize a grand feast that will impress not only the nobleman but the entire court.", [{"answer_desc" : "You will organize a celebration in his honor.", "yes" : nobleman_yes(), "no": nobleman_no()}]),
        Quest("Take care of the field!", "The local villagers have long complained about the lack of fertile land and the ever-growing needs of the city. Now is the time to act! The local ruler has entrusted you with an important task—building a new field that will provide enough food for the inhabitants and trade caravans.", [{"answer_desc" : "Build a field and claim resources every day! Will you do it?","yes": field_yes() , "no": field_no()}]),
        Quest("New Houses!", "The city is growing, and with it, the need for new homes for incoming settlers, traders, and craftsmen. The local ruler has entrusted you with an important task—to build new dwellings and ensure that the new inhabitants have a place to rest their heads!", [{"answer_desc" : "Build more houses for citizens. Do you agree?","yes": build_yes() , "no": build_no()}]),
        Quest("Increase the population!", "The city is growing, and with it comes the need to secure its future. The local ruler has entrusted you with an important task—to build a new maternity hospital that would support higher birth rates and ensure the continuation of the lineage for future generations. Creating such a facility is crucial for the long-term growth of the city's population and securing a workforce for various trades.", [{"answer_desc" : "Build a Maternity hospital and increase the amount of citizens. Will you do that?","yes": baby_yes() , "no": baby_no()}]),
        Quest("You got an offer from treader!", "A merchant from a distant kingdom has arrived in the city, accompanied by a large caravan. He claims that his land is suffering from poor harvests and famine, and he is seeking a reliable supplier of grain. He offers a generous sum of gold in exchange.", [{"answer_desc" : "The dealer offers you a trade, 100 pt of wheat for a 500 gold.","yes": wheat1_yes() , "no": wheat1_no()}]),
        Quest("Public execution!", "After weeks of robberies and attacks on travelers, the feared bandit has finally been captured! He is now imprisoned in the city dungeon, awaiting his sentence. The townspeople cry out for justice—his crimes deserve punishment, and what better warning for other criminals than a public execution?", [{"answer_desc" : "Will you arrange the execution of the bandit from your kingdom and satisfy your people?","yes": execute_yes() , "no": execute_no()}])
    ]}
