# O(n*m) Time | O(n*m) Space, where m is length of allMnemonics and n
# is length of phoneNumber
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	digitToLetters = [['a','b','c'], ['d', 'e', 'f'],
					 ['g','h','i'], ['j', 'k', 'l'],
					 ['m','n','o'], ['p', 'q', 'r', 's'],
					 ['t','u','v'], ['w', 'x', 'y', 'z'],]

	allMnemonics = [""]
	allDigits = convertToDigit(phoneNumber)
	for index in range(len(allDigits)):
		if allDigits[index] == 1 or allDigits[index] == 0:
			allMnemonics = appendCharToMnemonic(str(allDigits[index]), allMnemonics, 0, len(allMnemonics))
		else:
			multiplyFactor = len(digitToLetters[allDigits[index] - 2])
			allMnemonics = multiplyMnemonics(multiplyFactor, allMnemonics)
			startIdx = 0
			endIdx = len(allMnemonics) // multiplyFactor
			counter = 1
			for char in digitToLetters[allDigits[index] - 2]:
				allMnemonics = appendCharToMnemonic(char, allMnemonics, startIdx, endIdx)
				counter += 1
				startIdx = endIdx
				endIdx = (len(allMnemonics) // multiplyFactor) * counter
	return allMnemonics


#O(m) Time | O(m) Space, where m is length of allMnemonics	
def appendCharToMnemonic(char, allMnemonics, startIdx, endIdx):
	for index in range(startIdx, endIdx):
		elem = allMnemonics[index]
		elem += char
		allMnemonics[index] = elem
	return allMnemonics


# O(m) Time | O(m) Space, where m is length of allMnemonics
def multiplyMnemonics(factor, allMnemonics):
	multipliedMnemonic = []
	for index in range(factor*len(allMnemonics)):
		index %= len(allMnemonics)
		multipliedMnemonic.append(allMnemonics[index])
	return multipliedMnemonic


# O(n) Time | O(n) Space where n is length of phoneNumber
def convertToDigit(phoneNumber):
	# create a map of letter to digit
	letterToDigit = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3,
					'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5,
					'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6,
					'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8,
					'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9,
					'z': 9}	
	allDigits = []
	for elem in phoneNumber:
		if ord(elem) < 97:
			allDigits.append(ord(elem) - ord("0"))
		else:
			digit = letterToDigit[elem]
			allDigits.append(elem)
	return allDigits
