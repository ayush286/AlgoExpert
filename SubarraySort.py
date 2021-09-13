# O(n) Time | O(1) Space, where n is length of array
def subarraySort(array):
    # Write your code here.
	start = None
	end = None
	# locate startIdx
	for index in range(1, len(array)):
		if array[index - 1] > array[index]:
			if start is None:
				start = backtrackNewStart(array, array[index], index)
			else:
				if array[start] > array[index]:
					start = backtrackNewStart(array, array[index], start)
	if start is None:
		return [-1, -1]
	# locate endIdx
	for index in reversed(range(len(array) -1)):
		if array[index] > array[index + 1]:
			if end is None:
				end = backTrackNewEnd(index, array[index], array)
			else:
				if array[end] < array[index]:
					end = backTrackNewEnd(end, array[index], array)
	return [start, end]
	
	
def backtrackNewStart(array, target, start):
	while start > 0:
		newStart = start - 1
		if array[newStart] <= target:
			return newStart + 1
		start -= 1
	return 0

def backTrackNewEnd(end, target, array):
	while end < len(array) - 1:
		newEnd = end + 1
		if array[newEnd] > target:
			return end
		end += 1
	return len(array) - 1
					
