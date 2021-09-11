def validIPAddresses(string):
    # Write your code here.
	if len(string) < 4:
		return []
	validIPs = []
	validIPAddressesHelper(string, validIPs, "", 1)
    return validIPs


#O(1) Time | O(1) Space
def validIPAddressesHelper(notChosen, validIPs, chosenIP, octetCount):
	if len(notChosen) == 0:
		return
	if octetCount == 4:
		if isValidOctet(notChosen):
			validIP = chosenIP + notChosen
			validIPs.append(validIP)
		return
	for index in range(1,4):
		octet = notChosen[:index]
		if isValidOctet(octet):
			newChosenIP = chosenIP + octet + "."
			newNotChosen = notChosen[index:]
			validIPAddressesHelper(newNotChosen, validIPs, newChosenIP, octetCount + 1)
	return 


def isValidOctet(octet):
	if len(octet) == 0:
		return False
	if int(octet) > 255:
			return False
	if len(octet) > 1 and int(octet[0]) == 0:
		return False
	return True
