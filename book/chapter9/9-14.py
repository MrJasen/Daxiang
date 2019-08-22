from random import randint


# x=randint(1,6)
# print(x)
class Die():
    def __init__(self):
        self.sides = 6

    def roll_die6(self):
        x = randint(1, self.sides)
        print(x)

    def roll_die10(self):
        x = randint(1, 10)
        print(x)


die = Die()
# 6面的仍10次
for i in range(10):
    die.roll_die6()
print('----------------------------')

for i in range(10):
    die.roll_die10()
