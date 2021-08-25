def riverSizes(matrix):
    # Write your code here.
	rivers = []
    for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			#visited cell is marked as -1
			if matrix[row][col] == 1:
				matrix[row][col] = -1
				rivers.append(getSize(row, col, 1, matrix))
	return rivers
	
def getSize(row, col,size, matrix):
	edges = getEdges(row, col, matrix)
	for edge in edges:
		m = edge[0]
		n = edge[1]
		size += 1
		size = getSize(m, n, size, matrix)
	return size
		

def getEdges(row, col, matrix):
	#edges should check if cell has been visited or not
	upperRowBound = len(matrix)
	upperColBound = len(matrix[row])
	edges = []
	#left
	colL = col - 1
	if colL >= 0:
		if matrix[row][colL] == 1:
			matrix[row][colL] = -1
			edges.append([row, colL])
	#right
	colR = col + 1
	if colR < upperColBound:
		if matrix[row][colR] == 1:
			matrix[row][colR] = -1
			edges.append([row, colR])
	#up
	rowU = row - 1
	if rowU >= 0:
		if matrix[rowU][col] == 1:
			matrix[rowU][col] = -1
			edges.append([rowU, col])
	#down
	rowD = row + 1
	if rowD < upperRowBound:
		if matrix[rowD][col] == 1:
			matrix[rowD][col] = -1
			edges.append([rowD, col])
	return edges
