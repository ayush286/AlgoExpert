# O(n) Time | O(n) Space, where n is total elements in array
def zigzagTraverse(array):
    # Write your code here.
	if len(array) < 1:
		return []
	zigzags = []
	direction = "down"
	row = 0
	col = 0
	while len(zigzags) < len(array) * len(array[0]):
		zigzags.append(array[row][col])
		if row == len(array) - 1 and col == len(array[0]) - 1:
			break
		if direction == "down":
			row = row + 1
			col = col - 1
			if col < 0 or row > len(array) - 1:
				direction = "up"
				col = col + 1
				if row > len(array) - 1:
					row = row - 1
					col = col + 1
		else:
			row = row - 1
			col = col + 1
			if row < 0 or col > len(array[0]) - 1:
				direction = "down"
				row = row + 1
				if col > len(array[0]) - 1:
					col = col - 1
					row = row + 1
	return zigzags
					
				
					
