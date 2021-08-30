# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	# O(v + e) Time | O(v) Space where v is vertices of graph and e 
	# their edges
    def breadthFirstSearch(self, array):
        # Write your code here.
        left = 0
		queue = [self]
		while left < len(queue):
			array.append(queue[left].name)
			if queue[left].children:
				for node in queue[left].children:
					queue.append(node)
			left += 1
		return array
		
