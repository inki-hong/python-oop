import random
print(random)
print(type(random))
print(random.random())
print('-' * 40)

















import lib_module
# import lib_module
print('-' * 40)









print(lib_module.a)
print(lib_module.b)
print(lib_module.pi())
print(lib_module.my_list[0])
print(lib_module.d)
# print(lib_module.c)
print('-' * 40)













# print(lib_module.__dict__)
for attr in lib_module.__dict__:
    print(attr)
print('-' * 40)


















from lib_module import a, b
print(a)
# print(lib_module.b)
print(b)

from random import randrange
print(randrange(10))

from random import randrange as rr
print(rr(10))
print('-' * 40)









import lib_module

print(lib_module)
# lib_module = 'abc'
# print(lib_module)
print('-' * 40)

print(lib_module.a)
lib_module.a = 200
print(lib_module.a)
lib_module.aaa = 1000
print(lib_module.aaa)
print('-' * 40)







# print(lib_module.__dict__)
print(dir(lib_module))
print('-' * 40)

import random
print(dir(random))
print('-' * 40)

import builtins
print(dir(builtins))








#
