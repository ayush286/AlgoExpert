# O(n^2) Time | O(1) Space, where n is leength of array
def bubbleSort(array):
    # Write your code here.
    isModified = True
	while isModified:
		isModified = False
		for index in range(1, len(array)):
			if array[index - 1] > array[index]:
				array[index - 1], array[index] = array[index], array[index - 1]
				isModified = True
	return array
