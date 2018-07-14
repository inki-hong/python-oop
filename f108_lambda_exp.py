def square(x):
	return x**2

a = square(2)
print(a)

square = lambda x: x**2

b = square(2)
print(b)

print('-' * 40)


numbers = [1, 2, 3, 4, 5]
# sq = map(square, numbers)
sq = map(lambda x: x ** 2, numbers)
print(list(sq))
print('-' * 40)
















####################


def expo(e):
	def wrapped(x):
		return x**e
	return wrapped

f = expo(3)
g = expo(4)
print(f(2))
print(g(2))


def expo_v2(e):
	return lambda x: x**e

f2 = expo_v2(3)
g2 = expo_v2(4)
print(f2(2))
print(g2(2))
#
