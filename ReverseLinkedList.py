# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space, where n is length of linkedList
def reverseLinkedList(head):
    # Write your code here.
    pointerOne = head
	nodeHolder = head
	pointerTwo = None
	while pointerOne is not None:
		pointerOne = pointerOne.next
		nodeHolder.next = None
		if pointerTwo is None:
			pointerTwo = nodeHolder
		else:
			nodeHolder.next = pointerTwo
			pointerTwo = nodeHolder
		nodeHolder = pointerOne
	return pointerTwo
