#O(nlogn) Time | O(1) Space, where n is length of queries 
def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	minWaitingTime = 0
	currWaitTime = 0
	for index in range(1, len(queries)):
		currWaitTime += queries[index - 1]
		minWaitingTime += currWaitTime
	return minWaitingTime
