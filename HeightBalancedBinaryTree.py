# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.
	height = heightBalancedBinaryTreeHelper(tree)
	return height != -1


#O(n) Time | O(h) Space whre n is total nodes in tree and h is it's height
def heightBalancedBinaryTreeHelper(tree):
	if tree is None:
		return 0
	leftHeight = heightBalancedBinaryTreeHelper(tree.left)
	rightHeight = heightBalancedBinaryTreeHelper(tree.right)
	nodeHeight = getHeight(leftHeight, rightHeight) # if -1 => unbalanced
	if nodeHeight == -1:
		return -1
	else:
		return nodeHeight + 1

def getHeight(left, right):
	if left == right:
		return left
	elif left > right:
		if left - right > 1:
			return -1
		else:
			return left
	else:
		if right - left > 1:
			return -1
		else:
			return right
