# class statement (복합문)
class Sedan():
	# print('Hi')
	no_of_doors = 4  # class attribute

print(Sedan)
print(type(Sedan))

print('도어 수', Sedan.no_of_doors)

# Sedan.no_of_doors = 5
# print('도어 수', Sedan.no_of_doors)
print('-' * 40)







# instantiation 개체화

alice_sedan = Sedan()
bob_sedan = Sedan()

print(alice_sedan)
print(bob_sedan)

print('도어 수', alice_sedan.no_of_doors)
print('-' * 40)









alice_sedan.owner = 'Alice'
alice_sedan.plate_no = 'ABCDE'
alice_sedan.mileage = 10000

print('Alice 번호판', alice_sedan.plate_no)
print('Bob 번호판', bob_sedan.plate_no)
print('클래스 번호판', Sedan.plate_no)









#
