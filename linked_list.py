class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

	def __str__(self):
		return '{} -> {}'.format(str(self.data), str(self.next))


class LinkedList:
	def __init__(self, head):
		self.head = head

	def append(self, data):
		new_node = Node(data, None)
		
		if not self.head:
			self.head = new_node
			return
		
		node_to_append = self.head
		while node_to_append.next:
			node_to_append = node_to_append.next

		node_to_append.next = new_node

	def get(self, index):
		if not self.head:
			raise IndexError('Linked list empty')
		
		node_to_get = self.head
		
		while index != 0:
			node_to_get = node_to_get.next
			
			if not node_to_get:
				raise IndexError('Index out of bounds')
			
			index -= 1
		
		return node_to_get.data

	def remove_first(self):
		if not self.head:
			raise IndexError('Linked list empty')
		node_to_remove = self.head
		node_after = node_to_remove.next
		self.head = node_after
		return node_to_remove.data

	def remove(self, index):
		if index == 0:
			return self.remove_first()
		
		if not self.head:
			raise IndexError('Linked list empty')

		previous_node = None
		node_to_remove = self.head

		while index != 0:
			previous_node = node_to_remove
			node_to_remove = node_to_remove.next
			
			if not node_to_remove:
				raise IndexError('Index out of bounds')
			
			index -= 1

		previous_node.next = node_to_remove.next

		return node_to_remove.data


if __name__ == '__main__':
	node_1 = Node('hello', None)
	linked_list = LinkedList(node_1)
	print(linked_list.head)
	# linked_list.append(Node('hi', None))
	linked_list.append('hi')
	print(linked_list.head)
	linked_list.append('welcome')
	print(linked_list.head)
	print(linked_list.get(0))
	print(linked_list.get(1))
	print(linked_list.get(2))
	# print(linked_list.get(3))
	# print(linked_list.get(4))
	print('Removing {}'.format(linked_list.remove_first()))
	print(linked_list.head)
	print('Adding good-bye')
	linked_list.append('good-bye')
	print(linked_list.head)
	print('Removing {}'.format(linked_list.remove(1)))
	print(linked_list.head)
	print('Removing {}'.format(linked_list.remove(1)))
	print(linked_list.head)
	print('Removing {}'.format(linked_list.remove(0)))
	print(linked_list.head)
