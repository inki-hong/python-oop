player_name = 'Alex'
player_life = 10
player_power = 2

monster_type = 'Dragon'
monster_life = 100
monster_power = 5

monster_2_type = 'Orc'
monster_2_life = 50
monster_2_power = 3

def attack_dragon():
	global player_life
	print('attack dragon')
	player_life -= monster_power

def attack_orc():
	pass

def attack_player():
	global monster_life
	print('attack player')
	monster_life -= player_power

import random
while True:
	if random.random() < 0.5:
		attack_dragon()
	else:
		attack_player()
	if player_life <= 0:
		print('player dead')
		break
	elif monster_life <= 0:
		print('monster dead')
		break
