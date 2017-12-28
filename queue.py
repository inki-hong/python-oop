class Queue:
	def __init__(self):
		self._list = []

	def enqueue(self, item):
		self._list.append(item)

	def dequeue(self):
		item = self._list[0]
		del self._list[0]
		return item

	def poll(self):
		return self._list[0]

	def is_empty(self):
		return len(self._list) == 0
