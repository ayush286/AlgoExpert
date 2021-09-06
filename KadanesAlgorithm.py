#O(n) Time | O(1) Space where n is length of array
# not the official algorithm
def kadanesAlgorithm(array):
    # Write your code here.
	if len(array) < 1:
		return array
    runningSum = array[0]
	maxSum = runningSum
	for integer in array[1:]:
		if runningSum is None:
			if integer > 0:
				runningSum = integer
			continue
		if integer < 0:
			if runningSum < 0:
				runningSum = max(runningSum, integer)
			else:
				maxSum = max(runningSum, maxSum)
				newSum = runningSum + integer
				if newSum > 0:
					runningSum += integer
				else:
					maxSum = max(runningSum, maxSum)
					runningSum = None
		else:
			if runningSum < 0:
				runningSum = integer
			else:
				runningSum += integer
	return max(maxSum, runningSum) if runningSum is not None else maxSum
					
