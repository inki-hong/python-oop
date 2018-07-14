f = open('some_text.txt',
	     encoding='UTF-8',
	     mode='rt')

s = f.read()

print(s)

f.close()

print('-' * 40)










f = open('some_text.txt',
	     encoding='UTF-8',
	     mode='rt')

no = 1
for line in f:
	print(no, line, end='')
	no += 1

f.close()

print('-' * 40)






import datetime

f = open('profile.txt', encoding='UTF-8')

line_no = 1
for line in f:
	if line_no == 1:
		print('Name: {}'.format(line), end='')
	elif line_no == 2:
		print('Place of birth: {}'.format(line), end='')
	elif line_no == 3:
		if line[-1] == '\n':
			line = line[:-1]
		dt = datetime.datetime.strptime(line, '%Y/%m/%d')
		fmt = dt.strftime('%B %d, %Y')
		print('Date of birth: {}'.format(fmt), end='')
	line_no += 1
print()

f.close()
#
