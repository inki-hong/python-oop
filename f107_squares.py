f = open('squares.txt', mode='wt', encoding='UTF-8')

f.write('Number, Squared\n')

for i in range(1, 11):
	f.write('{}, {}\n'.format(i, i * i))

f.close()
