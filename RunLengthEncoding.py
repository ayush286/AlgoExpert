# O(n) Time | O(1) Space, where n is length of string
def runLengthEncoding(string):
    # Write your code here.
    index = 0
	encodedString = ""
	while index < len(string):
		char = string[index]
		index += 1
		counter = 0
		while counter < 8 and index < len(string) and char == string[index]:
			counter += 1
			index += 1
		encodedString += str(counter + 1) + char
	return encodedString
		
