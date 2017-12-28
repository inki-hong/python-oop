import linked_list

class Queue:
	def __init__(self):
		self._linked_list = linked_list.LinkedList()

	def enqueue(self, item):
		self._linked_list.append(item)

	def dequeue(self):
		return self._linked_list.remove_first()

	def poll(self):
		return self._linked_list.get(0)

	def is_empty(self):
		return not self._linked_list.head
