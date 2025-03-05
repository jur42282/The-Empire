class Quest: # Záladní class, neměnit
    def __init__(self, name:str, description:str, options:list):
        self.name = name
        self.description = description
        self.options = options

    def __str__(self):
        return f"{self.name}\n{self.description}"
    
# zakládání questu    
quest1 = Quest("quest1", "Testovací quest", [
    {"answer_desc" : "Zaplať 500G", "yes" : "<funkce1>", "no": "<funkce2>"}
])

# Storování questů template
quests = {
  "common": [
    Quest()
  ],
  "uncommon": [
    Quest()
  ],
}