# O(n) Time | O(n) Space, where n is total elements in matrix 
def spiralTraverse(array):
    # Write your code here.
	if len(array) < 1:
		return array
	spiralElements = []
	rowMin = 0
	colMin = 0
	rowMax = len(array)
	colMax = len(array[0])
	while colMin < colMax and rowMin < rowMax:
		# col traverse (left to right)
		if rowMin < len(array):
			if rowMin == rowMax:
				continue
			for col in range(colMin, colMax):
				spiralElements.append(array[rowMin][col])
		rowMin += 1
		# update row min 

		# row Traverse
		if colMax >= 0:
			if colMin == colMax:
				continue
			for row in range(rowMin, rowMax):
				spiralElements.append(array[row][colMax - 1])
		# update col max
		colMax -= 1

		# inverse col traverse
		if rowMax >= 0:
			if rowMin == rowMax:
				continue
			for col in reversed(range(colMin, colMax)):
				spiralElements.append(array[rowMax - 1][col])
		# update row max
		rowMax -= 1

		# inverse row traverse
		if colMin < len(array[0]):
			if colMin == colMax:
				continue
			for row in reversed(range(rowMin, rowMax)):
				spiralElements.append(array[row][colMin])
		# update col min
		colMin += 1
		
	return spiralElements 
