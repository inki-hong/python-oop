class Sedan():
	no_of_doors = 4

	def __init__(self, owner='Unknown', plate_no='', mileage=0):
		self.owner = owner
		self.plate_no = plate_no
		self.mileage = mileage

	def set_owner(self, owner):
		self.owner = owner

	def set_plate_no(self, plate_no):
		self.plate_no = plate_no

	def set_mileage(self, mileage):
		self.mileage = mileage

alice_sedan = Sedan('Alice', 'ABCDE', 10000)
new_sedan = Sedan()
old_sedan = Sedan(mileage=20000)
print(new_sedan.owner)
print(new_sedan.plate_no)
print(new_sedan.mileage)
