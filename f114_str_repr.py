class Sedan():
	no_of_doors = 4

	def __init__(self, o='Unknown', pn='', m=0):
		self.owner = o
		self.plate_no = pn
		self.mileage = m

	def __str__(self):
		return 'Sedan owned by {} plate no. {} mileage {}'.format(
			self.owner, self.plate_no, self.mileage
		)

alice_sedan = Sedan('Alice', 'ABCDE', 10000)
print(alice_sedan)
