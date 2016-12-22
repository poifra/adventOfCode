from collections import Counter

class LinkedList(object):
	class Node:
		def __init__(self, value=None):
			self.value = value
			self.next = None
			self.previous = None

	def __init__(self):
		self.head = None
		self.length = 0
		self.tail = None

	def __len__(self):
		return self.length

	def __str__(self):
		pos = self.head
		values = []
		while pos is not None:
			values.append(pos.value)
			pos = pos.next
		return " ".join(map(str,values))

	def append(self, value):
		n = LinkedList.Node(value)
		if self.head is None:
			self.head = n
			self.tail = n
		else:
			self.tail.next = LinkedList.Node(value)
			self.tail.next.previous = self.tail
			self.tail = self.tail.next
			self.length += 1

	def makeCircular(self):
		self.tail.next = self.head

	def remove(self, value):
		pos = self.head
		while pos is not None and pos.value != value:
			pos = pos.next
		if pos is None:
			raise ValueError("Value not found")
		else:
			retval = pos.value
			pos.next.previous = pos.previous
			pos.previous.next = pos.next
			return retval


def part1():
	n = 5
	ll = LinkedList()
	for i in range(n):
		ll.append([i+1,1])

	while(len(ll) != 1):
		for i in range(len(ll)):
			if None:
				pass
