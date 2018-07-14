class Sedan():
	def __init__(self, owner='Unknown', mileage=0):
		self.owner = owner
		self.mileage = mileage
		self.x, self.y = 0, 0
		self.tank = 20

	def move_right(self, distance=1):
		if self.tank <= 0:
			return

		if self.tank >= distance:
			self.x = self.x + distance
			self.mileage = self.mileage + distance
			self.tank = self.tank - distance
		else:
			self.x = self.x + self.tank
			self.mileage = self.mileage + self.tank
			self.tank = 0

	def move_up(self, distance=1):
		self.y = self.y + distance
		self.mileage = self.mileage + distance
		self.tank = self.tank - distance




new_sedan = Sedan()
print('소유자', new_sedan.owner)
print('마일리지', new_sedan.mileage)
print('X', new_sedan.x)
print('Y', new_sedan.y)
print('-' * 40)

new_sedan.move_right()
new_sedan.move_up()
new_sedan.move_right(3)
new_sedan.move_up(7)
new_sedan.move_right(30)
print('마일리지', new_sedan.mileage)
print('X', new_sedan.x)
print('Y', new_sedan.y)
print('-' * 40)
#
