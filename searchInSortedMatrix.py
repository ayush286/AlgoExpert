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

###Solution 2
#O(rlogc) Time | O(1) Space where r is number of rows of matrix and 
#c is number of columns of matrix 
def searchInSortedMatrix(matrix, target):
    # Write your code here.
	col = 0
	for row in range(len(matrix)):
		low = 0
		high = len(matrix[row]) - 1
		if target < matrix[row][low]:
			return [-1, -1]
		if target > matrix[row][high]:
			continue
		while low <= high:
			middle = (low + high) // 2
			if target == matrix[row][middle]:
				return [row, middle]
			elif target < matrix[row][middle]:
				high = middle - 1
			else:
				low = middle + 1
	return [-1, -1]

