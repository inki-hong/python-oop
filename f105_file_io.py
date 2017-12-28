f = open('some_text.txt',
	     encoding='UTF-8',
	     mode='rt')

s = f.read()
print(s)

# for line in f:
# 	print(line, end='')

f.close()

print('-' * 40)
########################################
import datetime

f = open('profile.txt')

line_no = 1
for line in f:
	if line_no == 1:
		print('Name: {}'.format(line), end='')
	elif line_no == 2:
		print('Gender: {}'.format(line), end='')
	elif line_no == 3:
		if line[-1] == '\n':
			line = line[:-1]
		dt = datetime.datetime.strptime(line, '%Y-%m-%d')
		fmt = dt.strftime('%B, %d %Y')
		print('DOB: {}'.format(fmt), end='')
	line_no += 1
print()

f.close()
#
