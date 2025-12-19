class Class:
    def __init__(self, money, hp, phydmg, inv, race):
        self.money = money
        self.hp = hp
        self.phydmg = phydmg
        self.inv = inv
        self.race = race
John = Class(1, 1, 1, [""], [""])

class Races(Class):
    def human(self):
        self.money += 24
        self.hp += 99
        self.phydmg += 1
        self.race.append("Human")
    def mage(self):
        self.money += 24
        self.hp = 99
        self.race.append("Mage")
    def demon(self):
        self.money += 9
        self.hp += 74
        self.phydmg += 3
        self.race.append("Demon")
    userinput = input("X")
    if userinput == "Human":
        John.human()