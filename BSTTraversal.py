#O(n) Time | O(n) Space where n is nodes in tree 
def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
		return array
	array = inOrderTraverse(tree.left, array)
	array.append(tree.value)
	array = inOrderTraverse(tree.right, array)
	return array

#O(n) Time | O(n) Space where n is nodes in tree 
def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
		return array
	array.append(tree.value)
	array = preOrderTraverse(tree.left, array)
	array = preOrderTraverse(tree.right, array)
	return array

#O(n) Time | O(n) Space where n is nodes in tree 
def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
		return array	
	array = postOrderTraverse(tree.left, array)
	array = postOrderTraverse(tree.right, array)
	array.append(tree.value)
	return array
