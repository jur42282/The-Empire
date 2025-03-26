
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
        print("Dokončil jsi obchod. Prodal jsi 100 obilí za 500 goldů.")
    else:
        print("Nemáš dostatek obilí.")

def wheat1_no():
    print("Odmítl jsi obchodníka a on pokračuje dál.")


def execute_yes():
    if money >= 200:
        money -= 200
        if population >= 1:
            population -= 1
            if happiness <= 94:
                happiness += 6
            else:
                happiness = 100
            print("Uspořádal jsi veřejnou popravu a uspokojil jsi lid. Stála tě 200 goldů a obyvatelé jsou o 6% více spokojeni.")
        else:
            ("Nemáš ve svém království koho popravit.")
    else:
        print("Nemáš dostatek goldů.")
def execute_no():
    if happiness >= 6:
        happiness -= 6
    else:
        happiness = 0
    print("Odmítl jsi uspořádat popravu a lapka půjde do žaláře. Obyvatelé jsou o 6 % méně spokojeni.")

quests = {
    "common": [
        Quest("Nobleman arrival", "The city is buzzing with excitement—a nobleman of great renown, whose name is whispered in reverent conversations, is set to arrive soon! His presence could bring wealth, new alliances, or... unexpected intrigue. The local ruler has entrusted you with an important task: to organize a grand feast that will impress not only the nobleman but the entire court.", [{"answer_desc" : "You will organize a celebration in his honor.", "yes" : nobleman_yes(), "no": nobleman_no()}]),
        Quest("Take care of the field!", "The local villagers have long complained about the lack of fertile land and the ever-growing needs of the city. Now is the time to act! The local ruler has entrusted you with an important task—building a new field that will provide enough food for the inhabitants and trade caravans.", [{"answer_desc" : "Build a field and claim resources every day! Will you do it?","yes": field_yes() , "no": field_no()}]),
        Quest("New Houses!", "The city is growing, and with it, the need for new homes for incoming settlers, traders, and craftsmen. The local ruler has entrusted you with an important task—to build new dwellings and ensure that the new inhabitants have a place to rest their heads!", [{"answer_desc" : "Build more houses for citizens. Do you agree?","yes": build_yes() , "no": build_no()}]),
        Quest("Increase the population!", "The city is growing, and with it comes the need to secure its future. The local ruler has entrusted you with an important task—to build a new maternity hospital that would support higher birth rates and ensure the continuation of the lineage for future generations. Creating such a facility is crucial for the long-term growth of the city's population and securing a workforce for various trades.", [{"answer_desc" : "Build a Maternity hospital and increase the amount of citizens. Will you do that?","yes": baby_yes() , "no": baby_no()}]),
        Quest("Přišla ti nabídka od obchodníka", "Přijel obchodník z dalekého království a chce uzavřít obchod.", [{"answer_desc" : "Přijel obchodník z jiného království a chce odkoupit 100ks obilí.","yes": wheat1_yes() , "no": wheat1_no()}]),
        Quest("Veřejná poprava", "Lapka byl chycen a nyní čeká na svůj rozsudek. Potěš své obyvatele a uspořádej veřejnou popravu.", [{"answer_desc" : "Uspořádej popravu lapky z tvého království","yes": execute_yes() , "no": execute_no()}])
    ]}

