class Monster():
	power = 5

	def __init__(self):
		self.life = 20

	def __str__(self):
		return ('Monster, '
				'power {}, '
				'life {}'.format(Monster.power,
								 self.life))

	def get_life(self):
		return self.life

	def decrease_life(self, damage):
		self.life -= damage

	def is_alive(self):
		return self.life > 0

	def attack_player(self, player):
		player.decrease_life(self.power)

if __name__ == '__main__':
	monster_1 = Monster()
	print(monster_1)
