def interweavingStrings(one, two, three):
    # Write your code here.
	return interweavingStringsHelper(one, two, three)
    
def interweavingStringsHelper(one, two, three):
	first = 0
	second = 0
	third = 0
	while first < len(one) and second < len(two) and one[first] != two[second] and third != len(three):
		if one[first] == three[third]:
			first += 1
			third += 1
		elif two[second] == three[third]:
			second += 1
			third += 1
		elif one[first] != three[third] and two[second] != three[third]:
			return False
	if len(one) == first:
		return two[second:] == three[third:]
	elif len(two) == second:
		return one[first:] == three[third:]
	elif one[first] == two[second] and one[first] == three[third]:
		if first + 1 == len(one):
			if two[second:] == three[third + 1:]:
				return True
		elif first + 1 < len(one):
			left = interweavingStringsHelper(one[first + 1:], two[second:], three[third + 1:])
			if left:
				return True
		if second + 1 == len(two):
			if one[first:] == three[third + 1:]:
				return True
		if second + 1 < len(two):
			right = interweavingStringsHelper(one[first:], two[second + 1:], three[third + 1:])
			if right:
				return True
	return False
