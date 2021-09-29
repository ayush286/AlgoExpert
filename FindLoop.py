# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space, where n is length of input linked list
def findLoop(head):
    # Write your code here.
	slower = None
	faster = head
	while slower != faster:
		if slower is None:
			slower = head
		slower = slower.next
		faster = faster.next.next
	# met in loop
	slower = head
	while slower != faster:
		slower = slower.next
		faster = faster.next
	return faster
