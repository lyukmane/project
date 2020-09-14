from random import random


class Warrior:
    health = 100
    power = 1
    dexterity = 1

    def hit(self, h):
        self.health = self.health - h

    def checkHealth(self):
        if self.health > 0:
            return 'heath is {}'.format(self.health)
        else:
            return 'is dead'

    def set_atrb(self):
        self.power += 1


warrior_1 = Warrior()
warrior_2 = Warrior()
i = 1
while warrior_1.health > 0 and warrior_2.health > 0:
    print('Round', i)
    if random() < 0.5:
        warrior_1.hit(20)
        print('warrior_2 hits warrior_1')
        i += 1
    else:
        warrior_2.hit(20)
        print('warrior_1 hits warrior_2')
        i += 1

    print('warrior_1 -', warrior_1.checkHealth(), 'warrior_2 -', warrior_2.checkHealth())

if warrior_1.health > 0:
    print('\nwarrior_1 wins')
    warrior_1.set_atrb()
    print(warrior_1.power)
elif warrior_2.health > 0:
    print('\nwarrior_2 wins')
    warrior_2.set_atrb()
    print(warrior_2.power)

else:
    print('Friendship is a winner')
