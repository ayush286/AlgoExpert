# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	def depthFirstSearch(self, array):
		array = self.depthFirstSearchHelper(array, self)
		return array

	#O(n) Time | O(1) Space where n is total nodes in graph
	def depthFirstSearchHelper(self, array, node):
		array.append(node.name)
		if not node.children:
			return array
		for child in node.children:
			array = self.depthFirstSearchHelper(array, child)
		return array
