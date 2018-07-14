class Parent():
	common = 'Common Data'

	def __init__(self):
		self.parent_data = 'Parent Data'

	def get_name(self):
		return 'Parent Class'


class Child(Parent):
	def __init__(self):
		Parent.__init__(self)
		self.child_data = 'Child Data'






c = Child()
print(Child.common)
print(c.parent_data)
print(c.child_data)
print(c.get_name())
print(Child.get_name(c))
print(isinstance(c, Child))
print(isinstance(c, Parent))








#
