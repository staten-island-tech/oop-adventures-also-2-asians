#NZ - B

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

class Levels:
     def levelsystem(self):
        level = 1
        if self.exp >= self.expamt:
            level += 1
            self.exp -= self.expamt
            self.expamt * 1.1
        else:
            print(f"Exp requirement not met: You need {self.expamt} total exp!")

def killfunc(self):
    for index, i in enumerate(mobs):
        print(f"{index}. {i}")
    userinput = input("What mob would you like to fight? Please type its number via list!")
    x = int(userinput)
    print(f"Would you like to fight the {mobs[x]['name']}?")
    if userinput == "yes":
        charhealth = int(self.health)
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
            elif userinput == "Attack".lower() and classs == ["Warrior"]:
                xwar = self.phydmg * self.strength
                enemyhealth -= xwar - enemydef
                print(f"You landed a blow on the enemy! You dealt {xwar} damage! Enemy health: {enemyhealth}")
                charhealth -= enemydmg
                print(f"{mobs[x]['name']} has attacked! Character health: {charhealth}")
            elif userinput == "Attack".lower() and classs == ["Archer"]:
                xrang = self.rngdmg * self.strength
                enemyhealth -= xrang - enemydef
                print(f"You landed a blow on the enemy! You dealt {xrang} damage! Enemy health: {enemyhealth}")
                charhealth -= enemydmg
                print(f"{mobs[x]['name']} has attacked! Character health: {charhealth}")
            elif userinput == "Attack".lower() and classs == ["Mage"]:
                xmag = self.mgcdmg * self.mana
                enemyhealth -= xmag - enemydef
                print(f"You landed a blow on the enemy! You dealt {xmag} damage! Enemy health: {enemyhealth}")
                charhealth -= enemydmg
                print(f"{mobs[x]['name']} has attacked! Character health: {charhealth}")
            else:
                print("Input not indentified, please try again.")
                


    """ if userinput == "0":
        self.fbandit()

def fbandit(self):
    print("You've encountered a bandit!")
    bhealth = int(mobs[0]["health"])
    bmoney = int(mobs[0]["money"])
    bexp = int(mobs[0]["exp"])
    userinput = input("Please choose an option: Attack, Inventory, Flee")
    while True:
        if bhealth <= 0:
            self.money += bmoney
            self.exp += bexp
            return f"You defeated the bandit! Rewarded "
        if userinput == "Attack".lower() and classs == ["Warrior"]:
            x = self.phydmg * self.strength
            bhealth -= x 
        elif userinput == "Attack".lower() and classs == ["Mage"]:
            y = self.mgcdmg * self.mana
        elif userinput == "Attack".lower() and classs == ["Archer"]:
            z = self.rngdmg * self.strength """