# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) Time | O(d) Space where n is nodes in tree and d is longest branch
def binaryTreeDiameter(tree):
    # Write your code here.
	array = [0]
	binaryTreeDiameterHelper(tree, array)
	return array[0]

def binaryTreeDiameterHelper(tree, array):
	if tree is None:
		array[0] = max(array[0], 0)
		return 0
	else:
		left = binaryTreeDiameterHelper(tree.left, array)
		right = binaryTreeDiameterHelper(tree.right, array)
		array[0] = max(array[0], left + right)
	return 1 + max(left, right)
		
	
