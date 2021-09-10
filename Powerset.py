def powerset(array):
    # Write your code here.
	possibleSets = []
    powersetHelper(array, possibleSets)
	possibleSets.append([])
	return possibleSets

#O(n*2^n) Time | O(n*2^n) Space, where n is length of input array
def powersetHelper(array, possibleSets):
	if len(array) < 1:
		return
	if array in possibleSets:
		return
	possibleSets.append(array)
	for index in range(len(array)):
		newArray = array[:index] + array[index + 1:]
		powersetHelper(newArray, possibleSets)
	return

# Solution 2

#O(n*2^n) Time | O(n*2^n) Space, where n is length of input array
def powerset(array):
    # Write your code here.
    subsets = [[]]
	for ele in array:
		for index in range(len(subsets)):
			newSet = subsets[index] + [ele]
			subsets.append(newSet)
	return subsets
