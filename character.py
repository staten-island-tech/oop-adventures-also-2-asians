
weapontype=[
    {
        "name": "rusty sword",
        "phydmg": 3,
        "mgcdmg": 0,
        "rngdmg": 0,
        "type": "sword",
        "genre": "weapon",
        "price": 40
    },
    {
        "name": "rusty gaunlet",
        "phydmg": 3,
        "mgcdmg": 0,
        "rngdmg": 0,
        "type": "fists",
        "genre": "weapon",
        "price": 40
    },
    {
        "name": "basic staff",
        "phydmg": 0,
        "mgcdmg": 3,
        "rngdmg": 0,
        "type": "staff",
        "genre": "weapon",
        "price": 40
    }
]
resources=[
    {
    "name": "Iron",
    "amount": 1,
    "type": "Metal",
    "genre": "resource"
    },
    {
    "name": "Copper",
    "amount": 1,
    "type": "Metal",
    "genre": "resource"

    },
    {
    "name": "Wood",
    "amount": 1,
    "type": "Wood",
    "genre": "resource"
    }
]

mobs = [
    {
    "name" : "bandit",
    "damage" : 4,
    "health" : 25,
    "def" : 0,
    "exp" : 10,
    "money" : 5
},
{
    "name" : "rouge",
    "damage" : 6,
    "health" : 20,
    "def" : 0,
    "exp" : 12
},
{
    "name" : "Outcast",
    "damage" : 2,
    "health" : 10,
    "def" : -1,
    "exp" : 5
},
{
    "name" : "Squire",
    "damage" : 5,
    "health" : 25,
    "def" : 2,
    "exp" : 20
},
{
    "name" : "Guard",
    "damage" : 7,
    "health" : 50,
    "def" : 3,
    "exp" : 30
},
{
    "name" : "Knight",
    "damage" : 10,
    "health" : 100,
    "def" : 5,
    "exp" : 50
},
{
    "name" : "Royal Guard",
    "damage" : 12,
    "health" : 250, 
    "def" : 7,
    "exp" : 125
}
    ]

class Class:
    def __init__(self, name, money, hp, phydmg, rngdmg, mgcdmg, mana, inv, race, classs, equipped, strength, durability, defense, expamt, exp, level, health):
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
        self.equipped = equipped
        self.strength = strength
        self.durability = durability
        self.defense = defense
        self.level = level
        self.expamt = expamt
        self.exp = exp
        self.health = health
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

    def weaponshop(self):
        print("Buy a weapon... but choose wisely:")
        for index, i in enumerate(weapontype, start=1): 
            print(f"{index}. {i}")
        choice=int(input("type the #: "))
        #subtract the previously chosen weapon stats from character stats
        self.inv.append(weapontype[choice-1])
        
        print(f"Current Inventory: {self.inv}")
    
    def equipping(self):
        #Switching Equipped Weapon(SEW)
        print("Which weapon do you wanna equip?")
        for index, i in enumerate(self.inv, start=1): 
            if i['genre'] == "weapon":
                print(f"{index}. {i['name']}")
        choice=input("type the name: ").lower()
            #ayaan proof this later
            #for y in range(len(self.inv)):
        
        if any(choice == i['name'] for i in self.equipped):
            print("you have already equipped that")
            self.equipping()
            return
        if not any(choice == i['name'] for i in self.inv):
            print("That is not a item you currently have")
            self.equipping()
            return

        for x in weapontype:
            if choice==x['name'] and x['genre']=="weapon":
                if len(self.equipped) == 1:
                    self.phydmg - x['phydmg']
                    self.rngdmg-x['rngdmg']
                    self.mgcdmg-x['mgcdmg']
                    self.equipped.pop(0)
                self.equipped.append(x)
                self.phydmg + x['phydmg']
                self.rngdmg+x['rngdmg']
                self.mgcdmg+x['mgcdmg']
                print(self.phydmg,self.rngdmg,self.mgcdmg)
        print(f"currently equipped: {self.equipped}")

    def smithy(self):
        upgradecounter=0
        if self.equipped['name']==weapontype[0]['name']:
            print(f"if you wanna upgrade your current weapon you will need enough resources: {10} {resources[0]['name']}")
        if self.equipped['name']==weapontype[1]['name']:
            print(f"if you wanna upgrade your current weapon you will need enough resources: {10} {resources[1]['name']}")
        if self.equipped['name']==weapontype[2]['name']:
            print(f"if you wanna upgrade your current weapon you will need enough resources: {10} {resources[2]['name']}")
    #def genstore():

    def killfunc(self):
        for index, i in enumerate(mobs):
            print(f"{index}. {i}")
        userinput = input("What mob would you like to fight? Please type its number via list!")
        x = int(userinput)
        userinput = input(f"Would you like to fight the {mobs[x]['name']}?")
        if userinput == "yes":
            charhealth = int(self.health)
            chardef = int(self.defense)
            enemyhealth = int(mobs[x]['health'])
            enemymoney = int(mobs[x]['money'])
            enemyexp = int(mobs[x]['exp'])
            enemydmg = int(mobs[x]['damage'])
            enemydef = int(mobs[x]["def"])
            while True:
                userinput = input("Please choose an option: Attack, Inventory, Flee")
                if enemyhealth <= 0:
                    self.money += enemymoney
                    self.exp += enemyexp
                    return f"Well done! The {mobs[x]['name']} has been defeated! You have been rewarded with {enemyexp} and {enemymoney}"
                elif charhealth <= 0:
                    return f"The enemy has defeated you! Health remaining: {enemyhealth}"
                elif userinput == "Attack".lower() and self.classs == ["Warrior"]:
                    xwar = self.phydmg * ((self.strength * 0.1) + 1)
                    enemyhealth -= xwar - enemydef
                    print(f"You landed a blow on the enemy! You dealt {xwar} damage! Enemy health: {enemyhealth}")
                    print("----------------------------------")
                    charhealth -= enemydmg - chardef
                    print(f"{mobs[x]['name']} has attacked! Character health: {charhealth}")
                elif userinput == "Attack".lower() and self.classs == ["Archer"]:
                    xrang = self.rngdmg * ((self.strength * 0.1) + 1)
                    enemyhealth -= xrang - enemydef
                    print(f"You landed a blow on the enemy! You dealt {xrang} damage! Enemy health: {enemyhealth}")
                    print("----------------------------------")
                    charhealth -= enemydmg - chardef
                    print(f"{mobs[x]['name']} has attacked! Character health: {charhealth}")
                elif userinput == "Attack".lower() and self.classs == ["Mage"]:
                    xmag = self.mgcdmg * ((self.mana * 0.1) + 1)
                    enemyhealth -= xmag - enemydef
                    print(f"You landed a blow on the enemy! You dealt {xmag} damage! Enemy health: {enemyhealth}")
                    print("----------------------------------")
                    charhealth -= enemydmg - chardef
                    print(f"{mobs[x]['name']} has attacked! Character health: {charhealth}")
                else:
                    print("Input not indentified, please try again.")

    def levelsystem(self):
        if self.exp >= self.expamt:
            level += 1
            self.exp -= self.expamt
            self.expamt * 1.1
            user_input = input("You have met the level requirements! Where would you like to put your stat points?")
            if user_input.lower() == "strength":
                self.strength += 1
            elif user_input.lower() == "defense":
                self.defense += 1
            elif user_input.lower() == "durability":
                self.durability += 1
            elif user_input.lower() == "mana":
                self.mana += 1
        else:
            print(f"Exp requirement not met: You need {self.expamt} total exp!")

self = Class("John", 1, 1, 1, 0, 0, 0, [], [], [], [], 0, 0, 0, 1, 100, 0, 100)



while True:
    user_input = input("Please choose a race!: Human, Demon, Angel, Dwarf - Remember you will not be able to change these later on. Keep in mind each race will have their own buffs/debuffs. If you would like to get info about these races, please type 'info' ").lower()
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

print("Welcome to the game! Please type 'info' for a introduction to the game. Otherwise, enjoy!")
while True:
    user_input = input("What would you like to do? (Shop, Attack, Leveling, Equip, Stats)")
    if user_input.lower() == "shop":
        self.weaponshop()
    elif user_input.lower() == "attack":
        self.killfunc()
    elif user_input.lower() == "leveling":
        self.levelsystem()
    elif user_input.lower() == "equip":
        self.equipping()
    elif user_input.lower() == "stats":
        self.stats()
    else:
        print("unknown command, try again")



                

#_________________________________________________________________________________________
""" while True:
    user_input = input("x")
    if user_input== "x":
        self.weaponshop()
        self.equipping() """

#using this(below) to help
# Word Problem: The School Portal Login System
# Your school is creating a new online portal for students to sign up for accounts. The login system needs a function that accepts two pieces of information from the user:
# Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.


""" def isvalid(email, paswor):
    if not isinstance(email,str) or not isinstance(paswor,str):
        return "the email and password is not valid, must be string"
    if "@" not in email:
        return "Not valid email, nust have @ symbol"
    if len(paswor)<8:
        return "your password must be at least eight characters long"
    if not any(i.isdigit() for i in paswor):
        return "your password must have a number"
    if not any(i.isupper() for i in paswor):
        return "your password must have a uppercase letter"


    
    return {"email":email, "password":paswor}
print(isvalid("test123@gamer.com","F2d8layf")) """