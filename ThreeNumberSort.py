# O(n) Time | O(1) Space, where n is lengtho of array
def threeNumberSort(array, order):
    # Write your code here.
	if len(array) <= 1:
		return array
    toSwap = 0
	for index in range(len(array)):
		if array[index] == order[0]:
			array[index], array[toSwap] = array[toSwap], array[index]
			toSwap += 1
	for index in range(toSwap, len(array)):
		if array[index] == order[1]:
			array[index], array[toSwap] = array[toSwap], array[index]
			toSwap += 1
	return array
