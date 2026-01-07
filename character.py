
class Class:
    def __init__(self, name, money, hp, phydmg, rngdmg, mgcdmg, mana, inv, race, classs):
        self.name = name
        self.money = money
        self.hp = hp
        self.phydmg = phydmg
        self.rngdmg = rngdmg
        self.mgcdmg = mgcdmg
        self.mana = mana
        self.inv = inv
        self.race = race
        self.classs = classs
    def human(self):
        self.money += 24
        self.hp += 99
        self.mana += 10
        self.race.append("Human")
    def demon(self):
        self.money += 9
        self.hp += 74
        self.phydmg += 1
        self.mana += 5
        self.race.append("Demon")
    def angel(self):
        self.money += 9
        self.hp += 99
        self.mgcdmg += 1
        self.mana += 15
        self.race.append("Angel")
    def dwarf(self):
        self.money += 24
        self.hp += 74
        self.phydmg -= 0.5
        self.mana += 5
        self.race.append("Dwarf")

    #Races

    def Warrior(self):
        self.phydmg += 1
        self.classs.append("Warrior")

    def Archer(self):
        self.rngdmg += 1

    def Mage(self):
        self.mgcdmg += 1
        self.mana += 5
        
self = Class("John", 1, 1, 1, 0, 0, 0, [], [], [])

while True:
    user_input = input("Please choose a race!: Human, Demon, Angel, Dwarf - Remember you will not be able to change these later on. Keep in mind each race will have their own buffs/debuffs. If you would like to get info about these races, please type 'info'").lower()
    if user_input == "info":
        print("The human class, the jack of all trades - master of none. This race is capable of becoming all of the classes, and poses no debuffs. All stats of this race are default. The demon class is a master of combat, specializing in close ranged physical fights. The demon class has high damage and a special ability, but sacrifices some health for it. Demon is incapable of using ranged weapons. The angel race is similar to the human race, but has a few passives and abilities. The angel is capable of using its wings to dodge attacks and is eligible to use all types of weapons and is stronger with magic type attacks. The dwarf race specializes in ranged combat, being small enough to evade attacks. The dwarf class is weaker with physical weapons, and stronger with ranged weapons.")
    elif user_input == "human":
        self.human()
        break
    elif user_input == "demon":
        self.demon()
        break
    elif user_input == "angel":
        self.angel()
        break
    elif user_input == "dwarf":
        self.dwarf()
        break
    else:
        print("Answer not reconized, please try again.")

while True:
    user_input = input("Please choose a class for your character, remember that some classes wont be capable of becoming specific classes. - Warrior - Archer - Mage -").lower()
    if user_input == "warrior":
        self.Warrior()
        print("Class chosen: Warrior")
        break
    elif user_input == "archer" and self.race != ["Demon"]:
        self.Archer()
        print("Class Chosen: Archer")
        break
    elif user_input == "mage" and self.race != ["Demon"]:
        self.Mage()
        print("Class Chosen: Mage")
        break

#_________________________________________________________________________________________
weapontype=[
    {
        "name": "rusty sword",
        "phydmg": 3,
        "mgcdmg": 0,
        "rngdmg": 0,
        "type": "sword"
    },
    {
        "name": "rusty gaunlet",
        "physdmg": 4,
        "mgcdmg": 0,
        "rngdmg": 0,
        "type": "fists"
    },
    {
        "name": "basic staff",
        "physdmg": 0,
        "mgcdmg": 5,
        "rngdmg": 3,
        "type": "staff"
    }
]
resources=[
    {
    "name": "Iron",
    "amount": 1,
    "type": "Metal",
    },
    {
    "name": "Wood",
    "amount": 1,
    "type": "Wood",
    },
    {
    "name": "Copper",
    "amount": 1,
    "type": "Metal",
    }
]

#classes: knight fighter mage

#

#I FORGOT HOW TO GET THE [CLASS] class FROM CHARACTER.PY AHHHHHHHHHH

class shop():
    def __init__(self, equipped):
        super().__init__(self)
        self.equipped=equipped
        self= shop([])
    def weaponshop(self):
        print("Buy a weapon... but choose wisely:")
        for index, i in enumerate(weapontype, start=1): 
            print(f"{index}. {i}")
        choice=int(input("type the number: "))
        #subtract the previously chosen weapon stats from character stats
        self.inv.append(weapontype[choice-1])
        self.phydmg+=weapontype[choice-1]['phydmg']
        self.rngdmg+=weapontype[choice-1]['rngdmg']
        self.mgcdmg+=weapontype[choice-1]['mgcdmg']
        print(f"Current Inventory: {self.inv}")

    def smithy(self):
        upgradecounter=0
        if self.equipped['name']==weapontype[0]['name']:
            print("if you wanna upgrade your current weapon you will need enough resources: 10 metal")
    #def genstore():



while True:
    user_input = input("x")
    if user_input== "x":
        self.weaponshop()