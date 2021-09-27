# O(n) Time | O(d) Space where n is nodes in tree and d is 
# length of longest branch
def maxPathSum(tree):
    # Write your code here.
	maxSum = [tree.value]
    maxPathSumHelper(tree, maxSum)
	return maxSum[0]

def maxPathSumHelper(tree, maxSum):
	if tree is None:
		return 0
	left = maxPathSumHelper(tree.left, maxSum)
	right = maxPathSumHelper(tree.right, maxSum)
	maxSum[0] = max(maxSum[0], tree.value + left + right, tree.value + left, tree.value + right, tree.value)
	return tree.value + max(left, right)
