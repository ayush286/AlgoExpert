#O(nlogn) Time | O(n) Space where n is length of array
def minHeightBst(array):
	low = 0
	high = len(array) - 1
	middle = (low + high) // 2
	bstTree = BST(array[middle])
	minHeightBstHelper(array, low, middle - 1, bstTree)
	minHeightBstHelper(array, middle + 1, high, bstTree)
    return bstTree

def minHeightBstHelper(array, low, high, tree):
	if low > high:
		return tree
	if low == high:
		tree.insert(array[low])
		return tree
	middle = (low + high) // 2
	tree.insert(array[middle])
	minHeightBstHelper(array, low, middle - 1, tree)
	minHeightBstHelper(array, middle + 1, high, tree)
	return tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
