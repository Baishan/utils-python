"""
Class that represents a heap ADT
Author: Brian Cullen (brianshan@gmail.com)
"""

class Heap(object):
	"""
	Class that represents a heap ADT
	"""

	def __init__(self, nums=[]):
		"""
		Initialises the heap from an array of numbers
		"""
		self.__heap = nums
		self.__heapify()


	def push(self, num):
		"""
		Push a number to the heap keeping it intact
		num: The integer to add to the heap
		"""
		self.__heap.append(num)
		self.__repair_up_to_root(len(self.__heap) -1)


	def pop(self):
		"""
		Pops the minimum value from the heap, while keeping it intact
		rtype: The minimum number
		"""
		val = self.__heap[0]
		self.__heap[0] = self.__heap[-1]
		del self.__heap[-1]
		
		self.__repair_down(0)
		return val


	def __heapify(self):
		"""
		Repairs the entire heap
		"""
		for i in xrange(len(self.__heap)-1, 0, -1):
			if self.__heap[i] < self.__heap[(i+1)/2 - 1]:
				self.__heap[i], self.__heap[(i+1)/2 - 1] = self.__heap[(i+1)/2 - 1], self.__heap[i]


	def __repair_up_to_root(self, index):
		"""
		Repairs the heap from an item up to the root
		index: The index of node to start at
		"""
		while index > 0:
			index = self.__repair_up(index)


	def __repair_up(self, index):
		"""
		Repairs a parent child order from the childs index
		index: The index of a child node
		rtype: The index of the parent, -1 if index points to root
		"""
			if(index <=0 or index >= len(self.__heap)): return -1

			parent = (index+1)/2 - 1
			if self.__heap[index] > self.__heap[parent]:
				return -1
			self.__heap[index], self.__heap[parent] = self.__heap[parent], self.__heap[index]
			return parent


	def __repair_down(self, index):
		"""
		Repairs the heap downwards starting a given node
		index: The index of the node to repair from
		"""
		if index >= len(self.__heap):
			return
		rchild = (index +1) * 2
		self.__repair_up(rchild)
		self.__repair_up(rchild - 1)

		self.__repair_down(rchild)
		self.__repair_down(rchild - 1)