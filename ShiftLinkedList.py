# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space, where n is length of linked List
def shiftLinkedList(head, k):
    # Write your code here.
	length = 0
	node = head
	tail = None
	while node is not None:
		tail = node
		node = node.next
		length += 1
	newK = getLegitK(k, length)
	if newK == 0:
		return head
	newTailPosition = getTailPosition(newK, length)
	counter = 1
	newTail = head
	while counter != newTailPosition:
		newTail = newTail.next
		counter += 1
	newHead = newTail.next
	newTail.next = None
	tail.next = head
	head = newHead
	return head

# returns k < length of list
def getLegitK(k, length):
	if k > 0:
		newK = k % length
	else:
		newK = abs(k)
		newK %= length
		newK *= -1
	return newK

def getTailPosition(k, length):
	if k > 0:
		return length - k
	else:
		return abs(k)
