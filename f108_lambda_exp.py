def square(x):
	return x**2

a = square(2)
print(a)

f = lambda x: x**2

b = f(2)
print(b)












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
