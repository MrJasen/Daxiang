from random import randint
class Die():
    def __init__(self):
        self.sides = 6#这里的给了sides默认值不影响后面的赋值啊
    def roll_die(self):
        x = randint(1, 6)
        self.sides = x
        print(self.sides)
    def roll_die10(self):
        x = randint(1, 10)
        self.sides = x
        print(self.sides)
    def roll_die20(self):
        self.sides = randint(1, 20)
        print(self.sides)

die = Die()
print("----------6  sides-------------")
for i in range(10):
    die.roll_die()
print("----------10 sides-------------")
for i in range(10):
    die.roll_die10()
print("----------20 sides-------------")
for i in range(10):
    die.roll_die20()