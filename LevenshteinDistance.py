# O(n * m) Time | O(n * m) Space, where n and m are lengths of input strings 
def levenshteinDistance(str1, str2):
    # Write your code here.
    matrix = [[0 for col in range(len(str2) + 1)] for row in range(len(str1) + 1)]
	for col in range(len(matrix[0])):
		matrix[0][col] = col
	for row in range(len(matrix)):
		matrix[row][0] = row
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[row])):
			if str1[row - 1] == str2[col - 1]:
				matrix[row][col] = matrix[row - 1][col -1]
			else:
				matrix[row][col] = 1 + min(matrix[row -1][col], matrix[row - 1][col -1], matrix[row][col - 1])
	return matrix[len(matrix) - 1][len(matrix[0]) - 1]
