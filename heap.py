class Heap(object):

	def __init__(self, nums=[]):
		self.heap = nums
		self.heapify()

	def push(self, num):
		self.heap.append(num)
		self.__repair_up_to_root(len(self.heap) -1)

	def pop(self):
		val = self.heap[0]
		self.heap[0] = self.heap[-1]
		del self.heap[-1]
		self.__repair_down(0)
		return val

	def heapify(self):
		for i in xrange(len(self.heap)-1, 0, -1):
			if self.heap[i] < self.heap[(i+1)/2 - 1]:
				temp = self.heap[i]
				self.heap[i] = self.heap[(i+1)/2 - 1]
				self.heap[(i+1)/2 - 1] = temp

	def __repair_up_to_root(self, index):
		while index > 0:
			index = self.__repair_up(index)

	def __repair_up(self, index):
			if(index <=0 or index >= len(self.heap)): return -1

			parent = (index+1)/2 - 1
			if self.heap[index] > self.heap[parent]:
				return -1
			self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
			return parent

	def __repair_down(self, index):
		if index >= len(self.heap):
			return
		rchild = (index +1) * 2
		self.__repair_up(rchild)
		self.__repair_up(rchild - 1)

		self.__repair_down(rchild)
		self.__repair_down(rchild - 1)