# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

		
#O(n) Time | O(n) Space where n is nodes in tree
def findNodesDistanceK(tree, target, k):
    # Write your code here.
	ancestors = getAncestors(tree.left, target, [[tree, -1]], -1)
	if ancestors is None:
		ancestors = getAncestors(tree.right, target, [[tree, 1]], 1)
	if ancestors is None:
		ancestors = [[tree, 0]]
	nodes = []
	for index in reversed(range(len(ancestors))):
		newK = k - (len(ancestors) - index - 1)
		if newK < 0:
			break
		if ancestors[index][1] == 0:
			nodes = getChildDistanceK(ancestors[index][0], newK, 0, nodes)
		elif ancestors[index][1] == 1:
			if newK == 0:
				nodes.append(ancestors[index][0].value)
			else:
				nodes = getChildDistanceK(ancestors[index][0].left, newK, 1, nodes)
		else:
			if newK == 0:
				nodes.append(ancestors[index][0].value)
			else:
				nodes = getChildDistanceK(ancestors[index][0].right, newK, 1, nodes)	
    return nodes


#O(n) Time | O(k) Space where k is input and n is nodes in tree
def getChildDistanceK(tree, k, depth, childs):
	if tree is None:
		return childs
	if depth == k:
		childs.append(tree.value)
	else:
		childs = getChildDistanceK(tree.left, k, depth + 1, childs)
		childs = getChildDistanceK(tree.right, k, depth + 1, childs)
	return childs


#O(n) Time | O(n) Space where n is nodes in tree
def getAncestors(tree, target, ancestors, direction):
	if tree is None:
		return
	if tree.value == target:
		ancestors.append([tree, 0])
		return ancestors
	else:
		ancestors.append([tree, -1])
		left = getAncestors(tree.left, target, ancestors, direction)
		if left is None:
			ancestors.pop()
			ancestors.append([tree, 1])
			right = getAncestors(tree.right, target, ancestors, direction)
			if right is None:
				ancestors.pop()
			else:
				return ancestors
		else:
			return ancestors
