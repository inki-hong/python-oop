class Parent():
	common = 'parent class attribute'

	def __init__(self):
		self.parent_data = 'parent instance attribute'

	def get_name(self):
		return 'parent class'


class Child(Parent):
	def __init__(self):
		Parent.__init__(self)
		self.child_data = 'child instance attribute'






c = Child()
print(Child.common)
print(c.parent_data)
print(c.child_data)
print(c.get_name())
print(Child.get_name(c))
print(isinstance(c, Child))
print(isinstance(c, Parent))
