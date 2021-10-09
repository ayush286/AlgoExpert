# O(logn) Time | O(1) Space, where n is length of array
def searchForRange(array, target):
    # Write your code here.
    contains = None
	left = 0
	right = len(array) - 1
	lefts = None
	rights = None
	
	result = modifiedBinarySearch(left, right, array, target, 0)
	if result[0]:
		lefts = [left, result[1] - 1]
		rights = [result[1] + 1, right]
		contains = [result[1], result[1]]
	else:
		return [-1, -1]
	
	while lefts[0] <= lefts[1]:
		result = modifiedBinarySearch(lefts[0], lefts[1], array, target, -1)
		if not result[0]:
			break
		else:
			lefts[0] = result[2]
			lefts[1] = result[3]
			contains[0] = result[1]
	
	while rights[0] <= rights[1]:
		result = modifiedBinarySearch(rights[0], rights[1], array, target, 1)
		if not result[0]:
			break
		else:
			rights[0] = result[2]
			rights[1] = result[3]
			contains[1] = result[1]
	return contains


def modifiedBinarySearch(left, right, array, target, direction):	
	while left <= right:
		middle = (right + left) // 2
		if array[middle] == target:
			lefts = [left, middle - 1]
			rights = [middle + 1, right]
			contains = [middle, middle]
			if direction == 0:
				return [True, middle]
			elif direction == 1:
				return [True, middle, middle + 1, right]
			else:
				return [True, middle, left, middle - 1]
		elif array[middle] > target:
			right = middle - 1
		else:
			left = middle + 1
	return [False]
