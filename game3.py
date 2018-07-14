import random

class Player():
    def __init__(self, name, life, power):
        self.name = name
        self.life = life
        self.power = power

    def __str__(self):
        return '{} {} life {} power {}'.format(
            self.__class__.__name__, self.name, self.life, self.power
        )

    def attack_monster(self, monster):
        monster.life = monster.life - self.power

################################################################################

class Warrior(Player):
    def attack_monster(self, monster, option=1):
        if option == 1:
            Player.attack_monster(self, monster)
        elif option == 2:
            if random.random() < 0.5:
                print('Critical attack')
                monster.life = monster.life - self.power * 2
            else:
                print('Attack miss')

################################################################################

class Wizard(Player):
    def __init__(self, name, life, power, magic):
        Player.__init__(self, name, life, power)
        self.magic = magic

    def __str__(self):
        s = Player.__str__(self)
        return s + ' magic {}'.format(self.magic)

    def heal(self):
        if random.random() < 0.8:
            print('Heal')
            self.life = self.life + self.magic * 3
        else:
            print('Heal fail')

################################################################################

class Monster():
    def __init__(self, name, life, power):
        self.name = name
        self.life = life
        self.power = power

    def __str__(self):
        return '{} {} life {} power {}'.format(
            self.__class__.__name__, self.name, self.life, self.power
        )

    def attack_player(self, player):
        player.life = player.life - self.power

################################################################################

class Slime(Monster):
    def __init__(self, name, life, power, magic):
        Monster.__init__(self, name, life, power)
        self.magic = magic

    def __str__(self):
        s = Player.__str__(self)
        return s + ' magic {}'.format(self.magic)

    def heal(self):
        if random.random() < 0.8:
            print('Heal')
            self.life = self.life + self.magic * 3
        else:
            print('Heal fail')

################################################################################

class Dragon(Monster):
    def attack_player(self, player, option=1):
        if option == 1:
            Monster.attack_player(self, player)
        elif option == 2:
            if random.random() < 0.2:
                print('Fire')
                player.life = 0
            else:
                print('Fire miss')

################################################################################

chris = Warrior('Chris', 20, 2)
david = Wizard('David', 10, 1, 3)
print(chris)
print(david)

monster_1 = Slime('Monster 1', 10, 1, 3)
monster_2 = Dragon('Monster 2', 10, 4)
print(monster_1)
print(monster_2)

print('Chris', chris.life, 'David', david.life)
print('Monster 1', monster_1.life, 'Monster 2', monster_2.life)

################################################################################
