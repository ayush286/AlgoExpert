# O(n^2*m) Time, O(n*m) Space, where n is length of pi and m is 
# length of numbers
def numbersInPi(pi, numbers):
    # Write your code here.
    numbersHash = {}
	for number in numbers:
		numbersHash[number] = True
	space = getMinSpaces(pi, numbersHash, {})
	if space is None:
		return -1
	else:
		return space - 1

def getMinSpaces(pi, numberDict, memo):
	if pi in memo:
		return memo[pi]
	if pi == "":
		return 0
	space = None
	for key in numberDict:
		newPi = pi[:len(key)]
		if key == newPi:
			suffix = pi[len(key):]
			currentSpace = getMinSpaces(suffix, numberDict, memo)
			if currentSpace is not None:
				if space is None:
					space = currentSpace
				else:
					space = min(space, currentSpace)
	if space is None:
		memo[pi] = space
		return space
	else:
		memo[pi] = space + 1
		return space + 1
	
