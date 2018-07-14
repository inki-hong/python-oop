class Grandparent():
	def __init__(self):
		self.car = 'Great car'

class Father(Grandparent):
	def __init__(self):
		self.house = 'Big house'

class Mother(Grandparent):
	def __init__(self):
		self.land = 'Big land'

class ChildOne(Father, Mother):
	pass

class ChildTwo(Mother, Father):
	pass



if __name__ == '__main__':
	one = ChildOne()
	print(one.house)

	two = ChildTwo()
	print(two.land)

	print(one.car, one.house, one.land)
	print(two.car, two.house, two.land)







#
