class Stack:
	def __init__(self):
		self._list = []

	def push(self, item):
		self._list.append(item)

	def pop(self):
		item = self._list[-1]
		del self._list[-1]
		return item

	def peek(self):
		if len(self._list) == 0:
			return None
		return self._list[-1]
		# try:
		# 	self._list[-1]
		# except IndexError:
		# 	return None

	def is_empty(self):
		return len(self._list) == 0

stack = Stack()
print(stack.is_empty())	# True
stack.push('A')
stack.push('B')
stack.push('C')
print(stack.is_empty())	# False
print(stack.peek())		# C
print(stack.pop())		# C
print(stack.peek())		# B
print(stack.pop())		# B
print(stack.pop())		# A
print(stack.is_empty())	# True
print(stack.peek())		# ???
