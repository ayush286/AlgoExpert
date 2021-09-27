class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if self.value <= value:
			self.insertHelper(value, self, self.right, "right")
		else:
			self.insertHelper(value, self, self.left, "left")
        return self
	# Average: O(log(n)) Time | O(log(n)) Space
	# Worst: O(n) Time | O(n) Space
	def insertHelper(self, value, prevNode, currNode, direction):
		if currNode is None:
			if direction == "left":
				prevNode.left = BST(value)
				return
			else:
				prevNode.right = BST(value)
				return
		if currNode.value <= value:
			self.insertHelper(value, currNode, currNode.right, "right")
		else:
			self.insertHelper(value, currNode, currNode.left, "left")
	# Average: O(log(n)) Time | O(log(n)) Space
	# Worst: O(n) Time | O(n) Space
    def contains(self, value):
        # Write your code here.
        if self.value == value:
			return True
		else:
			if self.value > value:
				if self.left is None:
					return False
				else:
					return self.left.contains(value)
			else:
				if self.right is None:
					return False
				else:
					return self.right.contains(value)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		self.removeHelper(value, None, self)		
        return self
	# Average: O(log(n)) Time | O(log(n)) Space
	# Worst: O(n) Time | O(n) Space
	def removeHelper(self, value, prevNode, currNode):
		if currNode.value == value:	
			# if alone
			if currNode.left is None and currNode.right is None:
				if prevNode is None:
					return
				if prevNode.left == currNode:
					prevNode.left = None
				else:
					prevNode.right = None
				return
			# if only left is available
			elif currNode.right is None:
				if prevNode is None:
					self.value = currNode.left.value
					self.right = currNode.left.right
					self.left = currNode.left.left
				elif prevNode.left == currNode:
					prevNode.left = currNode.left
				else:
					prevNode.right = currNode.left
				return
			# if both available
			else:
				# find right min 
				rightMin = self.getRightMin(currNode.right, currNode.right.value)
				currNode.value = rightMin
				currNode.right.removeHelper(rightMin, currNode, currNode.right)
		else:
			if currNode.value > value:
				self.removeHelper(value, currNode, currNode.left)
			else:
				self.removeHelper(value, currNode, currNode.right)
		return		
	# Average: O(log(n)) Time | O(log(n)) Space
	# Worst: O(n) Time | O(n) Space
	def getRightMin(self, currNode, currMin):
		while currNode is not None:
			currMin = currNode.value
			currNode = currNode.left
		return currMin
			
