class Player():
	power = 2

	def __init__(self):
		self.life = 20

	def __str__(self):
		return ('{}, power {}, life {}'.format(
					self.__class__.__name__, self.power, self.life
				))

	def get_life(self):
		return self.life

	def increase_life(self, recovery):
		self.life += recovery

	def decrease_life(self, damage):
		self.life -= damage

	def is_alive(self):
		return self.life > 0

	def attack_monster(self, monster):
		monster.decrease_life(self.power)

	def heal(self):
		self.increase_life(self.power)


if __name__ == '__main__':
	player_1 = Player()
	print(player_1)
