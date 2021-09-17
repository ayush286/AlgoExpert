# O(n^2) Time | O(d) Space, where n is length of arrayOne, 
# and d is the depth of BST they represent
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
	if len(arrayOne) != len(arrayTwo):
		return False
	# greater than tree root ranges and sequence are same check
	rootPlusHeadIndexesOne = getRangeIndexesRootPlus(arrayOne)
	rootPlusHeadIndexesTwo = getRangeIndexesRootPlus(arrayTwo)
	if not areArrayElementsSame(arrayOne, arrayTwo,
							rootPlusHeadIndexesOne, rootPlusHeadIndexesTwo):
		return False
	else:
		for index in range(1, len(rootPlusHeadIndexesOne)):
			startOne = rootPlusHeadIndexesOne[index - 1]
			endOne = rootPlusHeadIndexesOne[index]
			startTwo = rootPlusHeadIndexesTwo[index - 1]
			endTwo = rootPlusHeadIndexesTwo[index]
			isSequenceSame = isSequenceSameWithinRangePlus(startOne, endOne, startTwo, endTwo, arrayOne, arrayTwo)
			if not isSequenceSame:
				return False
	# lesser than tree root ranges and sequence are same check
	rootMinusHeadIndexesOne = getRangeIndexesRootMinus(arrayOne)
	rootMinusHeadIndexesTwo = getRangeIndexesRootMinus(arrayTwo)
	if not areArrayElementsSame(arrayOne, arrayTwo,
								rootMinusHeadIndexesOne, rootMinusHeadIndexesTwo):
		return False
	else:
		for index in range(1, len(rootMinusHeadIndexesOne)):
			startOne = rootMinusHeadIndexesOne[index - 1]
			endOne = rootMinusHeadIndexesOne[index]
			startTwo = rootMinusHeadIndexesTwo[index - 1]
			endTwo = rootMinusHeadIndexesTwo[index]
			isSequenceSame = isSequenceSameWithinRangeMinus(startOne, endOne, startTwo, endTwo, arrayOne, arrayTwo)
			if not isSequenceSame:
				return False
	return True

def isSequenceSameWithinRangePlus(startOne, endOne, startTwo, endTwo, arrayOne, arrayTwo):
	stackOne = []
	stackTwo = []
	for index in range(len(arrayOne)):
		if arrayOne[index] >= arrayOne[startOne] and arrayOne[index] < arrayOne[endOne]:
			stackOne.append(arrayOne[index])
	for index in range(len(arrayTwo)):
		if arrayTwo[index] >= arrayTwo[startTwo] and arrayTwo[index] < arrayTwo[endTwo]:
			stackTwo.append(arrayTwo[index])
	return stackOne == stackTwo

def isSequenceSameWithinRangeMinus(startOne, endOne, startTwo, endTwo,
								   arrayOne, arrayTwo):
	stackOne = []
	stackTwo = []
	for index in range(startOne + 1, len(arrayOne)):
		if arrayOne[index] < arrayOne[startOne] and arrayOne[index] >= arrayOne[endOne]:
			stackOne.append(arrayOne[index])
	for index in range(startTwo + 1, len(arrayTwo)):
		if arrayTwo[index] < arrayTwo[startTwo] and arrayTwo[index] >= arrayTwo[endTwo]:
			stackTwo.append(arrayTwo[index])

	return stackOne == stackTwo
			
def getRangeIndexesRootPlus(array):
	rangeIndexes = [0]
	currentGreatest = array[0]
	for index in range(1, len(array)):
		if array[index] > currentGreatest:
			rangeIndexes.append(index)
			currentGreatest = array[index]
	return rangeIndexes

def getRangeIndexesRootMinus(array):
	rangeIndexes = [0]
	currentSmallest = array[0]
	for index in range(1, len(array)):
		if array[index] <= currentSmallest:
			rangeIndexes.append(index)
			currentSmallest = array[index]
	return rangeIndexes

def areArrayElementsSame(arrayOne, arrayTwo, arrayOneIndexes, arrayTwoIndexes):
	if len(arrayOneIndexes) != len(arrayTwoIndexes):
		return False
	for index in range(len(arrayOneIndexes)):
		if arrayOne[arrayOneIndexes[index]] != arrayTwo[arrayTwoIndexes[index]]:
			return False
	return True
