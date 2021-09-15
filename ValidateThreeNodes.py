# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(d) Time | O(d) Space where d is height between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
	# nodeOne -> nodeTwo -> nodeThree
	first = findSuccessor(nodeOne, nodeTwo)
	second = findSuccessor(nodeTwo, nodeThree)
	if first == nodeTwo and second == nodeThree:
		return True
	# nodeThree -> nodeTwo -> nodeOne
	first = findSuccessor(nodeThree, nodeTwo)
	second = findSuccessor(nodeTwo, nodeOne)
	if first == nodeTwo and second == nodeOne:
		return True
	return False

def findSuccessor(parent, node):
	if parent is None:
		return 
	if node.value == parent.value:
		return node
	if node.value < parent.value:
		nodeReceived = findSuccessor(parent.left, node)
		if nodeReceived is not None:
			return nodeReceived
	else:
		nodeReceived = findSuccessor(parent.right, node)
		if nodeReceived is not None:
			return nodeReceived
	return
