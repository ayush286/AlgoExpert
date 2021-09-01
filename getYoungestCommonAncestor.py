# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

#O(d) Time | O(1) Space where d is depth of ancestralTree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # get depth of descendants
	depthOne = getDepth(descendantOne, topAncestor)
	depthTwo = getDepth(descendantTwo, topAncestor)
	if depthTwo == 0 or depthOne == 0:
		return topAncestor
	if depthTwo > depthOne:
		parentTwo = descendantTwo
		while depthTwo != depthOne:
			parentTwo = parentTwo.ancestor
			depthTwo -= 1		
		if parentTwo == descendantOne:
			return descendantOne
		while parentTwo != topAncestor and parentTwo != descendantOne:
			parentTwo = parentTwo.ancestor
			descendantOne = descendantOne.ancestor
		return parentTwo
	else:
		parentOne = descendantOne
		while depthTwo != depthOne:
			parentOne = parentOne.ancestor
			depthOne -= 1
		
		if parentOne == descendantTwo:
			return descendantTwo
		while parentOne != topAncestor and parentOne != descendantTwo:
			parentOne = parentOne.ancestor
			descendantTwo = descendantTwo.ancestor
		return parentOne
	
def getDepth(descendant, topAncestor):
	node = descendant
	depth = 0
	while node != topAncestor:
		node = node.ancestor
		depth += 1
	return depth
