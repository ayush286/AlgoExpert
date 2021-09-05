#O(n) Time | O(n) Space where n is length of input string
def reverseWordsInString(string):
    stack = []
	currentWord = ""
	runningWhitespace = False
	chars = []
	for char in string:
		chars.append(char)
	for char in chars:
		if char == " ":
			if runningWhitespace:
				currentWord += char
			else:
				stack.append(currentWord)
				currentWord = char
				runningWhitespace = True
		else:
			if runningWhitespace:
				stack.append(currentWord)
				currentWord = char
				runningWhitespace = False
			else:
				currentWord += char
	stack.append(currentWord)
	reverseString = ""
	while len(stack) >= 1:
		reverseString += stack.pop()
	return reverseString
