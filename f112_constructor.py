class Sedan():
	no_of_doors = 4  # class attribute

	# constructor (생성자)
	# underscore 양쪽에 2개씩!
	def __init__(self, o='Unknown',
	                   pn='', m=0):
		self.owner = o
		self.plate_no = pn
		self.mileage = m

	def set_owner(self, o):
		self.owner = o

	def set_plate_no(self, pn):
		self.plate_no = pn

	def set_mileage(self, m):
		self.mileage = m


new_sedan = Sedan()
print('소유자', new_sedan.owner)
print('번호판', new_sedan.plate_no)
print('마일리지', new_sedan.mileage)
print('-' * 40)

old_sedan = Sedan(m=20000)
print('소유자', old_sedan.owner)
print('번호판', old_sedan.plate_no)
print('마일리지', old_sedan.mileage)
print('-' * 40)

alice_sedan = Sedan('Alice', 'ABCDE', 10000)
print('소유자', alice_sedan.owner)
print('번호판', alice_sedan.plate_no)
print('마일리지', alice_sedan.mileage)
#
