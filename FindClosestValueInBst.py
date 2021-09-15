# O(n) Time | O(d) Space, where n is total nodes in tree and d 
# is longest branch
def findClosestValueInBst(tree, target):
    # Write your code here.
    closestValue = tree.value
	return findClosestValueInBstHelper(tree, target, closestValue)
	
def findClosestValueInBstHelper(node, target, closestValue):
	if node is None:
		return closestValue
	currentDifference = abs(target - node.value)
	
	if currentDifference < abs(target - closestValue):
		closestValue = node.value
	closestValue = findClosestValueInBstHelper(node.left, target, closestValue)
	closestValue = findClosestValueInBstHelper(node.right, target, closestValue)
	return closestValue

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
