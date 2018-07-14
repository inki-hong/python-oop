player_name = 'Alice'
player_life = 20
player_power = 2

monster_name = 'Dragon'
monster_life = 10
monster_power = 4

def attack_monster(monster_life):
	print('player attacks monster')
	new_monster_life = monster_life - player_power
	return new_monster_life

def attack_player(player_life):
	print('monster attacks player')
	new_player_life = player_life - monster_power
	return new_player_life



import random
while True:
	if random.random() < 0.5:
		monster_life = attack_monster(monster_life)
	else:
		player_life = attack_player(player_life)

	if player_life <= 0:
		print('player dead')
		break
	elif monster_life <= 0:
		print('monster dead')
		break



#
