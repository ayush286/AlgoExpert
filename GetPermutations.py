def getPermutations(array):
    # Write your code here.
	if len(array) < 1:
		return []
    chosen = []
	notChosen = array.copy()
	permutations =  getPermutationsHelper(chosen, notChosen, [])
	return permutations

#O(n^2*n!) Time | O(n*n!) Space, where n is length of array
def getPermutationsHelper(chosen, notChosen, permutations):
	if len(notChosen) == 0:
		chosenCopy = chosen.copy() # this saves lives, also 
		# when we pop it does not pop from the array itself
		permutations.append(chosenCopy)
		return permutations
	for index in range(len(notChosen)):
		chosen.append(notChosen[index])
		newNotChosen = notChosen[:index] + notChosen[index + 1:]
		permutations = getPermutationsHelper(chosen, newNotChosen, permutations)
		chosen.pop()
	return permutations
