import datetime
import random

md_list, lg_list = [], []
for i in range(10000):
	md_list.append(random.choice('ABCD'))
for i in range(1000000):
	lg_list.append(random.choice('ABCD'))

t0 = datetime.datetime.now()
for t in range(200):
	md_list.insert(5000, 'X')
t1 = datetime.datetime.now()
print('Medium list INSERT: {} seconds'.format((t1 - t0).total_seconds()))

t0 = datetime.datetime.now()
for t in range(200):
	lg_list.insert(500000, 'X')
t1 = datetime.datetime.now()
print('Large list INSERT: {} seconds'.format((t1 - t0).total_seconds()))
