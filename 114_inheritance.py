class A():
	attr_a = 'A attr'

	def __init__(self):
		self.iattr_a = 'A instance attr'

	def get_name(self):
		return 'Class A'

class B(A):
	def __init__(self):
		A.__init__(self)
		self.iattr_b = 'B instance attr'

b = B()
print(b.iattr_a)
print(b.iattr_b)
print(b.get_name())
print(B.get_name(b))
print(isinstance(b, B))
print(isinstance(b, A))
