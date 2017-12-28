class Grandparent():
	def __init__(self):
		self.speak()

	def speak(self):
		print('Anything')


class Father(Grandparent):
	def __init__(self):
		self.common_data = 1

	def get_paternal_data(self):
		return self._paternal_data

	def set_paternal_data(self, data):
		self._paternal_data = data

	def speak(self):
		Grandparent.speak(self)
		print('McDonalds')


class Mother(Grandparent):
	def __init__(self):
		self.common_data = 22

	def get_maternal_data(self):
		return self._maternal_data

	def set_maternal_data(self, data):
		self._maternal_data = data

	def speak(self):
		Grandparent.speak(self)
		print('Burger King')

class Child(Father, Mother):
	def __init__(self):
		Father.__init__(self)
		temp = self.common_data
		Mother.__init__(self)
		temp += self.common_data
		self.common_data = temp

		self.speak()

	def speak(self):
		# Grandparent.speak(self)  # bad design
		Mother.speak(self)
		Father.speak(self)
		print('Wendy\'s')

child = Child()
child.set_paternal_data('qwerty')
# print(child.get_paternal_data())
child.set_maternal_data('dvorak')
# print(child.get_maternal_data())
# child.speak()
# print(child.common_data)
