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
		self._data = nums
		self.__heapify()


	def push(self, num):
		"""
		Push a number to the heap keeping it intact
		num: The integer to add to the heap
		"""
		self._data.append(num)
		self.__repair_up_to_root(len(self._data) -1)


	def pop(self):
		"""
		Pops the minimum value from the heap, while keeping it intact
		rtype: The minimum number
		"""
		val = self._data[0]
		self._data[0] = self._data[-1]
		del self._data[-1]

		self.__repair_down(0)
		return val


	def __heapify(self):
		"""
		Repairs the entire heap
		"""
		for i in xrange(len(self._data)-1, 0, -1):
			if self._data[i] < self._data[(i+1)/2 - 1]:
				self._data[i], self._data[(i+1)/2 - 1] = self._data[(i+1)/2 - 1], self._data[i]


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
		if(index <=0 or index >= len(self._data)): return -1

		parent = (index+1)/2 - 1
		if self._data[index] > self._data[parent]:
			return -1
		self._data[index], self._data[parent] = self._data[parent], self._data[index]
		return parent


	def __repair_down(self, index):
		"""
		Repairs the heap downwards starting a given node
		index: The index of the node to repair from
		"""
		if index >= len(self._data):
			return
		mchild = self.__get_min_child_index(index)
		if self.__repair_up(mchild) == index:
			self.__repair_down(mchild)


	def __get_min_child_index(self, index):
		"""
		Returns the index of the child with minimum value
		index: Index of a parent node
		rtype: If node has children then index of the child with minimum value, otherwise -1
		"""
		rchild = (index +1) * 2
		if rchild - 1 < len(self._data):
			if rchild < len(self._data):
				if self._data[rchild] < self._data[rchild-1]:
					return rchild
				
			return rchild -1
		return -1
