# O(w*l) Time | O(n) where w is length of words, l is length of longest word,
# and n is length of neededChars
def minimumCharactersForWords(words):
    # Write your code here.
	if len(words) < 1:
		return []
	
	neededChars = list(words[0])
	for word in words:
		neededCharsCopy = neededChars.copy()
		for char in word:
			if char in neededCharsCopy:
				neededCharsCopy[neededCharsCopy.index(char)] = None
			else:
				neededChars.append(char)
    return neededChars
