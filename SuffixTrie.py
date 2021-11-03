# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

	#O(n^2) Time | O(n^2) Space, where n is length of input string
    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for index in range(len(string)):
			suffix = string[index:]
			self.populateSuffixTrieFromHelper(suffix)		
		
	def populateSuffixTrieFromHelper(self, string):
		suffixPointer = self.root
		for char in string[:len(string) - 1]:
			if char not in suffixPointer:
				suffixPointer[char] = {}
			suffixPointer = suffixPointer[char]		
		lastChar = string[-1]
		if lastChar not in suffixPointer:
			suffixPointer[lastChar] = {self.endSymbol:True}
		else:
			hash = suffixPointer[lastChar]
			hash[self.endSymbol] = True
		return
	#O(m) Time | O(1) Space, where m is length of input string	
    def contains(self, string):
        # Write your code here.
        suffixPointer = self.root
		for char in string:
			if char not in suffixPointer:
				return False
			else:
				suffixPointer = suffixPointer[char]
		return self.endSymbol in suffixPointer
