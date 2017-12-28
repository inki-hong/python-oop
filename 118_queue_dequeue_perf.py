import datetime
import random
import queue

md_queue = queue.Queue()
lg_queue = queue.Queue()
for i in range(10000):
	md_queue.enqueue(random.choice([2, 4, 8, 16]))
for i in range(1000000):
	lg_queue.enqueue(random.choice([2, 4, 8, 16]))

head = 0
t0 = datetime.datetime.now()
for t in range(200):
	head += md_queue.dequeue()
t1 = datetime.datetime.now()
print('Medium queue head sum: {}'.format(head))
print('Medium queue DEQUEUE: {} seconds'.format((t1 - t0).total_seconds()))

head = 0
t0 = datetime.datetime.now()
for t in range(200):
	head += lg_queue.dequeue()
t1 = datetime.datetime.now()
print('Large queue head sum: {}'.format(head))
print('Large queue DEQUEUE: {} seconds'.format((t1 - t0).total_seconds()))
