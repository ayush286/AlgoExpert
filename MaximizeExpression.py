#O(n) Time | O(n) Space, where n is length of array
def maximizeExpression(array):
    # Write your code here.
	if len(array) < 4:
		return 0
    maxA = [array[0]]
	for elem in array[1:]:
		maxA.append(max(elem, maxA[-1]))
	maxAB = [array[0] - array[1]]
	for index in range(2, len(array)):
		maxAB.append(max(maxAB[-1], maxA[index - 1] - array[index]))
	maxABC = [array[0] - array[1] + array[2]]
	for index in range(3, len(array)):
		maxABC.append(max(maxABC[-1], maxAB[index - 2] + array[index]))
	maxABCD = [array[0] - array[1] + array[2] - array[3]]
	for index in range(4, len(array)):
		maxABCD.append(max(maxABCD[-1], maxABC[index - 3] - array[index]))
	return maxABCD[-1]
