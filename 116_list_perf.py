import datetime
import random

sm_list, md_list, lg_list = [], [], []
for i in range(100):
	sm_list.append(random.choice('ABCD'))
for i in range(10000):
	md_list.append(random.choice('ABCD'))
for i in range(1000000):
	lg_list.append(random.choice('ABCD'))

temp = []

t0 = datetime.datetime.now()
for t in range(200):
	temp.append( sm_list[random.randrange(100)] )
t1 = datetime.datetime.now()
print('Small list READ: {} seconds'.format((t1 - t0).total_seconds()))

temp.clear()

t0 = datetime.datetime.now()
for t in range(200):
	temp.append( md_list[5000 + random.randrange(100)] )
t1 = datetime.datetime.now()
print('Medium list READ: {} seconds'.format((t1 - t0).total_seconds()))

temp.clear()

t0 = datetime.datetime.now()
for t in range(200):
	temp.append( lg_list[500000 + random.randrange(100)] )
t1 = datetime.datetime.now()
print('Large list READ: {} seconds'.format((t1 - t0).total_seconds()))
