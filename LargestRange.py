# O(nlogn) Time | O(1) Space, where n is length of array
def largestRange(array):
    # Write your code here.
    array.sort()
	print(array)
	longestRange = [None, None]
	currentRange = [None, None]
	for index in range(1, len(array)):
		print(currentRange)
		if array[index] - array[index - 1] <= 1:
			if currentRange[0] is None:
				currentRange[0] = array[index - 1]
		else:
			if currentRange[0] is not None:
				currentRange[1] = array[index - 1]
				if longestRange[0] is None:
					longestRange = currentRange.copy()
					currentRange = [None, None]
				else:
					longestRangeLength = longestRange[1] - longestRange[0]
					currentRangeLength = currentRange[1] - currentRange[0]
					if currentRangeLength > longestRangeLength:
						longestRange = currentRange.copy()
						currentRange = [None, None]
					else:
						currentRange = [None, None]
	if currentRange[0] is not None:
		currentRange[1] = array[-1]
		if longestRange[0] is None:
			return currentRange
		else:
			if longestRange[1] - longestRange[0] < currentRange[1] - currentRange[0]:
				longestRange = currentRange.copy()
	if longestRange[0] is None:
		return [array[0], array[0]]
	return longestRange
