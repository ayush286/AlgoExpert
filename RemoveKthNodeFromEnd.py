# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) Time | O(1) Space, where n is length of linked list
def removeKthNodeFromEnd(head, k):
	print(k)
    # Write your code here.
	currentKthNode = None
	counter = 1
	currentNode = head
	while currentNode is not None:
		if counter == k + 1:
			currentKthNode = head
			currentNode = currentNode.next
			counter += 1
			continue
		if currentKthNode is not None:
			currentKthNode = currentKthNode.next
		currentNode = currentNode.next
		counter += 1
	if currentKthNode is None:
		head.value = head.next.value
		head.next = head.next.next
	else:
		nodeToRemove = currentKthNode.next
		currentKthNode.next = nodeToRemove.next
		nodeToRemove.next = None
