import random
import time

import player0
import monster0
player_1 = player0.Player()
monster_1 = monster0.Monster()
# from player0 import Player
# from monster0 import Monster
# player_1 = Player()
# monster_1 = Monster()

while True:
	r = random.random()
	if r < 1/2:
		print('Monster attacks Player')
		monster_1.attack_player(player_1)
	else:
		print('Player attacks Monster')
		player_1.attack_monster(monster_1)

	print('Life: {}, {}'.format(player_1.get_life(),
								monster_1.get_life()))

	if not player_1.is_alive():
		print('Player dead')
		break
	elif not monster_1.is_alive():
		print('Monster dead')
		break

	time.sleep(0.5)
