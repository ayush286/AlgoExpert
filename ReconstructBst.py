# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
	tree = BST(preOrderTraversalValues[0])
    reconstructBstHelper(preOrderTraversalValues, float("-inf"), float("inf"), tree, 1)
	return tree

def reconstructBstHelper(array, lower, upper, tree, index):
	if index == len(array):
		return index
	if array[index] < upper and array[index] >= lower:
		node = BST(array[index])
		tree = node
		index += 1
		if len(array) <= index:
			return index
		index = reconstructBstHelper(array, lower, array[index], tree.left, index)
		index = reconstructBstHelper(array, array[index], upper, tree.right, index)
	return index
