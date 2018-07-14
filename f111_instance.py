class Sedan():
	no_of_doors = 4

	def set_owner(self, owner):
		self.owner = owner  # alice_sedan.owner = 'Alice'

	def set_plate_no(self, plate_no):
		self.plate_no = plate_no

	def set_mileage(self, mileage):
		self.mileage = mileage









alice_sedan = Sedan()
# print(alice_sedan.owner)  # attribute error

Sedan.set_owner(alice_sedan, 'Alice')
alice_sedan.set_owner('Alice')

Sedan.set_plate_no(alice_sedan, 'ABCDE')

alice_sedan.set_mileage(10000)

print(alice_sedan.owner)
print(alice_sedan.plate_no)
print(alice_sedan.mileage)



#
