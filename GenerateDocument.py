#O(n + m) Time | O(n) Space where n is length of characters, and m is 
# length of document array
def generateDocument(characters, document):
    # Write your code here.
	charFrequencies = {}
	for char in characters:
		if char in charFrequencies:
			charFrequencies[char] += 1
		else:
			charFrequencies[char] = 1
	for docChar in document:
		if docChar not in charFrequencies or charFrequencies[docChar] == 0:
			return False
		else:
			charFrequencies[docChar] -= 1
			
    return True
