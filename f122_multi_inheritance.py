class Grandparent():
	def __init__(self):
		self.car = 'Great car'

class Father(Grandparent):
	def __init__(self):
		super().__init__()
		self.house = 'Big house'

class Mother(Grandparent):
	def __init__(self):
		super().__init__()
		self.land = 'Big land'

class ChildOne(Father, Mother):
	pass

class ChildTwo(Mother, Father):
	pass



if __name__ == '__main__':
	one = ChildOne()
	print(one.house, one.car)

	two = ChildTwo()
	print(two.land, two.car)

	print(one.car, one.house, one.land)
	print(two.car, two.house, two.land)







#
