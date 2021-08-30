#O(n) Time | O(1) Space where n is length of array
def longestPeak(array):
    # Write your code here.
    direction = 0
	longestPeak = 0
	currentPeak = 0
	peakFound = False
	if len(array) < 3:
		return 0
	for index in range(1, len(array)):
		print(array[index])
		print(currentPeak)
		if array[index] > array[index - 1]:
			if direction != 1:
				if currentPeak != 0 and direction == -1:
					if peakFound:
						longestPeak = max(currentPeak + 1, longestPeak)
					currentPeak = 1
				else:
					currentPeak = 1
			else:
				currentPeak += 1
			direction = 1
		elif array[index] < array[index - 1]:
			if direction == -1:
				if currentPeak > 0:
					currentPeak += 1
			elif direction == 1:
				#peak found
				peakFound = True
				currentPeak += 1
			direction = -1
		else:
			if direction == 1:
				currentPeak = 0
			elif direction == -1:
				if currentPeak > 0 and peakFound:
					longestPeak = max(currentPeak + 1, longestPeak)
				currentPeak = 0
			direction = 0
	if peakFound and currentPeak > 0:
		longestPeak = max(currentPeak + 1, longestPeak)
	return longestPeak
