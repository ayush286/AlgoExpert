#O(n) Time | O(1) Space, where n is length of array
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) < 1:
		return 0
	if len(array) == 1:
		return array[0]
	prevChosen = array[0]
	prevNotChosen = 0
	currentChosen = None
	currentNotChosen = max(prevChosen, prevNotChosen)
	for elem in array[1:]:
		currentChosen = prevNotChosen + elem
		currentNotChosen = max(prevChosen, prevNotChosen)
		prevChosen = currentChosen
		prevNotChosen = currentNotChosen
	return max(currentChosen, currentNotChosen)
