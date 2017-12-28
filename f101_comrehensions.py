my_list = []
for x in range(1, 11):
	my_list.append(x ** 2)
print(my_list)

my_list = [x ** 2 for x in range(1, 11)]
print(my_list)

my_list = [x ** 3
           for x in range(1, 11)
           if x % 2 == 0]
print(my_list)

_2nd_list = [x % 3 for x in my_list]
print(_2nd_list)

falses = [False for x in range(5)]
print(falses)

print('-' * 40)
####################################


import random

randoms = [round(random.random(), 3)
           for _ in range(5)]
print(randoms)

print('-' * 40)
####################################


# 2-dimensional (nested) list comprehension

my_list = []
for x in range(3):
	for y in range(4):
		my_list.append( (x, y) )  # tuple
print(my_list)

my_list = [(x, y)
		   for x in range(3)
		   for y in range(4)]
print(my_list)

print('-' * 40)
####################################


my_list = [(x, y)
           for x in range(5)
           for y in range(5)
           if x != 0 and y != 0 and
           ((x + y) % 2 == 0)]
print(my_list)
print('-' * 40)
####################################


my_str = 'applejuice'
my_list = [c.upper()
		   for c in my_str
           if c in ('a','e','i','o','u')]
my_str = ''.join(my_list)
print(my_str)
print('-' * 40)
####################################


my_list = [x % 5 for x in range(10)]
print(my_list)

my_set = {x % 5 for x in range(10)}
print(my_set)

my_dict = {str(n): n ** 2
           for n in range(6)}
print(my_dict)

my_tuple = tuple(x % 5 for x in range(10))
print(my_tuple)

g = (x % 5 for x in range(10))  # generator expression
print(g)

print('-' * 40)
####################################


el = []
for xx in range(10):
  el.append(xx)
print(xx)

el = [yy for yy in range(10)]
# print(yy)  # not in scope

print('-' * 40)
####################################

# exercise and ternary operator

my_list = []
for c in 'applejuice':
  if c in ('a', 'e', 'i', 'o', 'u'):
    my_list.append(c.upper())
  else:
    my_list.append(c)
print(''.join(my_list))

my_list = [c.upper() if c in ('a', 'e', 'i', 'o', 'u') else c
           for c in 'applejuice']
print(''.join(my_list))
