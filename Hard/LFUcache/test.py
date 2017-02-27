class KeyNode(object):
	def __init__(self, key, value, freq = 1):
		self.key = key
		self.value = value
		self.freq = freq
		self.prev = self.next = None

class FreqNode(object):
	def __init__(self, freq, prev, next):
		self.freq = freq
		self.prev = prev
		self.next = next
		self.first = self.last = None

class LFUCache(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.keyDict = {}
		self.freqDict = {}
		self.head = None

	def get(self, key):
		if key in self.keyDict:
			keyNode = self.keyDict[key]
			value = keyNode.value
			self.increase(key, value)
			return value
		return -1

	def put(self, key, value):
		if self.capacity == 0:
			return
		if key in self.keyDict:
			self.increase(key, value)
			return
		if len(self.keyDict) == self.capacity:
			self.removeKeyNode(self.head.last)
		self.insertKeyNode(key, value)

	def increase(self, key, value):
		"""
		Increments the freq of an exisiting keyNode<key, value> by 1
		"""
		keyNode = self.keyDict[key]
		keyNode.value = value
		freqNode = self.freqDict[keyNode.freq]
		nextFreqNode = freqNode.next
		keyNode.freq += 1
		if nextFreqNode is None or nextFreqNode.freq > keyNode.freq:
			nextFreqNode = self.insertFreqNodeAfter(keyNode.freq, freqNode)
		self.unlinkKey(keyNode, freqNode)
		self.linkKey(keyNode, nextFreqNode)
		
	def unlinkKey(self, keyNode, freqNode):
		"""
		Unlink keyNode from freqNode
		"""
		next, prev = keyNode.next, keyNode.prev
		if prev: prev.next = next
		if next: next.prev = prev
		if freqNode.first == keyNode:
			freqNode.first = next
		if freqNode.last == keyNode:
			freqNode.last = prev
		if not freqNode.first:
			self.delFreqNode(freqNode)

	def linkKey(self, keyNode, freqNode):
		"""
		Link keyNode to freqNode
		"""
		firstKeyNode = freqNode.first
		keyNode.prev = None
		keyNode.next = firstKeyNode
		if firstKeyNode:
			firstKeyNode.prev = keyNode
		freqNode.first = keyNode
		if not freqNode.last:
			freqNode.last = keyNode

	def delFreqNode(self, freqNode):
		"""
		Delete freqNode.
		"""
		prev, next = freqNode.prev, freqNode.next
		if prev:
			prev.next = next
		if next:
			next.prev = prev
		if self.head == freqNode:
			self.head = next
		del self.freqDict[freqNode.freq]

	def removeKeyNode(self, keyNode):
		"""
		Remove keyNode
		"""
		self.unlinkKey(keyNode, self.freqDict[keyNode.freq])
		del self.keyDict[keyNode.key]

	def insertFreqNodeAfter(self, freq, node):
		"""
		Insert a new freqNode(freq) after node
		"""
		newNode = FreqNode(freq, node, node.next)
		self.freqDict[freq] = newNode
		if node.next:
			node.next.prev = newNode
		node.next = newNode
		return newNode

	def insertKeyNode(self, key, value):
		"""
		Insert a keyNode with key value pair <key, value>
		"""
		node = KeyNode(key, value)
		self.keyDict[key] = node
		freqNode = self.freqDict.get(1)
		if not freqNode:
			freqNode = FreqNode(1, None, self.head)
			self.freqDict[1] = freqNode
			if self.head:
				self.head.prev = freqNode
			self.head = freqNode
		self.linkKey(node, freqNode)

cache = LFUCache(2)
print cache.get(1)
cache.put(1, 1)
cache.put(2, 2)
print cache.get(1)
cache.put(3, 3)
print cache.get(2)
print cache.get(3)
cache.put(4, 4)
print cache.get(1)
print cache.get(3)
print cache.get(4)
