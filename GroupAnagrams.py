#O(w * n * log(n)) Time | O(wn) space, where w is the number of words and 
# n is the length of the longest word
def groupAnagrams(words):
    # Write your code here.
    anagrams = []
	for outerIdx in range(len(words)):
		currentAnagram = []
		if words[outerIdx] is None:
			continue
		for innerIdx in range(outerIdx + 1, len(words)):
			if innerIdx == len(words):
				continue
			if words[innerIdx] is None:
				continue
			if isAnagram(words[outerIdx], words[innerIdx]):
				if len(currentAnagram) == 0:
					currentAnagram.append(words[outerIdx])
				currentAnagram.append(words[innerIdx])
				words[innerIdx] = None
		if len(currentAnagram) > 0:
			anagrams.append(currentAnagram)
		else:
			anagrams.append([words[outerIdx]])
	return anagrams

def isAnagram(wordOne, wordTwo):
	if len(wordOne) != len(wordTwo):
		return False
	charsOne = []
	for char in wordOne:
		charsOne.append(ord(char))
	charsTwo = []
	for char in wordTwo:
		charsTwo.append(ord(char))
	charsOne.sort()
	charsTwo.sort()
	return charsOne == charsTwo
