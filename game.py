import random
import time

import player
from monster import Monster

monster_1 = Monster()

player_1 = player.Infantry()
player_2 = player.Cavalry()
player_3 = player.Wizard()
player_4 = player.Farmer()

player_1.set_target(monster_1)
player_2.set_target(monster_1)
player_3.set_target([player_1, player_2])
player_4.set_target(player_3)

while True:
	for p in [player_1, player_2, player_3, player_4]:
		p.perform_action()

	r = random.random()
	if r < 1/3:
		print('Monster attacks Infantry')
		monster_1.attack_player(player_1)
	elif 1/3 < r < 2/3:
		print('Monster attacks Cavalry')
		monster_1.attack_player(player_2)
	else:
		print('Monster attacks Wizard')
		monster_1.attack_player(player_3)
	
	print('Life: {}, {}, {}, {}'.format(player_1.get_life(),
										player_2.get_life(),
										player_3.get_life(),
										monster_1.get_life()))

	if not player_1.is_alive() and not player_2.is_alive() and not player_3.is_alive():
		print('All players dead')
		break
	elif not monster_1.is_alive():
		print('Monster dead')
		break

	time.sleep(0.5)
