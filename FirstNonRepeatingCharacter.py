# O(n) Time | O(1) Space, where n is length of string
def firstNonRepeatingCharacter(string):
    # Write your code here.
	alphabetFrequencies = [0 for char in range(26)]
	for char in string:
		index = ord(char) - ord('a')
		alphabetFrequencies[index] += 1
	for i in range(len(string)):
		index = ord(string[i]) - ord('a')
		if alphabetFrequencies[index] == 1:
			return i
    return -1
