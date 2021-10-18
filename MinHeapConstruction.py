# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
	
	#O(nlogn) Time | O(1) Space, where n is length of array
    def buildHeap(self, array):
        # Write your code here.
		self.heap = []
		for elem in array:
			self.insert(elem)
        return self.heap

	# O(log(n)) Time | O(1) Space, where n is length of array
    def siftDown(self, nodeIndex, array):
        # Write your code here.
		smaller = nodeIndex * 2 + 1
		bigger = nodeIndex * 2 + 2
		if smaller >= len(self.heap) or bigger >= len(self.heap):
			if smaller < len(self.heap):
				if array[nodeIndex] > array[smaller]:
					array = self.swap(nodeIndex, smaller, array)
			return
		# if parent smaller than child, swap them, else swap bigger child
		while nodeIndex < len(self.heap) and (array[nodeIndex] > array[smaller] or array[nodeIndex] > array[bigger]):
			if self.heap[bigger] < self.heap[smaller]:
				smaller, bigger = bigger, smaller
			if array[nodeIndex] > array[smaller]:
				self.heap = self.swap(nodeIndex, smaller, self.heap)
				nodeIndex = smaller
			elif array[nodeIndex] > array[bigger]:
				self.heap = self.swap(nodeIndex, bigger, self.heap)
				nodeIndex = bigger
			else:
				return
			left = nodeIndex * 2 + 1
			right = nodeIndex * 2 + 2
			smaller = left
			bigger = right
			if left >= len(self.heap) or right >= len(self.heap):
				break
		if smaller < len(self.heap):
			if array[nodeIndex] > array[smaller]:
				array = self.swap(nodeIndex, smaller, array)
		
		
	# O(log(n)) Time | O(1) Space, where n is length of array	
    def siftUp(self, heapArray, nodeIndex):
        # Write your code here.
		parentIndex = (nodeIndex - 1) // 2
		if parentIndex < 0:
			return
		while parentIndex >= 0 and heapArray[nodeIndex] < heapArray[parentIndex]:
			heapArray = self.swap(nodeIndex, parentIndex, heapArray)
			nodeIndex = parentIndex
			parentIndex = (nodeIndex - 1) // 2
	
	# O(1) Time | O(1) Space
	def swap(self, one, two, array):
		array[one], array[two] = array[two], array[one]
		return array
		
	# O(1) Time | O(1) Space	
    def peek(self):
        # Write your code here.
		return self.heap[0] if len(self.heap) >= 1 else None
	
	# O(log(n)) Time | O(1) Space, where n is length of array		
    def remove(self):
        # Write your code here.
		if len(self.heap) == 1:
			minimum = self.heap.pop()
			return minimum
		elif len(self.heap) == 0:
			return None
        self.heap = self.swap(0, len(self.heap) - 1, self.heap)
		minimum = self.heap.pop()
		self.siftDown(0, self.heap)
		return minimum
	
	
	# O(log(n)) Time | O(1) Space, where n is length of array
    def insert(self, value):
        # Write your code here.
        if len(self.heap) < 1:
			self.heap.append(value)
			return
		self.heap.append(value)
		self.siftUp(self.heap, len(self.heap) - 1)
