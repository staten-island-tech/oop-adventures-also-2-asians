mobs = [
    {
    "name" : "bandit",
    "damage" : 4,
    "health" : 25,
    "def" : 0
},
{
    "name" : "rouge",
    "damage" : 6,
    "health" : 20,
    "def" : 0
},
{
    "name" : "Outcast",
    "damage" : 2,
    "health" : 10,
    "def" : -1
}
    ]

class Levels():
     def levelsystem(self, exp):
        self.exp = exp
        level = 1
        expamt = 100
        if self.exp >= expamt:
            level += 1
            exp -= expamt
            expamt * 1.1
        else:
            print(f"Exp requirement not met: You need {expamt} total exp!")