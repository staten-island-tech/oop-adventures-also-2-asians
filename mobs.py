mobs = [
    {
    "name" : "bandit",
    "damage" : 4,
    "health" : 25,
    "def" : 0,
    "exp" : 10
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
