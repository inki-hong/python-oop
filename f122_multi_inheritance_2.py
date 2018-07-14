class Grandparent():
	def speak(self):
		print('Anything')

class Father(Grandparent):
	pass

class Mother(Grandparent):
	def speak(self):
		print('Burger King')

class ChildOne(Father, Mother):
	pass

class ChildTwo(Mother, Father):
	pass




if __name__ == '__main__':
	child_one = ChildOne()
	child_one.speak()

	child_two = ChildTwo()
	child_two.speak()










#
