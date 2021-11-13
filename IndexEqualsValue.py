# O(logn) Time | O(1) Space, where n is length of array
def indexEqualsValue(array):
    # Write your code here.
	left = 0
	right = len(array) - 1
	indexToReturn = -1
	while left <= right:
		mid = (left + right) // 2
		if array[mid] == mid:
			indexToReturn = mid
			right = mid - 1
		elif array[mid] > mid:
			right = mid - 1
		else:
			left = mid + 1
	return indexToReturn
