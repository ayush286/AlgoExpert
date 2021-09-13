# O(n^2) Time | O(m) Space, where n is length of string and m is length of palindrome
def longestPalindromicSubstring(string):
    # Write your code here.
	if len(string) < 2:
		return string
	palindrome = None
	for i in range(len(string)):
		nextCharIndex = getCharIndex(string[i], string, i+1)
		while nextCharIndex != -1:	
			if isPalindrome(string[i:nextCharIndex + 1]):
				if palindrome is None:
					palindrome = string[i:nextCharIndex + 1]
				elif len(palindrome) < nextCharIndex - i + 1:
					palindrome = string[i:nextCharIndex + 1]	
			nextCharIndex = getCharIndex(string[i], string, nextCharIndex+1)
	return palindrome

def getCharIndex(char, string, start):
	for index in range(start, len(string)):
		if string[index] == char:
			return index
	return -1

def isPalindrome(string):
	left = 0
	right = len(string) - 1
	while left <= right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True
