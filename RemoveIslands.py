#O(n) Time | O(n) Space where n is total elements in matrix
def removeIslands(matrix):
    # Write your code here.
    # traverse boundary
	### first row, last row, first column, last column
	lastRow = len(matrix) - 1
	for col in range(len(matrix[0])):
		if matrix[0][col] == 1:
			exploreAndFlip(0, col, matrix)
	for col in range(len(matrix[lastRow])):
		if matrix[lastRow][col] == 1:
			exploreAndFlip(lastRow, col, matrix)
	for row in range(len(matrix)):
		if matrix[row][0] == 1:
			exploreAndFlip(row, 0, matrix)
	for row in range(len(matrix)):
		lastCol = len(matrix[row]) - 1
		if matrix[row][lastCol] == 1:
			exploreAndFlip(row, lastCol, matrix)		
	#traverse matrix
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == 1:
				exploreAndZero(row, col, matrix)

	#convert to positive traverse matrix
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == -1:
				matrix[row][col] = 1
	return matrix

def exploreAndFlip(row, col, matrix):
	matrix[row][col] = -1
	neighbours = getFlippables(row, col, matrix)
	for neighbour in neighbours:
		m = neighbour[0]
		n = neighbour[1]
		exploreAndFlip(m, n, matrix)
		
def exploreAndZero(row, col, matrix):
	matrix[row][col] = 0
	neighbours = getFlippables(row, col, matrix)
	for neighbour in neighbours:
		m = neighbour[0]
		n = neighbour[1]
		exploreAndZero(m, n, matrix)

def getFlippables(row, col, matrix):
	rowUpperBound = len(matrix)
	colUpperBound = len(matrix[row])
	neighbours = []
	#left
	if col - 1 >= 0:
		if matrix[row][col - 1] == 1:
			neighbours.append([row, col - 1])
	#right
	if col + 1 < colUpperBound:
		if matrix[row][col + 1] == 1:
			neighbours.append([row, col + 1])	
	#up
	if row - 1 >= 0:
		if matrix[row - 1][col] == 1:
			neighbours.append([row - 1, col])
	#down
	if row + 1 < rowUpperBound:
		if matrix[row + 1][col] == 1:
			neighbours.append([row + 1, col])
	return neighbours	
