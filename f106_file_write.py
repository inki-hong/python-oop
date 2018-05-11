f = open('record.txt',
	     encoding='UTF-8',
	     mode='wt')

f.write('name, gender, age\n')

name = 'Alice'
gender = 'F'
age = 15
f.write('{}, {}, {}\n'.format(name, gender, age))

name = 'Bob'
gender = 'M'
age = 14
f.write('{}, {}, {}\n'.format(name, gender, age))

f.close()



import random

try:
	f = open('read_write.txt', encoding='UTF-8', mode='r')
except FileNotFoundError:
	old_content = '(empty)'
else:
	old_content = f.read()
	f.close()

print('Old content is {}'.format(old_content))

f = open('read_write.txt', encoding='UTF-8', mode='w')
new_content = str(random.random())
f.write(new_content)
f.close()

print('New content is {}'.format(new_content))
