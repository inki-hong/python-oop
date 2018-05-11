my_list = []

for n1 in range(20):
    inner = []
    for n2 in range(20):
        inner.append(n1 * n2)
    my_list.append(inner)

# print(my_list)
print(my_list[5][6])
print(my_list[4][8])
print(my_list[2][3])








my_list = [[n1 * n2 for n2 in range(20)]
           for n1 in range(20)]
print(my_list)
print(my_list[5][6])
print(my_list[4][8])
print(my_list[15][10])










#
