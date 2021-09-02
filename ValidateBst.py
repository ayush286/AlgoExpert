# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#O(n) Time | O(d) Space where n is total nodes in tree and d is depth of tree
def validateBst(tree):
    # Write your code here.
    isValid = True
	isValid = validateBstHelper(tree, float("-inf"), tree.value, tree.left, isValid)
	isValid = validateBstHelper(tree, tree.value, float("inf"), tree.right, isValid)	
	return isValid

def validateBstHelper(tree, minimum, maximum, node, isValid):
	if node is None:
		return isValid	

	if node.value >= maximum or node.value < minimum:
		isValid = False
		return isValid

	isValid = validateBstHelper(tree, minimum, node.value, node.left, isValid)
	isValid = validateBstHelper(tree, node.value, maximum, node.right, isValid)
	return isValid
