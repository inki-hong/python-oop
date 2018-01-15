import random
import time

import player1
import monster1
player_1 = player1.Player()
monster_1 = monster1.Monster()
# from player0 import Player
# from monster0 import Monster
# player_1 = Player()
# monster_1 = Monster()

while True:
	r = random.random()
	if r < 1/4:
		print('Monster attacks Player')
		monster_1.attack_player(player_1)
	elif 1/4 <= r < 1/2:  # elif 1/4 <= r and r < 1/2:
		print('Player attacks Monster')
		player_1.attack_monster(monster_1)
	elif 1/2 <= r < 3/4:
		print('Monster heals')
		monster_1.heal()
	else:
		print('Player heals')
		player_1.heal()

	print('Life: {}, {}'.format(player_1.get_life(),
								monster_1.get_life()))

	if not player_1.is_alive():
		print('Player dead')
		break
	elif not monster_1.is_alive():
		print('Monster dead')
		break

	time.sleep(0.5)
