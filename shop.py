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
testinv=[]
#classes: knight fighter mage

class shop(Class):
    def __init__(self, name, money, hp, phydmg, rngdmg, mgcdmg, mana, inv, race, classs):
        super().__init__(self, name, money, hp, phydmg, rngdmg, mgcdmg, mana, inv, race, classs)
    def weaponshop(self):
        print("Buy a weapon... but choose wisely:")
        for index, i in enumerate(weapontype, start=1):
            print(f"{index}. {i}")
        choice=int(input("type the number: "))
        testinv.append(weapontype[choice-1])
        self.phydmg+=weapontype[choice-1]['phydmg']
        self.rngdmg+=weapontype[choice-1]['rngdmg']
        self.mgcdmg+=weapontype[choice-1]['mgcdmg']
        print(f"Current Inventory: {testinv}")
    

    def smithy(inv):
        startingweapon=inv[1]
        print("if you wanna upgrade your current weapon you will need ")
