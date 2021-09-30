# O(n) Time | O(1) Space, where n is length of input array
def waterArea(heights):
    # Write your code here.
    water = 0
	index = 0
	currPillarIdx = None
	while index < len(heights) - 1:
		if heights[index] > 0:
			if currPillarIdx is None:
				currPillarIdx = index
				continue
			nextPillarIdx = getNextPillarIdx(heights, index)
			if nextPillarIdx is None:
				break
			water += getWater(heights, currPillarIdx, nextPillarIdx)
			index = nextPillarIdx
			currPillarIdx = index
			continue
		index += 1
	return water


# returns None or index
def getNextPillarIdx(heights, index):
	maxHeightIdx = None
	currentPillar = heights[index]
	for i in range(index + 1, len(heights)):
		if heights[i] > 0:
			if heights[i] > currentPillar:
				return i
			if maxHeightIdx is None:
				maxHeightIdx = i
			else:
				if heights[i] > heights[maxHeightIdx]:
					maxHeightIdx = i
	return maxHeightIdx

def getWater(heights, currIdx, nextIdx):
	smallerPillar = min(heights[currIdx], heights[nextIdx])
	water = smallerPillar * (nextIdx - currIdx - 1)
	obstacleArea = 0
	for index in range(currIdx + 1, nextIdx):
		if heights[index] > 0:
			obstacleArea += heights[index]
	return water - obstacleArea
