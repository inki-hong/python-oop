import random

class Player():
	power = 2

	def __init__(self, target=None):
		self.life = 10
		self.target = target

	def __str__(self):
		return ('{}, power {}, life {}'.format(self.__class__.__name__, self.power, self.life))

	def get_life(self):
		return self.life

	def set_target(self, target):
		self.target = target

	def increase_life(self, recovery):
		self.life += recovery

	def decrease_life(self, damage):
		self.life -= damage

	def is_alive(self):
		return self.life > 0

	def perform_action(self):
		print('Default: do nothing')


class Infantry(Player):
	def perform_action(self):
		print('{} attacks monster'.format(self.__class__.__name__))
		self.attack_monster(self.target)

	def attack_monster(self, monster):
		monster.decrease_life(self.power)


class Cavalry(Player):
	power = 4

	def __init__(self):
		self.life = 8

	def perform_action(self):
		print('{} attacks monster'.format(self.__class__.__name__))
		self.attack_monster(self.target)

	def attack_monster(self, monster):
		monster.decrease_life(self.power)


class Wizard(Player):
	def perform_action(self):
		r = random.random()
		if r < 1/2:
			print('{} heals {}'.format(self.__class__.__name__,
										self.target[0].__class__.__name__))
			self.heal_player(self.target[0])
		else:
			print('{} heals {}'.format(self.__class__.__name__,
										self.target[1].__class__.__name__))
			self.heal_player(self.target[1])

	def heal_player(self, player):
		# player.life += self.power  # not recommended
		player.increase_life(self.power)


class HealerMixIn():
	def heal_player(self, player):
		player.increase_life(self.power)


class Farmer(Player, HealerMixIn):
	def perform_action(self):
		print('{} heals wizard'.format(self.__class__.__name__))
		self.heal_player(self.target)
