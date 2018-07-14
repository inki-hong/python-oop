class Grandparent():
	def __init__(self):
		self.car = 'Great car'

class Parent(Grandparent):
	def __init__(self):
		Grandparent.__init__(self)
		self.house = 'Big house'
		self.land = 'Big land'

class FoodMixIn():
	def food(self):
		print('McDonalds')

class ChildOne(Parent, FoodMixIn):
	pass

class ChildTwo(Parent, FoodMixIn):
	pass



if __name__ == '__main__':
	one = ChildOne()
	print(one.house, one.car)

	two = ChildTwo()
	print(two.land, two.car)

	print(one.car, one.house, one.land)
	print(two.car, two.house, two.land)

	one.food()
	two.food()




#
