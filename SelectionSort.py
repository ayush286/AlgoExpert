# O(n^2) Time | O(1) Space, where n is length of array
def selectionSort(array):
    # Write your code here.
    for index in range(len(array)):
		minimum = array[index]
		for innerIndex in range(index + 1, len(array)):
			if array[innerIndex] <= minimum:
				minimum = array[innerIndex]
				array[innerIndex], array[index] = array[index], array[innerIndex]
	return array
