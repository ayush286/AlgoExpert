# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) Time | O(1) Space, where n is nodes of headOne and 
# m is nodes of headTwo
def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    pointerOne = headOne
	pointerTwo = headTwo
	nodeHandler = None
	mergedHead = pointerOne
	if pointerOne.value > pointerTwo.value:
		mergedHead = pointerTwo
	else:
		pointerOne = headTwo
		pointerTwo = headOne
	while pointerOne is not None and pointerTwo is not None:
		if pointerTwo.next is None:
				pointerTwo.next = pointerOne
				break
		if pointerOne.value >= pointerTwo.value and pointerOne.value < pointerTwo.next.value:
				nodeHandler = pointerOne
				pointerOne = pointerOne.next
				nodeHandler.next = pointerTwo.next
				pointerTwo.next = nodeHandler
		else:
			pointerTwo = pointerTwo.next

	return mergedHead
