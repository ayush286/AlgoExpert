# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

# O(n) Time | O(d) Space, where d is the maximum depth array level
# in input array
def productSum(array):
    currentSum = productSumHelper(array, 1)
	return currentSum
    
def productSumHelper(array, depth):
	currentSum = 0
	for index in range(len(array)):
		if type(array[index]) is not list:
			currentSum += array[index]
		else:
			currentSum += (depth + 1) * productSumHelper(array[index], depth + 1)
	return currentSum
