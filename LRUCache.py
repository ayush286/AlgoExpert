# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		self.head = None
		self.headNode = None
		self.tail = None
		self.tailNode = None
		self.nodePositions = {}
		self.cache = {}
	
	#O(1) Time | O(1) Space
    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key in self.cache:
			self.cache[key] = value
			self.removeNodeInsertTail(key)
		else:
			if len(self.cache) < self.maxSize:
				self.cache[key] = value
				self.insertNode(key)
			else:
				del self.cache[self.head]
				self.removeHead()
				self.cache[key] = value
				self.insertNode(key)
	
	def removeNodeInsertTail(self, key):
		if self.tail == key:
			return
		node = self.nodePositions[key]
		if self.head == key:
			self.headNode = node.next
			self.head = self.headNode.value
		else:	
			prevNode = node.prev
			nextNode = node.next
			prevNode.next = nextNode
			nextNode.prev = prevNode
		node.next = None
		self.tailNode.next = node
		node.prev = self.tailNode
		self.tailNode = node
		self.tail = node.value
	
	
	def removeHead(self):
		if self.headNode == self.tailNode:
			self.headNode = None
			self.tailNode = None
			del self.nodePositions[self.head]
			self.head = None
			self.tail = None
		else:
			newHead = self.headNode.next
			self.headNode.next = None
			del self.nodePositions[self.head]
			self.headNode = newHead
			self.head = self.headNode.value
			self.headNode.prev = None
	
	def insertNode(self, key):
		node = Node(key)
		self.nodePositions[key] = node
		if self.tailNode is None:
			self.headNode = node
			self.tailNode = node
			self.head = key
			self.tail = key
		else:
			self.tailNode.next = node
			node.prev = self.tailNode
			self.tailNode = node
			self.tail = key
			
			
	#O(1) Time | O(1) Space
    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.cache:
			return None
		self.removeNodeInsertTail(key)
		return self.cache[key]
	
	
	#O(1) Time | O(1) Space
    def getMostRecentKey(self):
        # Write your code here.
        return self.tail
	
class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None
