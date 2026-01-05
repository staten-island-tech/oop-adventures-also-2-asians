from character import Class

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


#I FORGOT HOW TO GET THE [CLASS] class FROM CHARACTER.PY AHHHHHHHHHH

class shop(Class):
    def __init__(self, name, money, hp, phydmg, rngdmg, mgcdmg, mana, inv, race, classs, equipped):
        super().__init__(self, name, money, hp, phydmg, rngdmg, mgcdmg, mana, inv, race, classs)
        self.equipped=equipped
    invlist=[]
    currentequip=[]
    def weaponshop(self):
        self.inv=invlist
        self.equipped=currentequip
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
    

    def smithy(inv):
        startingweapon=
        print("if you wanna upgrade your current weapon you will need ")
