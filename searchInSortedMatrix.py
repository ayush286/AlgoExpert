#O(n + m) Time | O(1) Space where n and m are rows and columns of matrix
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    node = [0, len(matrix[0]) - 1]
	while(node[0] < len(matrix) and node[1] >= 0):
		if target == matrix[node[0]][node[1]]:
			return node
		elif target > matrix[node[0]][node[1]]:
			node[0] += 1
		else:
			node[1] -= 1
	return [-1, -1]
