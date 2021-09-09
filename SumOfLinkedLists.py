# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(n) Space where n is the nodes in output linkedList
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
	carryOver = 0
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	linkedListSum = None
	currentNode = None
	while nodeOne is not None or nodeTwo is not None or carryOver > 0:
		unitOne = nodeOne.value if nodeOne is not None else 0
		unitTwo = nodeTwo.value if nodeTwo is not None else 0
			
		unitSum = unitOne + unitTwo + carryOver
		carryOver = unitSum // 10
		nodeSum = LinkedList(unitSum % 10)
		
		if linkedListSum is None:
			linkedListSum = nodeSum
			currentNode = nodeSum
		else:
			currentNode.next = nodeSum
			currentNode = nodeSum
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
	
    return linkedListSum
