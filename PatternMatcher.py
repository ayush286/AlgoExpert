# O(n^2 + m) Time | O(n) Space, where n is length of string and m is 
# length of pattern
def patternMatcher(pattern, string):
    # Write your code here.
    X = 0
	Y = 0
	n = len(string)
	# Equation will be Xx + Yy = n
	for char in pattern:
		if char == 'x':
			X += 1
		else:
			Y += 1
	for integer in reversed(range(2, min(X, Y))):
		if X % integer == 0 and Y % integer == 0:
			if n % integer != 0:
				return []
			else:
				X //= integer
				Y //= integer
				n //= integer
	swapped = False
	if Y > X:
		X, Y = Y, X
		swapped = True

	if Y == 0:
		s1 = string[:n//X]
		s = ""
		for i in range(X):
			s += s1
		if s == string:
			return ["", s1] if swapped else [s1, ""]
		else:
			return []
	
	# add chars to x and y
	for i in range(1, n//X):
		if swapped:
			result = check(string, pattern, (n - (X * i))//Y, i)
		else:
			result = check(string, pattern, i, (n - (X * i))//Y)
		if result[0]:
			return [result[1], result[2]]
	return []

def check(string, pattern, xLength, yLength):
	s1 = None
	s2 = None
	s = ""
	
	for char in pattern:
		if char is 'x':
			if s1 is None:
				s1 = string[len(s):len(s) + xLength]
			s += s1
		else:
			if s2 is None:
				s2 = string[len(s):len(s) + yLength]
			s += s2
	if s == string:
		return [True, s1, s2]
	else:
		return [False]
