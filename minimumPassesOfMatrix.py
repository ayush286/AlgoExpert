#O(w*h) Time| O(w*h) Space, where w an h are width and height of matrix
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passed = 0
	stack = []
	shouldTraverse = True
	while shouldTraverse:
		for row in range(len(matrix)):
			for col in range(len(matrix[row])):
				if matrix[row][col] < 0:
					#check flippable
					willFlip = isConversionPossible(row, col, matrix)
					if willFlip:
						stack.append([row, col])
		if len(stack) < 1:
			shouldTraverse = False
			break
		passed += 1
		convertNegatives(stack, matrix)
		stack = []
	return checkNegatives(matrix, passed)

def convertNegatives(stack, matrix):
	for index in stack:
		m = index[0]
		n = index[1]
		matrix[m][n] *= -1

def isConversionPossible(row, col, matrix):
	upperRowLimit = len(matrix)
	upperColLimit = len(matrix[row])
	#up
	if row - 1 >= 0:
		if matrix[row - 1][col] > 0:
			return True
	#down
	if row + 1 < upperRowLimit:
		if matrix[row + 1][col] > 0:
			return True
	#left
	if col - 1 >= 0:
		if matrix[row][col - 1] > 0:
			return True
	#right
	if col + 1 < upperColLimit:
		if matrix[row][col + 1] > 0:
			return True
	return False

def checkNegatives(matrix, passed):
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] < 0:
				return -1
	return passed
