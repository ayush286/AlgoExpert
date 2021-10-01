# O(n) Time | O(1) Space, where n is length of string
def caesarCipherEncryptor(string, key):
    # Write your code here.
    cryptedString = ""
	key = getKey(key)
	for char in string:
		cryptedString += getCryptedChar(char, key)
	return cryptedString

def getKey(key):
	return key % 26

def getCryptedChar(char, key):
	if ord(char) + key > ord('z'):
		newChar = chr(ord(char) - ord('z') + key + ord('a') - 1)
	else:
		newChar = chr(ord(char) + key)
	return newChar
