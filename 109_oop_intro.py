player_name = 'Alice'
player_life = 20
player_power = 2

monster_name = 'Dragon'
monster_life = 10
monster_power = 4

def attack_monster():
	global monster_life
	print('player attacks monster')
	monster_life = monster_life - player_power

def attack_player():
	global player_life
	print('monster attacks player')
	player_life = player_life - monster_power

import random
while True:
	if random.random() < 0.5:
		attack_monster()
	else:
		attack_player()
	if player_life <= 0:
		print('player dead')
		break
	elif monster_life <= 0:
		print('monster dead')
		break
