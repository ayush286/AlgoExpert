#O(n) Time | O(n) Space where n is length of string.
def balancedBrackets(string):
    # Write your code here.
	openBrackets = "{", "(", "["
	closeBrackets = "}", ")", "]"
	brackets = []
	for char in string:
		if char in closeBrackets:
			print(char)
			print(brackets)
			if len(brackets) < 1 or brackets[-1] != openBrackets[closeBrackets.index(char)]:
				print("Hello")
				return False
			else:
				brackets.pop()
		if char in openBrackets:
			brackets.append(char)
	if len(brackets) >= 1:
		return False
	return True
