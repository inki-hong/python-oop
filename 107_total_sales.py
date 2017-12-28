sales = int(input('How many did you sell today? '))

try:
	f = open('sales.txt',
		     encoding='UTF-8',
		     mode='r')
except FileNotFoundError:
	current_total = 0
else:
	s = f.read()
	if s == '':
		current_total = 0
	else:
		current_total = int(s)
	f.close()

f = open('sales.txt',
		 encoding='UTF-8',
		 mode='w')
new_total = current_total + sales
f.write(str(new_total))
f.close()

print('Your total sales is {} units.'.format(new_total))
