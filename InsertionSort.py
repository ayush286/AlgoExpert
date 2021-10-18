# Average and Worst -> O(n^2) Time | O(1) Space, where n is length of array
# Best O(n) Time | O(1) Space, where n is length of array
def insertionSort(array):
    # Write your code here.
	for index in range(len(array)):
		start = getInsertPosition(array, index)
		if start != index:
			insertAndSwap(array, start, index)
	return array

def insertAndSwap(array, start, end):
	elem = array[end]
	index = start
	while index < end:
		array[index], elem = elem, array[index]
		index += 1
	array[end] = elem
	
def getInsertPosition(array, index):
	elem = array[index]
	for i in reversed(range(index)):
		if elem >= array[i]:
			return i + 1
	return 0
