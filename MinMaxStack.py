# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.mins = []
		self.maxs = []
		self.stack = []
	
	
	# O(1) Time | O(1) Space
    def peek(self):
        # Write your code here.
        return self.stack[len(self.stack) - 1] if len(self.stack) > 0 else None
	
	
	# O(1) Time | O(1) Space
    def pop(self):
        # Write your code here.
		if len(self.stack) < 1:
			return 
        if self.mins[len(self.mins) - 1] == self.stack[len(self.stack) - 1]:
			self.mins.pop()
		if self.maxs[len(self.maxs) - 1] == self.stack[len(self.stack) - 1]:
			self.maxs.pop()
		return self.stack.pop()

	
	# O(1) Time | O(1) Space
    def push(self, number):
        # Write your code here.
		if len(self.stack) < 1:
			self.stack.append(number)
			self.mins.append(number)
			self.maxs.append(number)
			return
        if number <= self.mins[len(self.mins) - 1]:
			self.mins.append(number)
		if number >= self.maxs[len(self.maxs) - 1]:
			self.maxs.append(number)
		self.stack.append(number)
		return
	
	
	# O(1) Time | O(1) Space
    def getMin(self):
        # Write your code here.
        return self.mins[len(self.mins) - 1] if len(self.mins) > 0 else None
	
	
	# O(1) Time | O(1) Space
    def getMax(self):
        # Write your code here.
        return self.maxs[len(self.maxs) - 1] if len(self.maxs) > 0 else None
