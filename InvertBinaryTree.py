#O(n) Time | O(d) Space where n is nodes in Tree and d is depth of tree
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return 
	temp = tree.left
	tree.left = tree.right
	tree.right = temp
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	return


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
