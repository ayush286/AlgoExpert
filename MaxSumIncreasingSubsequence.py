# O(n^2) Time | O(n) Space, where n is length of array
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    maxSubsequenceTillIdx = [[]]
	for index in range(len(array)):
		currentMaxSequence = [array[index]]
		for i in range(1, index + 1):
			if maxSubsequenceTillIdx[i][-1] < array[index]:
				if sum(currentMaxSequence) < sum(maxSubsequenceTillIdx[i]) + array[index]:
					currentMaxSequence = maxSubsequenceTillIdx[i].copy()
					currentMaxSequence.append(array[index])
		maxSubsequenceTillIdx.append(currentMaxSequence)
	maxSubsequence = [array[0], [array[0]]]
	for index in range(1, len(maxSubsequenceTillIdx)):
		currentIdxSequenceSum = sum(maxSubsequenceTillIdx[index])
		if currentIdxSequenceSum > maxSubsequence[0]:
			maxSubsequence = [currentIdxSequenceSum, maxSubsequenceTillIdx[index]]
	return 	maxSubsequence
