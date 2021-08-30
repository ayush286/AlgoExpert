#O(n) Time | O(1) Space
def firstDuplicateValue(array):
    # Write your code here.
	for elem in array:
		if array[abs(elem) - 1] < 0:
			return abs(elem)		
		array[abs(elem) - 1] *= -1
    return -1
