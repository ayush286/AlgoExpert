#O(nlogn) Time | O(n) Space, where n is length of times
def laptopRentals(times):
    # Write your code here.
	starts = []
	ends = []
	for time in times:
		starts.append(time[0])
		ends.append(time[1])
	starts.sort()
	ends.sort()
	startIdx = 0
	endIdx = 0
	minLaptops = 0
	currentLaptops = 0
	while startIdx < len(starts):
		if starts[startIdx] < ends[endIdx]:
			currentLaptops += 1
			minLaptops = max(minLaptops, currentLaptops)
			startIdx += 1
		else:
			currentLaptops -= 1
			endIdx += 1
	return minLaptops
