class Sedan():
	# print('Hi')
	no_of_doors = 4

print(Sedan)
print(type(Sedan))

print(Sedan.no_of_doors)

# Sedan.no_of_doors = 5
# print(Sedan.no_of_doors)

alice_sedan = Sedan()
bob_sedan = Sedan()

print(alice_sedan)
print(bob_sedan)

print(alice_sedan.no_of_doors)

alice_sedan.owner = 'Alice'
alice_sedan.plate_no = 'ABCDE'
alice_sedan.mileage = 10000
