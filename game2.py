import random

class Player():
    def __init__(self):
        self.name = 'Alice'
        self.life = 20
        self.power = 2

    def attack_monster(self, monster, option=1):
        if option == 1:
            monster.life = monster.life - self.power
        elif option == 2:
            if random.random() < 0.5:
                monster.life = monster.life - self.power * 2

    def heal(self):
        if random.random() < 0.8:
            self.life = self.life + self.power * 3


################################################################################


class Monster():
    def __init__(self):
        self.name = 'Dragon'
        self.life = 10
        self.power = 4

    def attack_player(self, player):
        player.life = player.life - self.power


################################################################################


alice = Player()
dragon = Monster()
print('player', alice.life, 'monster', dragon.life)

while True:
    ########################################
    # Monster turn
    #

    print('monster attacks player')
    dragon.attack_player(alice)
    print('player', alice.life, 'monster', dragon.life)

    ########################################
    # Player turn
    #

    action = input('액션을 입력하세요 (1, 2, 3): ')
    if action == '1':
        print('player attacks monster')
        alice.attack_monster(dragon)
    elif action == '2':
        print('player attacks monster with option 2')
        alice.attack_monster(dragon, option=2)
    else:
        print('player heals')
        alice.heal()
    print('player', alice.life, 'monster', dragon.life)

    ########################################
    # End of turn
    #

    if alice.life <= 0:
        print('player dead')
        break
    elif dragon.life <= 0:
        print('monster dead')
        break
#
