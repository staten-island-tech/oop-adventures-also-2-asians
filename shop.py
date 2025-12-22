weapontype=[
    {
        "name": "rusty sword",
        "physdmg": 3,
        "type": "sword"
    },
    {
        "name": "rusty gaunlet",
        "physdmg": 4,
        "type": "fists"
    },
    {
        "name": "basic staff",
        "physdmg": 1,
        "magidmg": 5,
        "type": "staff"
    }
]
testinv=[]
#classes: knight fighter mage

class shop:
    def weaponshop(inv):
        print("Buy a weapon... but choose wisely:")
        for index, i in enumerate(weapontype, start=1):
            print(f"{index}. {i}")
        choice=int(input("type the number: "))
        testinv.append(weapontype[choice-1])
        print(f"Current Inventory: {testinv}")
    weaponshop(testinv)

    def smithy(inv):
        if self.inv:
        print("if you wanna upgrade your current weapon you will need ")
